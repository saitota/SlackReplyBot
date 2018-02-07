# Slack Serverless Reply Bot
スラックのPublic Channel のメッセージを受信し、特定のキーワードがあると返信するサーバレスBOTです。

***DEMO:***


## 詳細
- Lambda をメッセージ送信に使っています
- Subscribe に API Gateway を使っています
- Slack BOT を使っています

## 必要なもの
- AWS アカウント
- Serverless Framework
- Slack アカウント

## インストール
1. [ここ](https://api.slack.com/slack-apps) からBOT作成
    - Bot User
        - Display Name
        - Default Username
    - Permissions
        - OAuth & Permissions
            - Scopes
                - channels:history
                - channels:write
2. トークンを２つ取得
    - Permissions
        - OAuth & Permissions
            - OAuth Access Token
            - Bot User OAuth Access Token

3. リポジトリをClone
```
$ git clone https://github.com/saitota/SlackServerlessReplyBot.git
```

4. Serverless の設定ファイルを編集、先程のトークンで書き換えてください
``` sererless.yml
OAUTH_TOKEN: 'xoxp-000000000000-000000000000-000000000000-0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x'
BOT_TOKEN: 'xoxb-000000000000-0x0x0x0x0x0x0x'
```

5. Serverless Framework でデプロイ (事前にaws-cliの初期設定が必要です)
```
$ sls deploy ./SlackServerlessReplyBot
(略)
api keys:
  None
endpoints:
  POST - https://0x0x0x0x0x.execute-api.ap-northeast-1.amazonaws.com/prod/
functions:
  fnc: SlackServerlessReplyBot-prod-fnc
```
6. Slack BOT のエンドポイント設定と、Subscribe設定をします
    - Event Subscriptions
        - Request URL: `set your endopint url(you can see in your deploy log)`
    - Subscribe to Workspace Events
        - message.channels

7. 設定完了！Slackで `poop` と発言してみましょう

## Anything Else
I wrote article about this BOT.
[Slack で自動返信するサーバレスBOTを作りました - Qiita](https://qiita.com/saitotak/items/822bf2dce7e3baa25ae0)

## Author
[saitotak](https://qiita.com/saitotak)

## License
[MIT](http://b4b4r07.mit-license.org)
