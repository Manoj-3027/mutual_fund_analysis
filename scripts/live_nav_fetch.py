import requests
import pandas as pd
import os

# Mutual fund scheme codes
funds = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Save location
SAVE_PATH = "../data/raw"

# Fetch NAV data
for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_data = data.get("data", [])

        df = pd.DataFrame(nav_data)

        output_file = os.path.join(
            SAVE_PATH,
            f"{fund_name}_nav.csv"
        )

        df.to_csv(output_file, index=False)

        print(f"{fund_name} NAV saved successfully")

    else:
        print(f"Failed to fetch {fund_name}")