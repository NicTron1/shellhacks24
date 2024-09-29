import json
import requests
from bs4 import BeautifulSoup

def scrape_power_outage_data(county_code, county_name):
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
        'customersOut': 0
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
        rows = providers_table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 4:  # Ensure there are enough columns
                company_name = columns[0].text.strip()
                customers_tracked = int(columns[1].text.strip().replace(',', ''))
                customers_out = int(columns[2].text.strip().replace(',', ''))

                outage_data['companies'].append({
                    'name': company_name,
                    'tracked': customers_tracked,
                    'out': customers_out
                })

    # Save the scraped data to florida_outages.json
    with open('florida_outages.json', 'w') as json_file:
        json.dump(outage_data, json_file)

    return outage_data  # Optionally return data if needed
