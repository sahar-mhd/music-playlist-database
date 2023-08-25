import sqlalchemy as db

if __name__ == '__main__':
    username = input("enter your username ")
    password = input("enter your password ")
    try:
        engine = db.create_engine("mysql+pymysql://" + username + ":" + password + "@127.0.0.1:3306/db_Project3")
        connection = engine.connect()
        while 1:
            func = input("create|read|update|delete? ")
            if func.__eq__("create"):
                table = input("name of the table? ")
                values = input("values? ")
                query = db.text("create table " + table + "(" + values + ");")
                connection.execute(query)
            elif func.__eq__("read"):
                table = input("from which table? ")
                query = db.text("select * from " + table + ";")
                result = connection.execute(query)
                x = result.fetchall()
                print(x)
            elif func.__eq__("update"):
                table = input("which table? ")
                column = input("which column? ")
                where = input("where? ")
                query = db.text("update " + table + " set " + column + " where " + where + ";")
                connection.execute(query)
                query = db.text("select * from " + table + ";")
                result = connection.execute(query)
                x = result.fetchall()
                print(x)
            elif func.__eq__("delete"):
                table = input("which table? ")
                where = input("where? ")
                query = db.text("delete from " + table + " where " + where + ";")
                connection.execute(query)
                query = db.text("select * from " + table + ";")
                result = connection.execute(query)
                x = result.fetchall()
                print(x)
    except:
        print("wrong username or password")