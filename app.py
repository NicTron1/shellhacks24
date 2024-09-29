from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    data = request.get_json()  # Get the JSON data from the request
    county_name = data.get('countyName', '').lower()  # Get the county name and convert to lowercase

    # Check if the county name exists in the dictionary
    if county_name in florida_counties:
        return jsonify({'countyCode': florida_counties[county_name]})
    else:
        return jsonify({'error': 'County not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
