from flask import Flask, render_template, request, redirect, url_for, flash
from google.cloud.sql.connector import Connector
from sqlalchemy import text

import sqlalchemy
import os
import pymysql

app = Flask(__name__)
credential_path = "/Users/song15101556787/Desktop/fa22-cs411-A-team025-crack411/basketball/cs411-project-366021-ac0ccade16f9.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
# initialize Connector object
connector = Connector()


# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "cs411-project-366021:us-central1:myinstance",
        "pymysql",
        user="root",
        password="12345",
        db="project"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
# with pool.connect() as db_conn:
#     # query database
    
#     result = db_conn.execute("SELECT * from Player").fetchall()

#     # Do something with the results
#     for row in result:
#         print(row)

@app.route('/')
def Index():
    with pool.connect() as db_conn:
        result = db_conn.execute("SELECT * from Player").fetchall()
    return render_template('test.html', player = result)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        Player_ID = request.form['playerID']    
        Name = request.form['name']
        Height = request.form['height']  
        Weight = request.form['weight']
        Age = request.form['age']
        Country = request.form['country']
        TeamName = request.form['teamName']
        CollegeName = request.form['collegeName']
        Movie_ID = request.form['movieID']
        
        with pool.connect() as db_conn:
            db_conn.execute("INSERT INTO Player (Player_ID, Name, Height, Weight, Age, Country, TeamName, CollegeName, Movie_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Player_ID, Name, Height, Weight, Age, Country, TeamName, CollegeName, Movie_ID))
        # conn.commit()
        return redirect(url_for('Index'))     


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    # flash("Record Has Been Deleted Successfully")
    # cur = mysql.connection.cursor()
    with pool.connect() as db_conn:
        db_conn.execute("DELETE FROM Player WHERE Player_ID=%s", (id_data))
    return redirect(url_for('Index'))


@app.route('/update', methods = ['POST'])
def update():
    # print("hello there")
    if request.method == "POST":
        player_ID = request.form['playerID']    
        name = request.form['name']
        height = request.form['height']  
        weight = request.form['weight']
        age = request.form['age']
        country = request.form['country']
        teamName = request.form['teamName']
        collegeName = request.form['collegeName']
        movie_ID = request.form['movieID']
        
        with pool.connect() as db_conn:
            db_conn.execute("""
                UPDATE Player
                SET Name = %s, Height = %s, Weight = %s, Age = %s,Country = %s,TeamName = %s, CollegeName = %s, Movie_ID = %s
                WHERE Player_ID = %s """, (name, height, weight, age, country, teamName, collegeName, movie_ID, player_ID))
        return redirect(url_for('Index'))    

@app.route('/search', methods = ['POST'])
def search():
    name = request.form['name']
    sql = text("SELECT * from Player WHERE Name like '"+name+"%'")
    with pool.connect() as db_conn:
        result = db_conn.execute(sql).fetchall()
        
    return render_template('test.html', player = result)


@app.route('/advanceSearch1')
def advanceSearch1():
    # name = request.form['name']
    sql = text(" SELECT p.Player_ID, p.Name, p.Height, p.Weight, p.Age, p.Country, p.TeamName, p.CollegeName, p.Movie_ID FROM Player p left join College c on (p.CollegeName = c.Name) Where c.City like 'A%' ")
    with pool.connect() as db_conn:
        result = db_conn.execute(sql).fetchall()
    return render_template('test.html', player = result)



@app.route('/advanceSearch2')
def advanceSearch2():
    # name = request.form['name']
    sql = text("SELECT * FROM Player Where Movie_ID IN (SELECT id From movie_and_genre_sql WHERE movie like 'P%')")
    with pool.connect() as db_conn:
        result = db_conn.execute(sql).fetchall()
    return render_template('test.html', player = result)

@app.route('/show_s_rank_player')
def show_s_rank_player():
    # name = request.form['name']
    sql = text("call SPlayer()")
    with pool.connect() as db_conn:
        result = db_conn.execute(sql).fetchall()
    return render_template('test.html', player = result)

@app.route('/show_a_rank_player')
def show_a_rank_player():
    # name = request.form['name']
    sql = text("call APlayer()")
    with pool.connect() as db_conn:
        result = db_conn.execute(sql).fetchall()
    return render_template('test.html', player = result)


@app.route('/show_b_rank_player')
def show_b_rank_player():
    # name = request.form['name']
    sql = text("call BPlayer()")
    with pool.connect() as db_conn:
        result = db_conn.execute(sql).fetchall()
    return render_template('test.html', player = result)

@app.route('/show_c_rank_player')
def show_c_rank_player():
    # name = request.form['name']
    sql = text("call CPlayer()")
    with pool.connect() as db_conn:
        result = db_conn.execute(sql).fetchall()
    return render_template('test.html', player = result)

@app.route('/open/<string:id_data>', methods = ['GET'])
def open(id_data):
    with pool.connect() as db_conn:
        result=db_conn.execute("select StatsID,Name,PTS,FG,ThreePT,REB,AST,STL,BLK from Stats left join Player p on Stats.StatsID=p.Player_ID WHERE Player_ID=%s", (id_data))
    return render_template('Untitled-2.html', player = result)

# a = SELECT(id From movie_and_genre_sql WHERE movie like ('P%'))
if __name__ == "_main_":
    app.run(debug=True)