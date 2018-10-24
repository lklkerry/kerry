import json
import requests

URL='https://api.github.com'

# URL='https://www.baidu.com'

def build_url(endpoint):
    return '/'.join([URL,endpoint]) #主要作用拼接接口请求

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4) #采用json里面提供的方法1打印出来，格式更好看


def request_method():
    response=requests.get(build_url('users/lklkerry'))
    print(better_output(response.text))

if __name__=='__main__':
    request_method()