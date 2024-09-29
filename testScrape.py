import json
import requests
from bs4 import BeautifulSoup

def scrape_power_outage_data(county_code, county_name, coordinates):
    # Replace this URL with the actual URL you want to scrape
    url = f'https://poweroutage.us/area/county/{county_code}'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the required information
    outage_data = {
        'name': county_name,
        'id': county_code,
        'companies': [],
        'customersTracked': 0,
        'customersOut': 0,
        'coordinates': coordinates
    }

    # Get the number of customers tracked and out
    tracked = soup.find(text="Customers Tracked").find_next('div')
    out = soup.find(text="Customers Out").find_next('div')

    if tracked:
        outage_data['customersTracked'] = int(tracked.text.replace(',', ''))
    if out:
        outage_data['customersOut'] = int(out.text.replace(',', ''))

    # Extract electric providers
    providers_table = soup.find('table', class_='table-striped')
    if providers_table:
        rows = providers_table.find_all('td', class_ = "row")[1:]  # Skip header row
        for row in rows:
            # Find the company name from the 'a' element
            company_name = row.find('a').text.strip() if row.find('a') else 'N/A'
            # Find all divs with class 'text-right' (assuming customer values are here)
            customer_values = [div.text.strip().replace(',', '') for div in row.find_all('div', class_='text-right')]
            # Only take the first two customer values
            customer_values = customer_values[:2]
            # Convert the customer values to integers if they exist, otherwise set to 0
            total_value = int(customer_values[0]) if len(customer_values) > 0 and customer_values[0].isdigit() else 0
            out_value = int(customer_values[1]) if len(customer_values) > 1 and customer_values[1].isdigit() else 0
            # Create a dictionary for each company

            outage_data['companies'].append({"name":  company_name,
                    "curOut": out_value,
                    "totalCustomers": total_value})


    # Save the scraped data to florida_outages.json
    # with open('florida_outages.json', 'w') as json_file:
    #     json.dump(outage_data, json_file)

    return outage_data  # Optionally return data if needed
