# syokudou

ラズパイ(linux)での運用を想定しています。

※完全セットアップガイドはこちら→[RPI.md](RPI.md)

## セットアップ(わかってる人向け)

```
% npm i
% export DB_FILE=hoge.db
% export HID_FILE=/dev/hidraw0
```

## 実行(わかってる人向け)

`HID_FILE`を読む権限が必要。

```
% sudo node app
```
