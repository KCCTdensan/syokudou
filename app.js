import express from "express"
import WebSocket, { WebSocketServer } from "ws"
import { createServer } from "node:http"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"

import hid, { hidev } from "./hid.js"
import initDB, { Activity } from "./db.js"

const unixDate = ms => Math.trunc(ms / 1000 / 3600 / 24)

const { DB_FILE, HID_FILES } = process.env
if(!DB_FILE || !HID_FILES) {
  console.error("$DB_FILE and $HID_FILES must be set!")
  console.error("README.md読んで!")
  process.exit(1)
}

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

async function main() {
  await initDB(DB_FILE)

  const app = express()
  const server = createServer(app)
  const wss = new WebSocketServer({ server })

  app.use(express.static(join(__dirname, "pub")))

  app.get("/api/dump", async (req, res) => {
    const rows = await Activity.findAll({
      attributes: ["code", "event", "date"],
    })
    const data = rows.map(({ code, event, date }) => ({
      code, event,
      date: date.getTime(),
    }))
    res.json(data)
  })

  const send = body => {
    const data = JSON.stringify({
      ...body,
      now: Date.now(),
    })
    wss.clients.forEach(client => {
      if(client.readyState === WebSocket.OPEN) {
        client.send(data)
      }
    })
  }

  HID_FILES.split(",").forEach(hid)
  hidev.on("submit", async code => {
    const validator = /^\d{6}$/
    if(!validator.test(code)) {
      send({ code, msg: "invalid" })
      return
    }

    const row = await Activity.findOne({
      where: { code },
      order: [["date", "ASC"]],
    })
    if(row && row.event === "used") {
      const now = Date.now()
      const dt = row.date.getTime()

      // 日付跨いでたら認める
      if(unixDate(now) !== unixDate(dt)) {
        await Activity.create({ code, event: "used" })
        send({ code, msg: "accept" })
        return
      }

      // 3秒以内の再スキャンは認める
      if(now - dt < 3000) send({ code, msg: "accept" })
      else                send({ code, msg: "used", dt })
      return
    }

    await Activity.create({ code, event: "used" })
    send({ code, msg: "accept" })
  })

  server.listen(process.env.PORT || 3000)
}
main()
