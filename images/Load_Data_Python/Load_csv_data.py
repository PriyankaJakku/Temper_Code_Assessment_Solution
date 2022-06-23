#!/usr/bin/env python

import csv
import json
import mysql.connector as msql
from mysql.connector import Error
import pandas as pd


# read the places CSV data
Placesdata = pd.read_csv('/data/places.csv', index_col=False, encoding='utf-8',delimiter = ',')
Placesdata.head()

# read the people CSV data
Peopledata = pd.read_csv('/data/people.csv', index_col=False, encoding='utf-8',delimiter = ',')
Peopledata.head()


# connect to the database
try:
    conn = msql.connect(host='database', user='temper_code_test',  database='temper_code_test',
                        password='good_luck')
    if conn.is_connected():
        cursor = conn.cursor()
        print("Connected to Database")
        cursor.execute('DROP TABLE IF EXISTS temper_code_test.people')
        cursor.execute("create table temper_code_test.people (id int not null auto_increment,First_Name varchar(100),Last_Name varchar(100),DOB Date,POB varchar(100),primary key (id),FOREIGN KEY (POB) REFERENCES places(city))")
        print("Table people is created.")
        cursor.execute('DROP TABLE IF EXISTS temper_code_test.places')
        cursor.execute("create table temper_code_test.places (City varchar(100),Country varchar(100),Provience varchar(100) NOT NULL,primary key (city))")
        print("Table places is created.")
        # Insert data into Mysql Tables
        for i,row in Placesdata.iterrows():
            places_sql = "INSERT INTO temper_code_test.places VALUES (%s,%s,%s)"
            cursor.execute(places_sql, tuple(row))
            conn.commit()
        for i,row in Peopledata.iterrows():
            people_sql = "INSERT INTO temper_code_test.people VALUES(%s,%s,%s,%s)"
            cursor.execute(people_sql, tuple(row))
            conn.commit()
            
        # output the table to a JSON file
        with open('/data/summary_output.json', 'w', encoding='utf-8') as json_file:
          query = "select places.provience,count(*) from temper_code_test.places places join temper_code_test.people people on places.Provience=people.POB group by places.provience"
          cursor.execute(query)
          # Fetch all the records
          result = cursor.fetchall()
          rows = [{'Provience': row[0], 'Count': row[1]} for row in result]
          json.dump(rows, json_file, separators=(',', ':'))
        
except Error as e:
    print("Error while connecting to MySQL", e)



        







