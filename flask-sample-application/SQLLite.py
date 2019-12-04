import sqlite3 as lit

def main():

    try:
        db = lit.connect('employee.db')

        # create table
        # cur = db.cursor()

        # tablequery = "create table users (id int, name TEXT, email TEXT)"
        # cur.execute(tablequery)
        # print("table created")


        # myusers = (
        #
        #     (3,'Jennifer','kesmith21@gmail.com'),
        #     (4, 'Lucy', 'kesmith21@gmail.com')
        # )
        #
        # with db:
        #     cur = db.cursor()
        #     cur.executemany('Insert into users values (?,?,?)',myusers)
        #
        #     print("records added")

        with db:
            cur = db.cursor()
            SQL = "select * from students"
            cur.execute(SQL)

            rows = cur.fetchall()

            for data in rows:
                print(data)



            print("records selected")

    except:
        print("Failed")

    finally:
        db.close()

if __name__ == "__main__":
    main()