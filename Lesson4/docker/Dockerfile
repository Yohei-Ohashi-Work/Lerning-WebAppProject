# PythonのDockerイメージをダウンロード
# 現行の安定バージョン
FROM python:3.11-slim

# Pythonの出力表示をDocker用に設定
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリを設定
WORKDIR /Lesson4
# pipを使ってpoetryをインストール
RUN pip install poetry
# Poetry が仮想環境を作らず、コンテナ上のグローバル環境に直接パッケージをインストールする
RUN poetry config virtualenvs.create false

# poetryの設定ファイルが存在するなら、コピーしてパッケージをインストール
COPY pyproject.toml* poetry.lock* ./
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi