# Tuya RTSP ブリッジ

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Tuya / Smart Life / iSmartLife の安カメラを、普通のRTSPカメラにする。** Frigate、Agent DVR、go2rtc、Home Assistant、VLC向け。

ファームウェアはいじらない。ONVIFもない（純正には最初からない）。QRを一度読めば、あとはURLをコピーするだけ。

| 立場 | ここから |
|---|---|
| とりあえず動かしたい | [5分で入れる](#5分で入れる) |
| 自宅NVR | [docs/nvr.md](docs/nvr.md) |
| 開発 | [docs/architecture.md](docs/architecture.md) |

このリポジトリにアカウントも機器IDも自宅IPも入っていない。

## なぜ安カメラにこれが要るのか

2〜4千円の「Smart Life」カメラはIPカメラに見える。中身は違う。純正は **ONVIFなし**、**RTSPのチェックもない**。映像はメーカーアプリと、自分では握れない雲経由。二台目のスマホや「クラウドNVR」は課金か、唯一のライブを奪うかのどっちかが多い。

壁に付けたセンサーは自分が払ったものだ。録画は自分のディスクへ。

このプログラムは小さなローカル橋。いつものアプリでQRを読む。そのあと各カメラは普通のURLになる。

```
rtsp://<このPC>:8554/<カメラ名>/hd
```

ログインの合図はTuyaのまま。このPCから見るとき、映像はだいたいLANに留まる。長い話は [docs/ja/why.md](docs/ja/why.md)。

## 正直な限界

- ONVIFも、カメラ本体のRTSPもない
- HDはだいたい **10fps**。アプリが間引いているわけではない
- VLC 3はHEVC/RTSPで真っ黒になりがち。見るならAgent DVRかFrigate
- 録画はNVR側。橋に残さない

対応ログイン地域: 西欧、東欧、米国西/東、中国、インド。

## 5分で入れる

1. Windows 10/11と、もうカメラが見えているSmart Lifeアカウント。PythonもVLCもffmpegも別途いらない。
2. [Releases](../../releases) の `TuyaRtspBridge-Setup.exe`。次へ、次へ、完了。詳細は [docs/windows.md](docs/windows.md)。
3. アプリ起動 → スマホと同じ地域（日本のアカウントでもEU/USなど実クラスタを選ぶ）→ QR作成 → アプリで読んで **確認**
4. HDのURLをAgent DVR / Frigateへ: `rtsp://127.0.0.1:8554/<名前>/hd`

カメラ一覧が空なら、だいたい地域違い。QRが終わらないのは、まだ確認していないだけ。待つ。

データ: `%APPDATA%\TuyaRtspBridge\`。プログラム: `%LOCALAPPDATA%\Programs\TuyaRtspBridge`。

## ライセンス

こちらのコードはMIT。エンジンはMIT、Copyright (c) 2025 seydx。Tuya Inc.とは無関係。

名称・手元のデータ・同梱ライセンスは [docs/legal.md](docs/legal.md)。
