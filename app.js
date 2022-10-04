import express from "express"
import WebSocket, { WebSocketServer } from "ws"
import { createServer } from "node:http"
import { EventEmitter } from "node:events"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"

import hid from "./hid.js"
import initDB, { Activity } from "./db.js"

const { DB_FILE, HID_FILE } = process.env
if(!DB_FILE || !HID_FILE) {
  console.error("$DB_FILE and $HID_FILE must be set!")
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

  const send = msg => {
    const data = JSON.stringify(msg)
    wss.clients.forEach(client => {
      if(client.readyState === WebSocket.OPEN) {
        client.send(data)
      }
    })
  }

  hid(HID_FILE).on("submit", async code => {
    const validator = /\d{6}/
    if(!validator.test(code)) {
      send({ code, msg: "invalid" })
      return
    }

    const row = await Activity.findOne({
      where: { code },
      order: [["date", "ASC"]],
    })
    if(row && row.event === "used") {
      send({ code, msg: "used" })
      return
    }

    await Activity.create({ code, event: "used" })
    send({ code, msg: "accept" })
  })

  server.listen(3000)
}
main()
