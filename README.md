# syokudou

ラズパイ(linux)での運用を想定しています。

## セットアップ

```
% npm i
% export DB_FILE=hoge.db
% export HID_FILE=/dev/hidraw0
```

## 実行

`HID_FILE`を読む権限が必要。

```
% sudo node app
```
