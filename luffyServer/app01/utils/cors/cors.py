

def cors(response):
    """
    为解决请求跨站问题
    :param response: server端向client端返回的json数据
    :return: 添加响应头
    """
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    response['Access-Control-Allow-Origin'] = '*'
    response["Access-Control-Max-Age"] = '100000'
    response['Access-Control-Allow-Headers'] = "*"

    return response