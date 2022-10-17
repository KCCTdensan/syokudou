#!/bin/bash
set -ex

cd `dirname $0`

(
  sleep 3
  chromium --kiosk --app=http://localhost:3000 &
) &

. app.env
export DB_FILE HID_FILES

DB_BACK=$BACK_DIR/latest.db
if [ -e $DB_BACK ]; then
  sudo cp $DB_BACK $DB_FILE
  sudo chown root $DB_FILE
else
  sudo touch $DB_FILE
fi

exec sudo -E node app
