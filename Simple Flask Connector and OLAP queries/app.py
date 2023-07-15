from flask import Flask, redirect, url_for, render_template, request
import os
import pandas as pd
import mysql.connector

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        curs = mysql.connection.cursor()
        curs.execute(query)
        mysql.connection.commit() # commit the change to the database
        x = curs.fetchall() # fetch all the values from the query
        dataf = pd.DataFrame(x) # using pandas library to convert the data into a table
        dataf.to_html('templates/tables.html') 
        return render_template('tables.html') #rendering the updated html file after each query
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()