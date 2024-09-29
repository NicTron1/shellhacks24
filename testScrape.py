import requests
from bs4 import BeautifulSoup
import json

# Replace 'your_url_here' with the actual URL
url = 'https://poweroutage.us/area/county/315'
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with class 'table-striped'
table = soup.find('table', class_='table-striped')

# If the table is found, find all the rows within the table
if table:
    rows = table.find_all('td', class_='row')

    # Initialize a list to store all the row data in JSON format
    data_list = []

    # Loop through each row to find company name and customer values
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
        company_data = {
            "name": company_name,
            "total": total_value,
            "out": out_value
        }

        # Append the dictionary to the list
        data_list.append(company_data)

    # Output the list in JSON format
    print(json.dumps(data_list, indent=2))

else:
    print("Table with class 'table-striped' not found.")
