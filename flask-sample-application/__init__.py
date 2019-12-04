from flask import Flask, render_template, request, redirect, url_for, flash
# import flask_mysqldb as MySQL
from flask_mysqldb import MySQL
# import mysql.connector



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '$password1119'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="$password1119",
#     auth_plugin='mysql_native_password')



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    # cur = mydb.cursor()
    cur.execute("SELECT  * FROM crud.students")
    data = cur.fetchall()
    cur.close()


    return render_template('index2.html', students=data)



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        # cur = mydb.cursor()
        cur.execute("INSERT INTO crud.students"
                    " (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    # cur = mydb.cursor()
    cur.execute("DELETE FROM crud.students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE crud.students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)
