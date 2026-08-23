# なぜこれを作ったか

安いTuya / Smart Life / iSmartLifeカメラは買いやすい。持ち主になるのは面倒だ。

箱は普通のIPカメラに見える。中身はメーカー雲に鍵がかかっている。

- 純正に **ONVIFはない**
- FrigateやAgent DVRに貼れる **カメラ本体のRTSPもない**
- 公式アプリはアカウントとスマホと、自分では握れないサーバを要求する
- 二台目や「クラウドNVR」は課金か、唯一のライブを奪うか

壁のセンサーは自分で払った。録画は自分のディスクへ。

**Tuya RTSP ブリッジ** は小さなローカルプログラムだ。いつものアプリでQRを一度読む。そのあと各カメラは普通のURLになる。

```
rtsp://<このPC>:8554/<カメラ名>/hd
```

合図（ログイン）はTuyaのまま。このPCから見るとき、映像はだいたいカメラ→この機械のLANに留まる。安いハードウェア、自宅アーカイブ。それが目的。

## これは何ではないか

- ファームウェア改造でもジェイルブレイクでもONVIFでもない
- 60fpsの約束ではない。多くの機種はHD HEVCで **約10fps**。カメラ側の話
- スマホアプリを殺すものでもない。NVR用の *ローカル* 経路だ
- Tuya Inc.とは無関係。エンジンは [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)（MIT）

次: [getting-started.md](getting-started.md) · [FAQ](faq.md)
