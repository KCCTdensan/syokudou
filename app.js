import express from "express"
import WebSocket, { WebSocketServer } from "ws"
import { createServer } from "node:http"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"

import hid from "./hid.js"
import initDB, { Activity } from "./db.js"

const { DB_FILE, HID_FILE } = process.env
if(!DB_FILE || !HID_FILE) {
  console.error("$DB_FILE and $HID_FILE must be set!")
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

  hid(HID_FILE).on("submit", async code => {
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
      const dt = row.date.getTime()
      if(Date.now() - dt < 3000) {
        // 3秒以内の再スキャンは認める
        send({ code, msg: "accept" })
      } else {
        send({ code, msg: "used", dt })
      }
      return
    }

    await Activity.create({ code, event: "used" })
    send({ code, msg: "accept" })
  })

  server.listen(process.env.PORT || 3000)
}
main()
