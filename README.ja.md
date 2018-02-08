# 🤖 Slack Serverless Reply Bot
Slack のパブリックチャンネルのメッセージから、特定のキーワードが含まれるときに定型文を自動返信するサーバレス BOT です。

***DEMO:***

![demo](https://user-images.githubusercontent.com/1152469/35902255-db0707e4-0c1d-11e8-882e-ca90d1e7a933.gif)

## Description
Slack の BOT と Subscribe を使うことで、全ての Public Message を API-Gateway 経由で Lambda に受信します。
特定のキーワードがある場合は Slack API を呼び出して、同一チャンネルに固定メッセージを返信します。
Slack BOT は手動で設定する必要がありますが、AWS 側は Serverless Framework を使うことで環境構築を自動化しています。

## Requirement
- AWS アカウント
- Serverless Framework
- Slack アカウント

## Installation
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
...
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

# 🤔 Anything Else
この BOT に関する記事を書きました。

[Slack で自動返信するサーバレスBOTを作りました - Qiita](https://qiita.com/saitotak/items/822bf2dce7e3baa25ae0)

# 🐑 Author
[saitotak](https://qiita.com/saitotak)

# ✍ License
[MIT](./LICENSE)

