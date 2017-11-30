import hashlib
import time

def gen_token(user):
    """
    生成token
    :param user: 根据传来的用户名和当前时间进行md5hash
    :return:
    """
    ctime = str(time.time())
    md = hashlib.md5(user.encode("utf-8"))
    md.update(ctime.encode("utf-8"))
    return md.hexdigest()


