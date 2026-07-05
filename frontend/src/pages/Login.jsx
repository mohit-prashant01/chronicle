import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../services/authService";
import { useAuth } from "../context/AuthContext";
import { useEffect } from "react";

export default function Login(){
  const navigate=useNavigate()
  const{login,isAuthenticated}=useAuth()
  const[email,setEmail]=useState("")
  const[password,setPassword]=useState("")

  const[loading,setLoading]=useState(false)
  const[error,setError]=useState("")


  useEffect(()=>{
    if(isAuthenticated){
      navigate("/dashboard")
    }
  },[isAuthenticated])

  async function submit(){
    setLoading(true)
    setError("")
    
    try{
      const res=await loginUser(email,password)
      login(res.access_token)
      navigate("/dashboard")
    }
    catch(err){
      setError("Invalid email or password")
    }
    finally{
      (setLoading(false))
    }
  }

  return(
    <div className="space-y-4 max-w-sm">

      <input className="border p-2 w-full"
             placeholder="email"
             onChange={e=>setEmail(e.target.value)}/>

      <input type="password"
             className="border p-2 w-full"
             onChange={e=>setPassword(e.target.value)}/>

            {error && 
              <p className="text-red-500 text-sm">
                {error}
              </p>
            }


      <button className="border px-4 py-2 w-full"
              onClick={submit}
              disabled={loading}>
              {loading?"Logging in...":"Login"}
      </button>

    </div>
  )
}