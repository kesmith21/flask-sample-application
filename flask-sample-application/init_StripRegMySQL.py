from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# import flask_mysqldb as MySQL
from flask_mysqldb import MySQL
# import mysql.connector



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '$password1119'
app.config['MYSQL_DB'] = 'stripregistration'
# app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="$password1119",
#     auth_plugin='mysql_native_password')


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT CounterMeasureID, DATE_FORMAT(DateAdded, '%m/%d/%Y') DateAdded, DATE_FORMAT(DateClosed, '%m/%d/%Y') DateClosed, item, portion, Discrepancy "
                "FROM stripregistration.countermeasure")
    # cur.execute("SELECT  * FROM crud.students")
    data = cur.fetchall()

    # return render_template('index2.html', students=data)
    # return render_template('DatatablesYouTube.html', students=data)
    # colours = ['All','2007', '2009', '3009', '4038']
    cur.execute("SELECT  CounterMeasureID FROM stripregistration.countermeasure order by CounterMeasureID")
    rv = cur.fetchall()
    colours = ['All']
    content = {}
    for result in rv:
        content = result[0]
        colours.append(content)
        content = {}
    # CMID = jsonify(payload)
    cur.close()
    return render_template('StripCM.html', countermeasures=data, colours=colours)


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO crud.students"
                    " (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))



@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM stripregistration.countermeasure WHERE CounterMeasureID=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update',methods=['POST','GET'])
def update():

        if request.method == 'POST':
            id_data = request.form['CounterMeasureID']
            item = request.form['item']
            portion = request.form['portion']
            discrepancy = request.form['discrepancy']
            cur = mysql.connection.cursor()
            cur.execute("""
                   UPDATE stripregistration.countermeasure
                   SET item=%s, portion=%s, discrepancy=%s
                   WHERE CounterMeasureID=%s
                """, (item, portion, discrepancy, id_data))
            flash("Data Updated Successfully")
            mysql.connection.commit()
            return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
