import os
import configparser
from slack_sdk import WebClient

# config/config.iniの読み出し
config_ini = configparser.ConfigParser()
config_ini.optionxform = str
config_ini.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),'config/config.ini'), encoding='utf-8')

SLACK_BOT_TOKEN = config_ini['slack']['SLACK_BOT_TOKEN']
SLACK_BOT_CH = config_ini['slack']['SLACK_BOT_CH']

# Web API クライアントを初期化します
client = WebClient(SLACK_BOT_TOKEN)

# chat.postMessage API を呼び出します
response = client.chat_postMessage(
    channel=SLACK_BOT_CH,
    text=":wave: こんにちは！",
)