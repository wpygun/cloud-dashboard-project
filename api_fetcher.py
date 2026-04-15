import requests

env = "prod"  # "local" or "prod"
base_urls = {
    "local": "http://127.0.0.1:5000/api/",
    "prod": "https://cloud-dashboard-project.onrender.com/api/",
}
base_url = base_urls[env]
nbp_url = "http://api.nbp.pl/api/exchangerates/rates/a/"

# function that fetches data from REST API using requests library
def get_dashboard_data(endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    # .json() converts JSON into dictionary
    return response.json()

# USD and CHF exchange rates
def get_nbp_data(endpoint):
    response = requests.get(f"{nbp_url}{endpoint}/last/20/?format=json")
    data = response.json()
    # create a list of numbers from 1 to 20
    labels = list(range(1, 21))
    # gets mid-value from The National Bank of Poland API
    values = [item["mid"] for item in data["rates"]]
    return labels, values