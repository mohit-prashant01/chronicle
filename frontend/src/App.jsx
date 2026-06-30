import { useEffect } from "react";
import { ping } from "./api/test";

function App(){
  useEffect(()=>{ping().then(console.log)},[])

  return (
    <h1>Chronicle</h1>
  )
}

export default App