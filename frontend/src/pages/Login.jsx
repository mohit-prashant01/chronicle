import { useAuth } from "../context/AuthContext"

export default function Login(){
    const {login}=useAuth()
    return(
      <button className="border px-5 py-2"
        onClick={()=>login("demo-token")}>
        Fake Login
      </button>
    )   
}