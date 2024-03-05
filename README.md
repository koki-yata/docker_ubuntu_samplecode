# docker_ubuntu_samplecode
ubuntu 20.04にてdocker環境構築時のサンプルコード

## slackトークンの発行とチャンネルIDの取得・アプリのインストール

### ▼下記記事に記載のあるトークンを取得してください。  
xoxb- ではじまるSLACK_BOT_TOKEN  
参考記事：https://qiita.com/seratch/items/1a460c08c3e245b56441

### ▼通知したいチャンネルIDを取得してください  
参考画像：  
![スクリーンショット 2022-06-24 12 39 08](https://git.dmm.com/storage/user/1436/files/78ad8d0e-edfe-47bc-8bbe-0355b54f4ad3)

### ▼アプリをインストール
作成したアプリをメッセージを検知したいslackチャンネルにインストールしてください。  
参考画像：  
![スクリーンショット 2022-06-24 13 11 18](https://git.dmm.com/storage/user/1436/files/86aea77e-ac2b-4143-a414-4b1c331d920c)

### ▼設定ファイルの編集 
* コンフィグのフォルダとディレクトリを作成してください。
```
cd docker_ubuntu_samplecode/plugins
mkdir config
touch config/config.ini
```  
参考画像：  
![スクリーンショット 2022-08-02 13 08 28](https://git.dmm.com/storage/user/1436/files/4d9b53c4-9295-4465-aa20-af3ef8e75616)


* 作成したconfig.iniファイルに設定値を入れる

```
[slack]
SLACK_BOT_TOKEN = xoxb-ではじまるSLACK_BOT_TOKEN 
SLACK_BOT_CH = 通知したいチャンネルID
```

### ▼起動時コマンド  
```
$ cd docker_ubuntu_samplecode
$ docker-compose up -d
```
