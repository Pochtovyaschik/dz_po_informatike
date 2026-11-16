import pymysql

class Database:
    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(host=host, user=user, password=password, db=database, cursorclass=pymysql.cursors.DictCursor)

    def search(self):
        sql = "SELECT * FROM table_1"
        with self.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()

    def registration(self, username, password):
        sql = f"INSERT INTO table_1 (Namel, password) VALUES ({username}, {password}])"
        with self.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()





connect = pymysql.connect(
    host='localhost',
    user='root',
    password='admin',
    db='database_FLASK',
    )

n = Database.search(connect)

