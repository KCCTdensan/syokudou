# ラズパイで実行

## ラズパイのセットアップ

GUIでやる。

まずはイメージをDLする(例: [確認済みのイメージ](
https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2022-09-26/2022-09-22-raspios-bullseye-arm64.img.xz
))。

ファイル形式に依って適宜解凍する。
Windowsだと[7-Zip](https://www.7-zip.org)が便利。

Linuxでの例:
```
% unxz hoge.img.xz
```

そしてSDカードにイメージを焼く。
このとき，最初からSDカードに入っていたデータは全て消える。
コマンド操作が不安な人は[Etcher](https://www.balena.io/etcher/)を使うといい。

焼き終わったらラズパイに刺して配線を済ませる。

## ラズパイのセットアップ : OS編

セットアップ時はラズパイをネットに繋げておく(wifiでも可)。

最近のRaspberry Pi OSは初回起動時にウィザード的なやつがあるので，適宜設定する。

起動したら，自動ログインを設定しておく。
なんか手元の環境だとウィザードを終えた時点で最初から自動ログインになっていた。

そして必要なパッケージを入れる。

```
% sudo apt update
% sudo apt install -y git chromium nodejs npm
% sudo npm i -g n
% sudo n lts
```

このリポジトリをセットアップする。

```
% git clone https://github.com/KCCTdensan/syokudou ~/syokudou
% cd ~/syokudou
% npm i
```

カードリーダーを探す。
`/dev/hidrawX`みたいなやつが欲しい。
いつものやつはUnitechうんたら製。

```
% node devices
```

見つかったら設定ファイルを編集する。

```
% mousepad app.env
```

そして自動で起動するようにする。

```
% echo "~/syokudou/run.sh &" >> ~/.xprofile
```
