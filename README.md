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

## ngrokの環境設定
1. [ngrokのダウンロードページ](https://ngrok.com/download)にアクセスしDL
2. ダウンロードしたものを解凍する
3. 解凍して出てきたファイルのあるディレクトリにターミナルで移動
4. `$ printenv PATH`で`/usr/local/bin`にPATHが通っていることを確認
5. `$ mv ngrok /usr/local/bin/`
6. `$ ngrok -v`でバージョンが出ればおk

## テスト環境の立て方
1. mian.pyを動かす → `Bolt is running!`的なのが出てればおk
2. ngrokを動かす
    1. ngrok環境があることを確認する
    2. `$ ngrok http 3000`
    3. `Forwarding      https://a10dc1f0b796.ngrok.io -> http://localhost:`みたいなとこのhttpsリンクをコピー
3. [Slack app の設定画面](https://api.slack.com/apps/A0252JRUBU2/general?)を開く
4. Event Subscriptionsに飛び，トグルをオンにする
5. URLフォームに`コピーしたURL/slack/events`と入力 → 失敗してたら再起動とかしてみる
6. 何か設定を変えるならここで変える
7. 変えた場合はOAuth & PermissionsからReinstall in Workspaceでリインストールする
8. Slack上とlogで動作確認開始！
