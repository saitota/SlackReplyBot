import json
import logging
import urllib.request
import os

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def event_to_json(event):
    if 'body' in event:
        body = json.loads(event.get('body'))
        return body
    elif 'token' in event:
        body = event
        return body
    else:
        logger.error('unexpected event format')
        exit


class ChallangeJson(object):
    def data(self, key):
        return {
            'isBase64Encoded': 'true',
            'statusCode': 200,
            'headers': {},
            'body': key
        }


class PostJson(object):
    def __init__(self):
        self.BOT_TOKEN = os.environ['BOT_TOKEN']
        self.OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
        self.REPLY_WORD = os.environ['REPLY_WORD']
        self.BOT_NAME = os.environ['BOT_NAME']
        self.BOT_ICON = os.environ['BOT_ICON']

    def headers(self):
        return {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': 'Bearer {0}'.format(self.BOT_TOKEN)
        }

    def data(self, channel):
        return {
            'token': self.OAUTH_TOKEN,
            'channel': channel,
            'text': self.REPLY_WORD,
            'username': self.BOT_NAME,
            'icon_emoji': self.BOT_ICON
        }


def handler(event, context):
    HOOK_KEYWORD = os.environ['HOOK_KEYWORD']

    # Output the received event to the log
    # logging.info(json.dumps(event))
    body = event_to_json(event)

    # return if it was challange-event
    if 'challenge' in body:
        challenge_key = body.get('challenge')
        logging.info('return challenge key %s:', challenge_key)
        return ChallangeJson().data(challenge_key)

    # Hook specific word
    if HOOK_KEYWORD in body.get('event').get(
            'text', '') and body.get('event').get('subtype', '') == '':
        logger.info('hit: %s', HOOK_KEYWORD)
        post_head = PostJson().headers()
        post_data = PostJson().data(body.get('event').get('channel'))
        # POST
        url = 'https://slack.com/api/chat.postMessage'
        req = urllib.request.Request(
            url,
            data=json.dumps(post_data).encode('utf-8'),
            method='POST',
            headers=post_head)
        res = urllib.request.urlopen(req)
        logger.info('post result: %s', res.msg)

    return {'statusCode': 200, 'body': 'ok'}
