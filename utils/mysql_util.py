import pymysql

from utils.log_util import logger
from utils.read_path import FileRead

# 获取数据库相关连接信息
data = FileRead.read_ini()['mysql']
# print(data['MYSQL_HOST'])
# print(int(data['MYSQL_PORT']))
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "passwd": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB']
}
# print(DB_CONF)


class MysqlDb:
    def __init__(self):
        # 连接mysql
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 查询
    # @staticmethod
    def select_db_one(self, sql):
        logger.info("执行sql：{}".format(sql))
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info("执行sql结果：{}".format(result))
        return result

    # 查询多条
    def select_db_all(self,sql):
        logger.info("执行sql：{}".format(sql))
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info("执行sql结果：{}".format(result))
        return result

    # 更新
    # @staticmethod
    def execute_db(self, sql):
        try:
            logger.info("执行sql:{}".format(sql))
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


db = MysqlDb()
if __name__ == '__main__':

    result = db.select_db_one(
        "select code FROM users_verifycode WHERE mobile = '15234565431' ORDER BY add_time DESC LIMIT 1"
    )
    print(result['code'])
