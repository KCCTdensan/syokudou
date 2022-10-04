const { useEffect, useRef, useState } = React

const sleep = async ms => new Promise(res => setTimeout(res, ms))

const App = () => {
  const [code, setCode] = useState("-")
  const [msg, setMsg] = useState("")

  const clear = () => {
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
      case "used":    return "既に使用済みのカードです"
      case "invalid": return "無効なカードです"
    }
  }

  useEffect(() => {
    async function handler({ data }) {
      const { code, msg } = JSON.parse(data)
      setCode(code)
      setMsg(msg)
      await sleep(5000)
      clear()
    }

    function connect() {
      const url = new URL("/ws", location.href)
      url.protocol = "ws"

      const ws = new WebSocket(url)
      ws.onmessage = handler
      ws.onclose = async e => {
        console.warn("socket closed.", e)
        await sleep(1000)
        connect()
      }
    }
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
      </header>
      <main>
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
            textAlign: "center",
            overflow: "visible",
          }}>
          {msgText(msg)}
        </div>
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
