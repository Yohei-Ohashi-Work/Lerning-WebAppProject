# Study Web App

## 概要
このプロジェクトは、学習用のWebアプリケーションです。Flaskを使用して構築されており、基本的なWebアプリケーションの開発手法を学ぶことができます。

## 必要要件
- Python 3.11以上
- Flask 3.1.0以上
- Docker（オプション：コンテナ化された環境で実行する場合）

## セットアップ方法

### 通常のセットアップ
1. Pythonの環境を準備
   ```bash
   # Python 3.11以上がインストールされていることを確認
   python --version
   ```

2. 依存関係のインストール
   ```bash
   # Poetryを使用して依存関係をインストール
   poetry install
   ```

### Dockerを使用する場合
1. DockerとDocker Composeがインストールされていることを確認
2. 以下のコマンドでコンテナを起動
   ```bash
   docker-compose up
   ```

## プロジェクト構造
```
web-app-template/
├── flasker/          # Flaskアプリケーションのメインコード
├── docker/           # Docker関連の設定ファイル
├── docker-compose.yml # Docker Composeの設定
├── pyproject.toml    # プロジェクトの依存関係設定
└── poetry.lock       # 依存関係のバージョンロック
```

## 開発者向け情報
- このプロジェクトは学習目的で作成されています
- コードの変更や機能追加は自由に行って構いません
- 問題や改善点を見つけた場合は、積極的に報告してください

## ライセンス
このプロジェクトは学習目的で作成されています。 