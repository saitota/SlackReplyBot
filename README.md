# Slack Serverless Reply Bot
Receive the message on Slack public channel, and reply when a specific keyword is included.

***DEMO:***


## Description
- Using Lambda to Post message
- Using API Gateway to subscribe message
- Using Slack BOT & Subscribe

## Requirement
- AWS Account
- Serverless Framework
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
$ git clone https://github.com/saitota9/SlackServerlessReplyBot
```

4. Modify sererless.yml 's two TOKEN to your token.
``` sererless.yml
OAUTH_TOKEN: 'xoxp-000000000000-000000000000-000000000000-0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x'
BOT_TOKEN: 'xoxb-000000000000-0x0x0x0x0x0x0x'
```

5. Deploy with Serverless Framework (you must aws-cli initialize before)
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
6. Set Slack BOT endpoint and event subscribe settings 
    - Event Subscriptions
        - Request URL: `set your endopint url(you can see in your deploy log)`
    - Subscribe to Workspace Events
        - message.channels

7. Done! try to say `poop` at Slack.

## Anything Else
I wrote article about this BOT.
[Slack で自動返信するサーバレスBOTを作りました - Qiita](https://qiita.com/saitotak/items/822bf2dce7e3baa25ae0)

## Author
[saitotak](https://qiita.com/saitotak)

## License
[MIT](http://b4b4r07.mit-license.org)
