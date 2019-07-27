import pymysql

class Database:
    def __init__(self):
        host = "localhost"
        user = "crimen"
        password = "crimen2019clave"
        db = "crimen"
        self.con = pymysql.connect(
            charset="utf8",
            host=host, 
            user=user, 
            password=password, 
            db=db, 
            cursorclass=pymysql.cursors.
            DictCursor
        )
        self.cur = self.con.cursor()

    def getResult(self, sql, columna):
        query = self.cur
        query.execute(sql)
        result = query.fetchall()
        resource = []
        for data in result:
            resource.append(data[''+columna])
        # query.close()
        return resource

    def getResource(self, sql):
        query = self.cur
        query.execute(sql)
        result = query.fetchall()
        resource = []
        for data in result:
            resource.append(data)
        return resource        