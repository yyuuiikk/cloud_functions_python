# Cloud Functions Python実行環境

ローカル環境でCloud Functionsを実行するための環境。

HTTPトリガーにのみ対応。

# サンプルプログラム

slackの任意のチャンネルにメッセージを投稿する処理を実装。

```
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
```

`src`フォルダ内に`env.yml`を別途作成し、投稿するslackチャンネルのWebhookURLを定義する。

```
$ touch src/env.yml
```

```
WEBHOOK_URL: https://xxxxxxxxxxxxxxxxxxx
```

# コンテナの作成と起動

```
$ docker-compose up -d
```

## ローカル環境でのプログラム実行

コンテナ環境にログインしてpythonプログラムを実行する。

```
$ docker exec -it function_python bash

# python src/main.py 
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
 * Restarting with inotify reloader
 * Debugger is active!
 * Debugger PIN: 111-11-111
```

webサーバが起動するので、ターミナルの別ウインドウを開き再度コンテナ環境にログインしてcurlを実行する。

```
$ docker exec -it function_python bash

# curl http://127.0.0.1:8000/
True
```

実行後指定したSlackチャンネルにメッセージが投稿される。

## デプロイ

GCPプロジェクトには下記のコマンドでデプロイする。

```
$ gcloud functions deploy post_slack --runtime=python37 --trigger-http --allow-unauthenticated --source=. --region=asia-northeast1 --env-vars-file=env.yml
```
