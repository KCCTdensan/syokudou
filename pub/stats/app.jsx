const { useEffect, useState } = React

const timeDiffFmt = (dt, now) => {
  const ds = (now - dt) / 1000
  if(ds < 0) return "未来"

  const h = Math.trunc(ds / 3600)
  const m = Math.trunc((ds - 3600 * h) / 60)

  const date = new Date(dt)
  return `${h}時間と${m}分前 (${date.toLocaleString("ja")})`
}

const Stats = () => {
  const [tab, setTab] = useState([])

  useEffect(async () => {
    const dump = await fetch("/api/dump").then(res => res.json())
    dump.sort((a, b) => b.date - a.date)
    setTab(dump)
  }, [])

  return (
    <>
      <header>
        <h1>食堂管理システム - 統計情報</h1>
        <a href="/">メインUIに戻る</a>
      </header>
      <main>
        <table>
          <thead>
            <tr>
              <th>時刻</th>
              <th>学籍番号</th>
              {/*<th>イベント</th>*/}
            </tr>
          </thead>
          <tbody>
            {tab.map(({ code, event, date }, i) => (
              <tr key={i}>
                <td>{timeDiffFmt(date, Date.now())}</td>
                <td>{code}</td>
                {/*<td>{event}</td>*/}
              </tr>
            ))}
          </tbody>
        </table>
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

ReactDOM.render(<Stats />, document.getElementById("root"))
