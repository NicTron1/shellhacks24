from flask import Flask, render_template, request, jsonify
from testScrape import scrape_power_outage_data  # Import the scrape function
import json

app = Flask(__name__)

county_coords = {
    "escambia": [-87.2602, 30.6916],
    "santa rosa": [-86.9066, 30.7745],
    "okaloosa": [-86.6182, 30.5774],
    "walton": [-86.2402, 30.6470],
    "holmes": [-85.6220, 30.8590],
    "jackson": [-85.2260, 30.7753],
    "washington": [-85.6972, 30.5972],
    "bay": [-85.6159, 30.1587],
    "calhoun": [-85.2087, 30.3265],
    "gadsden": [-84.5795, 30.5890],
    "liberty": [-84.8506, 30.3330],
    "gulf": [-85.1945, 29.7368],
    "franklin": [-84.8939, 29.7604],
    "wakulla": [-84.3552, 30.2104],
    "leon": [-84.2807, 30.4383],
    "jefferson": [-83.9895, 30.3533],
    "madison": [-83.4058, 30.4460],
    "hamilton": [-83.2073, 30.4213],
    "taylor": [-83.5585, 30.2178],
    "columbia": [-82.6423, 30.5952],
    "suwannee": [-83.0826, 30.2903],
    "lafayette": [-83.1577, 30.1896],
    "gilchrist": [-82.8913, 29.6078],
    "dixie": [-83.1334, 29.5764],
    "levy": [-82.6681, 29.1095],
    "baker": [-82.3002, 30.3017],
    "union": [-82.3296, 30.0842],
    "bradford": [-82.1349, 29.9522],
    "alachua": [-82.3018, 29.6516],
    "nassau": [-81.5828, 30.5994],
    "monroe": [-81.5831, 24.7840],
    "miami-dade": [-80.2442, 25.7617],
    "duval": [-81.5393, 30.3322],
    "clay": [-81.7495, 29.9980],
    "st. johns": [-81.2519, 29.4082],
    "putnam": [-81.7211, 29.6492],
    "flagler": [-81.2519, 29.4082],
    "marion": [-82.1401, 29.1609],
    "citrus": [-82.5239, 28.7004],
    "volusia": [-81.3493, 29.0275],
    "lake": [-81.7464, 28.4023],
    "sumter": [-82.0954, 28.6380],
    "hernando": [-82.4334, 28.5384],
    "orange": [-81.2020, 28.5641],
    "seminole": [-81.1966, 28.7022],
    "brevard": [-80.6081, 28.3922],
    "osceola": [-81.1200, 28.0932],
    "polk": [-81.9560, 27.8684],
    "pasco": [-82.4310, 28.3216],
    "hillsborough": [-82.4572, 27.9949],
    "pinellas": [-82.7405, 27.8765],
    "indian river": [-80.6130, 27.6353],
    "manatee": [-82.5176, 27.4862],
    "sarasota": [-82.4544, 27.3364],
    "hardee": [-81.8332, 27.2247],
    "desoto": [-81.8332, 27.2247],
    "highlands": [-81.2654, 27.3444],
    "glades": [-81.1276, 26.2418],
    "okeechobee": [-80.8283, 27.2416],
    "st.lucie": [-80.4105, 27.1949],
    "martin": [-80.4105, 27.1949],
    "charlotte": [-82.0288, 26.9342],
    "lee": [-81.8015, 26.6633],
    "hendry": [-81.4250, 26.2013],
    "palm beach": [-80.3940, 26.7050],
    "collier": [-81.6954, 26.1950],
    "broward": [-80.1918, 26.1901]
}


# Your county dictionary
florida_counties = {
    "escambia": 2272,
    "santa rosa": 2276,
    "okaloosa": 2275,
    "walton": 2277,
    "holmes": 2273,
    "jackson": 2274,
    "washington": 2278,
    "bay": 292,
    "calhoun": 2343,
    "gadsden": 306,
    "liberty": 323,
    "gulf": 309,
    "franklin": 305,
    "wakulla": 349,
    "leon": 321,
    "jefferson": 317,
    "madison": 324,
    "hamilton": 310,
    "taylor": 345,
    "columbia": 300,
    "suwannee": 344,
    "lafayette": 318,
    "gilchrist": 307,
    "dixie": 302,
    "levy": 322,
    "baker": 291,
    "union": 346,
    "bradford": 293,
    "alachua": 290,
    "nassau": 330,
    "monroe": 329,
    "miami-dade": 328,
    "duval": 303,
    "clay": 298,
    "st. johns": 2317,
    "putnam": 338,
    "flagler": 304,
    "marion": 326,
    "citrus": 297,
    "volusia": 348,
    "lake": 319,
    "sumter": 343,
    "hernando": 313,
    "orange": 332,
    "seminole": 340,
    "brevard": 294,
    "osceola": 333,
    "polk": 337,
    "pasco": 335,
    "hillsborough": 315,
    "pinellas": 336,
    "indian river": 316,
    "manatee": 325,
    "sarasota": 339,
    "hardee": 311,
    "desoto": 2340,
    "highlands": 314,
    "glades": 308,
    "okeechobee": 331,
    "st.lucie": 342,
    "martin": 327,
    "charlotte": 296,
    "lee": 320,
    "hendry": 312,
    "palm beach": 334,
    "collier": 299,
    "broward": 295
}

@app.route('/')  # Only one route for the root URL
def home():  # Changed function name from index to home
    return render_template('index.html')  # This will serve your HTML page

@app.route('/get-county-code', methods=['POST'])
def get_county_code():
    data = request.get_json()
    county_name = data.get('countyName', '').lower()

    if county_name in florida_counties:
        county_code = florida_counties[county_name]
        scrape_power_outage_data(county_code, county_name)  # Call the scraping function (data will be saved to JSON)
        return jsonify({'countyCode': county_code})  # Just return the county code
    else:
        return jsonify({'error': 'County not found'}), 404

if __name__ == '__main__':
    data = {
        "counties": [

        ]
    }
    for county in florida_counties:
        newData = scrape_power_outage_data(florida_counties[county], county, county_coords[county])
        data["counties"].append(newData)
    with open('./templates/counties.json', 'w') as file:
        json.dump(data, file)
