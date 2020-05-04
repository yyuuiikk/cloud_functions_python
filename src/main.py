from flask import Flask, request
import json
import os
import requests
import yaml

# 環境変数の読み込み
try:
    # local
    with open('./env.yml') as f:
        os.environ.update(yaml.load(f))
except FileNotFoundError as e:
    # Google Cloud Functions
    pass

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
    
'''
slackにメッセージを通知
'''
def post_slack(request):
    message = 'first post'
    requests.post(url=WEBHOOK_URL, data=json.dumps({
        'text': message
    }))
    return 'True'

'''
ローカル環境で実行
'''
if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/')
    def index():
        # 作成した関数名を指定
        return post_slack(request)

    app.run('127.0.0.1', 8000, debug=True)
