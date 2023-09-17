# 获取短信验证码
from utils.mysql_util import db
from utils.log_util import logger


def get_code(mobile):
    sql = "select code FROM users_verifycode WHERE mobile = '%s' ORDER BY add_time DESC LIMIT 1" % mobile
    result = db.select_db_one(sql)
    logger.info("sql执行结果,得到验证码为：{}".format({result['code']}))
    return result['code']
