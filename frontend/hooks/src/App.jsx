import { useState, useEffect } from 'react'
import './App.css'
import HungerMap from './map'

function App() {
  const [details, setdetails] = useState({ count: 0, name: "" })
  const [c, setc] = useState(0)

  const handle = () => {
    if (details.count >= 20) {
      alert("it is greater than 20")
    } else {
      setdetails(prev => ({
        ...prev,
        count: prev.count + 1
      }))
    }
  }

  const increase = () => {
    setc(c + 5)
  }

  const remove = () => {
    if (details.count <= 0) {
      alert("no negative is allowed")
    } else {
      setdetails(prev => ({
        ...prev,
        count: prev.count - 1
      }))
    }
  }

  useEffect(() => {
    document.title = `${c} new message`
  }, [c])

  return (
    <>
      <h1>hi</h1>
       <HungerMap/>
    </>
  )
}

// export const LoginCont ext=createContext();

// <LoginContext.Provider value={true}>
//   <div>
//     <mainComponent/>
//   </div>
// </LoginContext.Provider>  # import there and use it from global----->small

export default App
