

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


# Input is an example, searchString needs to mirror the input received from the search
# bar in the frontend. The input will be ".lower()", and then request will be sent to the dictionary,
# the value of the key will be returned and pushed to the back of the URL for data to be scraped.

searchString = input("What is the county\n").lower()

#Searches for key in the dictionary, adds value to the end of the URL for scraper to run through
if searchString in florida_counties:
    value = florida_counties[searchString]
    print(value)
    print("https://poweroutage.us/area/county/"+str(value))


# Example: Accessing value for Miami-Dade
#print(florida_counties["Miami-Dade"])
