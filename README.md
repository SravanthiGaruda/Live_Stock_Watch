# Live_Stock_Watch

This project aims to provide real-time stock visualization using a combination of Python, Yahoo Finance API, Apache Cassandra, and Grafana. The workflow includes fetching real-time stock data using Python, storing it in Cassandra, and visualizing it using Grafana.

Prerequisites
- Apache Cassandra
- Grafana
- Python 3.x
- Yahoo Finance API

Installation

1.	Apache Cassandra
  a.	Installations to be done on MacOS
    •	Install Apache Cassandra using Homebrew: brew install Cassandra
    •	Start Cassandra service:  brew services start Cassandra
    •	Access Cassandra shell (CQLSH): cqlsh
    •	Create the database and table in Cassandra:
      1.	CREATE KEYSPACE stock_data WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
      2.	 USE stock_data;
      3.	CREATE TABLE stocks (
        					name TEXT PRIMARY KEY,
        					timestamp TIMESTAMP,
        					price DECIMAL);

2.	Grafana
   a.	Installations to be done on MacOS
      •	Download Grafana:
        - curl -O https://dl.grafana.com/enterprise/release/grafana-enterprise-11.0.0.darwin-amd64.tar.gz
      •	Extract the downloaded file: 
        - tar -zxvf grafana-enterprise-11.0.0.darwin-amd64.tar.gz
      •	Navigate to the Grafana directory: 
        - cd grafana-11.0.0
      •	Start Grafana server:  ./bin/grafana-server
      •	Keep the server running  and open Grafana in your brower:  
        - http://localhost:3000
        - log in with the default credentials 
          - username: admin
          -  password: admin
      •	Add Cassandra to your Data Source:  
        - Go to Configuration -> Data Source
        - Click on `Add data source`
        - Select `Apache Cassandra`
        -	Provide the host details(e.g., 127.0.0.1:9042)
        -	Keyspace (database name : `stock_db`)
      •	Create Visualization:
        -	Go to Create -> Dashboard
        -	Add a new visualization -> select database -> and select `Query`
        -	Write a query to fetch data from the Cassandra database:  
          -	select * from stock_db.stockprice where name=`stock_name` ALLOW FILTERING;
        -	Configure the visualizations as needed.

3.	Python Script
  •	Install required libraries:
   -	pip install yfinance cassandra-driver

4.	Things to Change in Code:
  •	Database Name (eg: stock_db)
  •	Stock Names (eg: ['RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'INFY.NS', 'SBIN.NS', 'KOTAKBANK.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS'])
  •	Query according to the columns in the table (eg: """ INSERT INTO stockprice (name, price, timestamp) VALUES (%s, %s, %s)""")

