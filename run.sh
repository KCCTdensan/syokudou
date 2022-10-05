#!/bin/bash
set -ex

cd `dirname $0`

(
  sleep 3
  chromium --kiosk --app=http://localhost:3000 &
) &

. app.env
export DB_FILE HID_FILE

node app
