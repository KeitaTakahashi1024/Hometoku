# Hometoku
Slack app Hometokuの開発

## 利用パッケージの共有方法
### 準備
1. `$ git pull origin main`
2. `$ python3 -m venv .venv`
3. `$ source .venv/bin/active`

### パッケージのインストールした時
1. `(.venv)$ pip install xxx(インストールするパッケージ)`
2. `(.venv)$ pip freeze > requirements.txt`
3. `(.venv)$ git add .`からいつものpushまで

### 他の人のものを引っ張ってくる時
1. `(.venv)$ git pull`
2. `(.venv)$ pip install -r requirements.txt`

## Tokenの管理
1. Slackの「たいせつなもの」チャンネルでTokenを確認．以下のコマンドを置き換えて打ち込む．
2. `export SLACK_BOT_TOKEN=xoxb-your-token`
3. `export SLACK_SIGNING_SECRET=your-signing-secret`