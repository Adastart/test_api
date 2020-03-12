#coding=utf-8
import pymysql

class DB():
    def __init__(self):
        self.conn=pymysql.connect(host='47.103.128.20',
                                   port=30306,
                                   user='p2p',
                                   passwd='p2p_2019',
                                   db='p2p_test',#库名
                                   charset='utf8'
        )



        self.cur=self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()


    def find_sql(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update_sql(self,sql):
        try:
            self.cur.execute(sql)
            self.cur.commit()
        except Exception as e:
            self.cur.rollback()
            print(str(e))

    def check_userId(self,userId):
        self.cur.execute("SELECT * FROM cap_capital_account WHERE user_id='{}'".format(userId))
        return self.cur.fetchall()


db=DB()
user=db.check_userId(85174)
print(user)


