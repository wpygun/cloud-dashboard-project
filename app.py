from flask import Flask, jsonify, render_template
from api_fetcher import get_dashboard_data, get_nbp_data
import sqlite3

# initialize flask app
app = Flask(__name__)

# route that used for displaying the dashboard webpage
@app.route('/dashboard')
def dashboard():
    # fetches data from a function as a dictionary
    os_data = get_dashboard_data("os-distribution")
    # split dictionary into labels and values
    os_labels = list(os_data.keys())
    os_values = list(os_data.values())

    cms_data = get_dashboard_data("cloud-market-share")
    cms_labels = list(cms_data.keys())
    cms_values = list(cms_data.values())

    aws_data = get_dashboard_data("aws-availability-zones")
    aws_labels = list(aws_data.keys())
    aws_values = list(aws_data.values())

    dcn_data = get_dashboard_data("data-center-numbers")
    dcn_labels = list(dcn_data.keys())
    dcn_values = list(dcn_data.values())

    # fetches data from a functions as a list
    usd_labels, usd_values = get_nbp_data("usd")
    chf_labels, chf_values = get_nbp_data("chf")

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

# function that used to query the data from SQLite table
def query_db_table(table_name):
    white_list = ["os_distribution", "cloud_market_share", "aws_availability_zones", "data_center_numbers"]
    if table_name not in white_list:
        return jsonify({"error": "invalid table name"})
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()    # fetches all rows from table as a list of tuples

        return dict(rows)   # converts rows into dictionary

# REST API routes that gets data and returns it as JSON key-value object

# OS distribution
@app.route('/api/os-distribution', methods=['GET'])
def os_distribution():
    return jsonify(query_db_table("os_distribution"))

# Cloud market share
@app.route('/api/cloud-market-share', methods=['GET'])
def cloud_market_share():
    return jsonify(query_db_table("cloud_market_share"))

# AWS Availability Zones
@app.route('/api/aws-availability-zones', methods=['GET'])
def aws_availability_zones():
    return jsonify(query_db_table("aws_availability_zones"))

# Number of Data Centers
@app.route('/api/data-center-numbers', methods=['GET'])
def data_center_numbers():
    return jsonify(query_db_table("data_center_numbers"))



if __name__ == '__main__':
    app.run(debug=True)
