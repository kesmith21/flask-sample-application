from flask import Flask, render_template, request, redirect, url_for, flash
# import flask_mysqldb as MySQL
from flask_mysqldb import MySQL
# import mysql.connector
import sqlite3 as lit


app = Flask(__name__)
app.secret_key = 'many random bytes'
#
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '$password1119'
# app.config['MYSQL_DB'] = 'crud'
#
# mysql = MySQL(app)

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="$password1119",
#     auth_plugin='mysql_native_password')



# TODO Add route for handling SQL Lite
# TODO Add route for handling SQL Server


@app.route('/')
def Index():
    # cur = mysql.connection.cursor()
    # # cur = mydb.cursor()
    # cur.execute("SELECT  * FROM crud.students")
    # data = cur.fetchall()
    # cur.close()
    db = lit.connect('employee.db')
    with db:
        cur = db.cursor()
        SQL = "select * from students"
        cur.execute(SQL)

        rows = cur.fetchall()

        # for data in rows:
        #     print(data)
    db.close()
    # return render_template('index2.html', students=data)
    return render_template('DatatablesYouTube.html', students=rows)


@app.route('/insert', methods = ['POST'])
def insert():

    # if request.method == "POST":
    #     flash("Data Inserted Successfully")
    #     name = request.form['name']
    #     email = request.form['email']
    #     phone = request.form['phone']
    #     cur = mysql.connection.cursor()
    #     # cur = mydb.cursor()
    #     cur.execute("INSERT INTO crud.students"
    #                 " (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    #     mysql.connection.commit()
    # id_data = request.form['id']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    db = lit.connect('employee.db')
    with db:
        cur = db.cursor()
        cur.execute('INSERT INTO students (name, email, phone) VALUES (?,?,?)', (name, email, phone))
    # flash("Data Updated Successfully")
        db.close()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
#     cur = mysql.connection.cursor()
#     # cur = mydb.cursor()
#     cur.execute("DELETE FROM crud.students WHERE id=%s", (id_data,))
#     mysql.connection.commit()
    db = lit.connect('employee.db')
    with db:
        cur = db.cursor()
        # cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
        cur.execute('DELETE FROM students WHERE id=?', (id_data))
    db.close()
    return redirect(url_for('Index'))
#
@app.route('/update',methods=['POST','GET'])
def update():
#
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        db = lit.connect('employee.db')
        with db:
            cur = db.cursor()
            cur.execute('UPDATE students SET name=?, email=?, phone=? WHERE id=?', (name, email, phone, id_data))
        # flash("Data Updated Successfully")
        db.close()
#         mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
