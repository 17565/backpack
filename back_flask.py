from flask import Flask, g, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = 'food_backpack.db'

#access database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#closes connetion
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#displays data
@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM food"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

#adds item to database
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        new_name = request.form["item_name"]
        new_cost = request.form["item_cost"]
        sql = "INSERT INTO food(food_item, cost) VALUES (?,?)"
        cursor.execute(sql,(new_name, new_cost))
        get_db().commit()
    return redirect("/")

#delete items from database
@app.route("/delete",methods=["GET","POST"])
def delete():
    if request.method =="POST":
        cursor = get_db().cursor()
        id = int(request.form["it_name"])
        sql = "DELETE FROM food WHERE id = ?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect("/")

#runs app
if __name__ == "__main__":
    app.run(debug=True)


