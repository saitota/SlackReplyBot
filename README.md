# 🤖 Slack Reply Bot
It is a serverless BOT which receives Slack's public channel message and reply if there includes a specific keyword.

***DEMO:***

![demo](https://user-images.githubusercontent.com/1152469/35902255-db0707e4-0c1d-11e8-882e-ca90d1e7a933.gif)

## Description
Using Slack's BOT and Subscribe to receive all the public messages toward Lambda via API-Gateway.
If there includes a specific keyword, call the Slack API and send a message back to the same channel.
Slack BOT needs to be create manually, but AWS side automates environment construction by using Serverless Framework.

## Requirement
- AWS Account
- Serverless Framework
- [serverless-plugin-aws-alerts](https://serverless.com/blog/serverless-ops-metrics/) (optional)
- Slack Account

## Installation
1. Create Slack BOT from [Here](https://api.slack.com/slack-apps)
    - Bot User
        - Display Name
        - Default Username
    - Permissions
        - OAuth & Permissions
            - Scopes
                - channels:history
                - channels:write
2. Get two tokens
    - Permissions
        - OAuth & Permissions
            - OAuth Access Token
            - Bot User OAuth Access Token

3. Clone this repo.
```
$ git clone https://github.com/saitota/SlackReplyBot.git
```

4. Modify environment_dev.yml 's two TOKENs to your token.
``` environment_dev.yml
OAUTH_TOKEN: 'xoxp-000000000000-000000000000-000000000000-0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x'
BOT_TOKEN: 'xoxb-000000000000-0x0x0x0x0x0x0x'
```

5. Deploy with Serverless Framework (you must aws-cli initialize before)
```
$ sls deploy
...
api keys:
  None
endpoints:
  POST - https://0x0x0x0x0x.execute-api.ap-northeast-1.amazonaws.com/dev/
functions:
  fnc: SlackReplyBot-dev-fnc
```
6. Set Slack BOT endpoint and event subscribe settings 
    - Event Subscriptions
        - Request URL: `set your endopint url(you can see in your deploy log)`
    - Subscribe to Workspace Events
        - message.channels

7. Done! try to say `poop` at Slack.

# 🤔 Anything Else
I wrote article about this BOT.

[Slack で自動返信するサーバレスBOTを作りました - Qiita](https://qiita.com/saitotak/items/822bf2dce7e3baa25ae0)

# 🐑 Author
[saitotak](https://qiita.com/saitotak)

# ✍ License
[MIT](./LICENSE)
