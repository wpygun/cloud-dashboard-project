from flask import Flask, jsonify, request, render_template
from curl_helpers import *
import sqlite3

# initialize flask app
app = Flask(__name__)

# route that used for dislaying the dashboard webpage
@app.route('/dashboard')
def dashboard():
    # gets data from curl functions as a dictionary
    os_data = curl_os_distribution()
    # split dictionary into labels and values
    os_labels = list(os_data.keys())
    os_values = list(os_data.values())

    cms_data = curl_cloud_market_share()
    cms_labels = list(cms_data.keys())
    cms_values = list(cms_data.values())

    aws_data = curl_aws_availability_zones()
    aws_labels = list(aws_data.keys())
    aws_values = list(aws_data.values())

    dcn_data = curl_data_center_numbers()
    dcn_labels = list(dcn_data.keys())
    dcn_values = list(dcn_data.values())

    # gets data from curl functions as a list
    usd_labels, usd_values = curl_usd_rates()
    chf_labels, chf_values = curl_chf_rates()

    # processes the HTML template with Jinja and then returns the data to the browser
    return render_template(
        "dashboard.html",
        os_labels=os_labels, os_values=os_values,
        cms_labels=cms_labels, cms_values=cms_values,
        aws_labels=aws_labels, aws_values=aws_values,
        dcn_labels=dcn_labels, dcn_values=dcn_values,
        usd_labels=usd_labels, usd_values=usd_values,
        chf_labels=chf_labels, chf_values=chf_values
    )

# OS distribution
# function that used to get data from SQLite table
def get_os_distribution():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM os_distribution")
    rows = cursor.fetchall()    # fetch all rows from table as a list of tuples
    cursor.close()
    connection.close()

    return dict(rows)   # converts rows into dictionary

# REST API route that gets data and returns it as JSON key-value object
@app.route('/api/os-distribution', methods=['GET'])
def os_distribution():
    return jsonify(get_os_distribution())

# Cloud market share
def get_cloud_market_share():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cloud_market_share")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return dict(rows)

@app.route('/api/cloud-market-share', methods=['GET'])
def cloud_market_share():
    return jsonify(get_cloud_market_share())

# AWS Availability Zones
def get_aws_availability_zones():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM aws_availability_zones")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return dict(rows)

@app.route('/api/aws-availability-zones', methods=['GET'])
def aws_availability_zones():
    return jsonify(get_aws_availability_zones())

# Number of Data Centers
def get_data_center_numbers():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data_center_numbers")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return dict(rows)

@app.route('/api/data-center-numbers', methods=['GET'])
def data_center_numbers():
    return jsonify(get_data_center_numbers())



if __name__ == '__main__':
    app.run(debug=True)
