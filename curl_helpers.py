import subprocess
import json

# function that used to use curl command to fetch data from REST API
def curl_os_distribution():
    # subprocess module helps to execute the curl command in a terminal
    result = subprocess.run(
        ["curl", "-s", "http://127.0.0.1:5000/api/os-distribution"],
        capture_output = True,  # used to capture output so it can be saved
        text = True             # treats data as a string
    )
    # json.loads converts JSON into dictionary
    return json.loads(result.stdout)

def curl_cloud_market_share():
    result = subprocess.run(
        ["curl", "-s", "http://127.0.0.1:5000/api/cloud-market-share"],
        capture_output = True,
        text = True
    )
    return json.loads(result.stdout)

def curl_aws_availability_zones():
    result = subprocess.run(
        ["curl", "-s", "http://127.0.0.1:5000/api/aws-availability-zones"],
        capture_output = True,
        text = True
    )
    return json.loads(result.stdout)

def curl_data_center_numbers():
    result = subprocess.run(
        ["curl", "-s", "http://127.0.0.1:5000/api/data-center-numbers"],
        capture_output = True,
        text = True
    )
    return json.loads(result.stdout)

# USD and CHF exchange rates
def curl_usd_rates():
    result = subprocess.run(
        ["curl", "-s", "http://api.nbp.pl/api/exchangerates/rates/a/usd/last/20/?format=json"],
        capture_output=True,
        text=True
    )
    data = json.loads(result.stdout)
    # create a list of numbers from 1 to 20
    labels = [i for i in range(1, 21)]
    # gets mid value from The National Bank of Poland API
    values = [item["mid"] for item in data["rates"]]
    return labels, values

def curl_chf_rates():
    result = subprocess.run(
        ["curl", "-s", "http://api.nbp.pl/api/exchangerates/rates/a/chf/last/20/?format=json"],
        capture_output=True,
        text=True
    )
    data = json.loads(result.stdout)
    labels = [i for i in range(1, 21)]
    values = [item["mid"] for item in data["rates"]]
    return labels, values
