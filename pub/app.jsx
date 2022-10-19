const { useEffect, useRef, useState } = React

const sleep = async ms => new Promise(res => setTimeout(res, ms))

const timeDiffFmt = (dt, now) => {
  const ds = (now - dt) / 1000
  if(ds < 0) return "未来"

  const h = Math.trunc(ds / 3600)
  if(h) return `${h}時間前`

  const m = Math.trunc(ds / 60)
  if(m) return `${m}分前`

  const s = Math.trunc(ds)
  if(s) return `さっき(${s}秒前)`
}

const App = () => {
  const [code, setCode] = useState("-")
  const [msg, setMsg] = useState("")
  const [dt, setDt] = useState(0)
  const [now, setNow] = useState(0)
  const userInput = useRef(null)

  const [clearRq, setClearRq] = useState(0)
  const clearRqRef = useRef()
  clearRqRef.current = clearRq

  const dispDur = 5000
  const clear = () => {
    // there are another requests
    if(Date.now() - clearRqRef.current < dispDur) return
    setCode("-")
    setMsg("")
  }

  const msgColor = msg => {
    switch (msg) {
      case "accept":  return "lime"
      case "used":    return "lightgray"
      case "invalid": return "red"
      default:        return "unset"
    }
  }

  const msgText = msg => {
    switch (msg) {
      case "accept":  return "正常に受け付けました"
      case "used":    return "既に使用済みです"
      case "invalid": return "無効なコードです"
    }
  }

  const onSubmit = e => {
    const data = e.target.value
    if(!data) return
    ws.send(data)
    e.target.value = ""
    console.log("submitted", data)
  }

  useEffect(() => {
    async function handler({ data }) {
      const { code, msg, dt, now } = JSON.parse(data)
      setCode(code)
      setMsg(msg)
      setDt(dt || 0)
      setNow(now)
      setClearRq(Date.now())
      await sleep(dispDur)
      clear(Date.now())
    }

    function connect() {
      const url = new URL("/ws", location.href)
      url.protocol = "ws"

      window.ws = new WebSocket(url)
      ws.onmessage = handler
      ws.onclose = async e => {
        console.warn("socket closed", e)
        await sleep(1000)
        connect()
      }
    }

    userInput.current.focus()
    connect()
  }, [])

  return (
    <>
      <div
        style={{
          width: "100vw",
          height: "100vh",
          position: "absolute",
          top: "0",
          left: "0",
          backgroundColor: msgColor(msg),
          zIndex: "-1",
        }}
      />
      <header>
        <h1>食堂管理システム</h1>
        <a href="/stats/">統計情報</a>
      </header>
      <main>
        <input
          style={{
            width: "100%",
            fontSize: "2rem",
            fontWeight: "bold",
            textAlign: "center",
          }}
          placeholder="コードを入力……"
          onKeyPress={e => e.key === "Enter" && onSubmit(e)}
          ref={userInput}
        />
        <div
          style={{
            fontSize: "8rem",
            fontWeight: "900",
            textAlign: "center",
          }}>
          {code}
        </div>
        <div
          style={{
            fontSize: "4rem",
            fontWeight: "bold",
            textAlign: "center",
          }}>
          {msgText(msg)}
        </div>
        {msg === "used" && (
          <div
            style={{
              marginTop: "2rem",
              fontSize: "3rem",
              textAlign: "center",
            }}>
            最終利用時刻 : {timeDiffFmt(dt, now)}
          </div>
        )}
      </main>
      <footer>
        <p
          style={{
            marginTop: "4rem",
            color: "gray",
            fontSize: "1.2em",
            fontWeight: "bolder",
            textAlign: "center",
          }}>
          https://github.com/KCCTdensan/syokudou
          <br />
          &copy; 2022 神戸高専電算部
        </p>
      </footer>
    </>
  )
}

ReactDOM.render(<App />, document.getElementById("root"))
