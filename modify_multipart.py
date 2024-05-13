# 江苏图采照片上传工具
# 小程序源码解析 + 此程序使用教程：
# https://blog.csdn.net/qq_27683537/article/details/138774682

# 端口: 6689

import flask
from flask import request
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

app = flask.Flask(__name__)


@app.route('/v2/camera/upload', methods=['POST'])
def modify():

    # 获取请求参数
    file_type = request.form.get('type')
    code = request.form.get('code')
    token = request.headers.get('Authorization')
    user_agent = request.headers.get('User-Agent')
    content_type = request.headers.get('Content-Type')
    boundary = request.headers.get('Content-Type').split(';')[1].split('=')[1]
    referer = request.headers.get('Referer')

   
    modify_headers = {
        'Authorization': token,
        'User-Agent': user_agent,
        'Content-Type': content_type,
        'Referer': referer,
        'Host': 'jstxcj.91job.org.cn',
        'Accept': 'application/json, text/javascript, */*;',
    }

    modify_form = {
        'type': file_type,
        'code': code,
        'file': ('tmp.jpg', open('/your/path/to/img.jpg', 'rb'), 'image/jpeg'),
    }

    encoder_multipart = MultipartEncoder(fields=modify_form, boundary=boundary)


    try:
        res = requests.post('https://jstxcj.91job.org.cn/v2/camera/upload', 
                            data=encoder_multipart, 
                            headers=modify_headers,
                            )

        print(res.text)
    
    except Exception as e:
        print(f"出现错误: {str(e)}")
    
    return res.content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6689, debug=True)
