# pythonのバージョン
FROM python:3.7

# ログなどの出力をバッファに貯めこまない設定
ENV PYTHONUNBUFFERED 1
# タイムゾーンの指定
ENV TZ JST-9

# apt-getパッケージのインストール
RUN apt-get update && apt-get install -y \
    curl \
    vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# dockerに接続した時のディレクトリ指定
WORKDIR /usr/src/

# pythonの必要モジュールのインストール
ADD requirements.txt /usr/src/
RUN pip3 install -r requirements.txt