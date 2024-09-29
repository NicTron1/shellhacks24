
from testScrape import scrape_power_outage_data  # Import the scrape function
import json


county_coords = {
    "Escambia": [-87.2602, 30.6916],
    "Santa Rosa": [-86.9066, 30.7745],
    "Okaloosa": [-86.6182, 30.5774],
    "Walton": [-86.2402, 30.6470],
    "Holmes": [-85.6220, 30.8590],
    "Jackson": [-85.2260, 30.7753],
    "Washington": [-85.6972, 30.5972],
    "Bay": [-85.6159, 30.1587],
    "Calhoun": [-85.2087, 30.3265],
    "Gadsden": [-84.5795, 30.5890],
    "Liberty": [-84.8506, 30.3330],
    "Gulf": [-85.1945, 29.7368],
    "Franklin": [-84.8939, 29.7604],
    "Wakulla": [-84.3552, 30.2104],
    "Leon": [-84.2807, 30.4383],
    "Jefferson": [-83.9895, 30.3533],
    "Madison": [-83.4058, 30.4460],
    "Hamilton": [-83.2073, 30.4213],
    "Taylor": [-83.5585, 30.2178],
    "Columbia": [-82.6423, 30.5952],
    "Suwannee": [-83.0826, 30.2903],
    "Lafayette": [-83.1577, 30.1896],
    "Gilchrist": [-82.8913, 29.6078],
    "Dixie": [-83.1334, 29.5764],
    "Levy": [-82.6681, 29.1095],
    "Baker": [-82.3002, 30.3017],
    "Union": [-82.3296, 30.0842],
    "Bradford": [-82.1349, 29.9522],
    "Alachua": [-82.3018, 29.6516],
    "Nassau": [-81.5828, 30.5994],
    "Monroe": [-81.5831, 24.7840],
    "Miami-Dade": [-80.2442, 25.7617],
    "Duval": [-81.5393, 30.3322],
    "Clay": [-81.7495, 29.9980],
    "St. Johns": [-81.2519, 29.4082],
    "Putnam": [-81.7211, 29.6492],
    "Flagler": [-81.2519, 29.4082],
    "Marion": [-82.1401, 29.1609],
    "Citrus": [-82.5239, 28.7004],
    "Volusia": [-81.3493, 29.0275],
    "Lake": [-81.7464, 28.4023],
    "Sumter": [-82.0954, 28.6380],
    "Hernando": [-82.4334, 28.5384],
    "Orange": [-81.2020, 28.5641],
    "Seminole": [-81.1966, 28.7022],
    "Brevard": [-80.6081, 28.3922],
    "Osceola": [-81.1200, 28.0932],
    "Polk": [-81.9560, 27.8684],
    "Pasco": [-82.4310, 28.3216],
    "Hillsborough": [-82.4572, 27.9949],
    "Pinellas": [-82.7405, 27.8765],
    "Indian River": [-80.6130, 27.6353],
    "Manatee": [-82.5176, 27.4862],
    "Sarasota": [-82.4544, 27.3364],
    "Hardee": [-81.8332, 27.2247],
    "Desoto": [-81.8332, 27.2247],
    "Highlands": [-81.2654, 27.3444],
    "Glades": [-81.1276, 26.2418],
    "Okeechobee": [-80.8283, 27.2416],
    "St. Lucie": [-80.4105, 27.1949],
    "Martin": [-80.4105, 27.1949],
    "Charlotte": [-82.0288, 26.9342],
    "Lee": [-81.8015, 26.6633],
    "Hendry": [-81.4250, 26.2013],
    "Palm Beach": [-80.3940, 26.7050],
    "Collier": [-81.6954, 26.1950],
    "Broward": [-80.1918, 26.1901]
}

florida_counties = {
    "Escambia": 2272,
    "Santa Rosa": 2276,
    "Okaloosa": 2275,
    "Walton": 2277,
    "Holmes": 2273,
    "Jackson": 2274,
    "Washington": 2278,
    "Bay": 292,
    "Calhoun": 2343,
    "Gadsden": 306,
    "Liberty": 323,
    "Gulf": 309,
    "Franklin": 305,
    "Wakulla": 349,
    "Leon": 321,
    "Jefferson": 317,
    "Madison": 324,
    "Hamilton": 310,
    "Taylor": 345,
    "Columbia": 300,
    "Suwannee": 344,
    "Lafayette": 318,
    "Gilchrist": 307,
    "Dixie": 302,
    "Levy": 322,
    "Baker": 291,
    "Union": 346,
    "Bradford": 293,
    "Alachua": 290,
    "Nassau": 330,
    "Monroe": 329,
    "Miami-Dade": 328,
    "Duval": 303,
    "Clay": 298,
    "St. Johns": 2317,
    "Putnam": 338,
    "Flagler": 304,
    "Marion": 326,
    "Citrus": 297,
    "Volusia": 348,
    "Lake": 319,
    "Sumter": 343,
    "Hernando": 313,
    "Orange": 332,
    "Seminole": 340,
    "Brevard": 294,
    "Osceola": 333,
    "Polk": 337,
    "Pasco": 335,
    "Hillsborough": 315,
    "Pinellas": 336,
    "Indian River": 316,
    "Manatee": 325,
    "Sarasota": 339,
    "Hardee": 311,
    "Desoto": 2340,
    "Highlands": 314,
    "Glades": 308,
    "Okeechobee": 331,
    "St. Lucie": 342,
    "Martin": 327,
    "Charlotte": 296,
    "Lee": 320,
    "Hendry": 312,
    "Palm Beach": 334,
    "Collier": 299,
    "Broward": 295
}


# @app.route('/')  # Only one route for the root URL
# def home():  # Changed function name from index to home
#     return render_template('index.html')  # This will serve your HTML page

# @app.route('/get-county-code', methods=['POST'])
# def get_county_code():
#     data = request.get_json()
#     county_name = data.get('countyName', '').lower()

#     if county_name in florida_counties:
#         county_code = florida_counties[county_name]
#         scrape_power_outage_data(county_code, county_name)  # Call the scraping function (data will be saved to JSON)
#         return jsonify({'countyCode': county_code})  # Just return the county code
#     else:
#         return jsonify({'error': 'County not found'}), 404

if __name__ == '__main__':
    data = {
        "counties": [

        ]
    }
    for county in florida_counties:
        newData = scrape_power_outage_data(florida_counties[county], county, county_coords[county])
        data["counties"].append(newData)
    with open('/home/bitnami/htdocs/shellhacks24/templates/counties.json', 'w') as file:
        json.dump(data, file)
