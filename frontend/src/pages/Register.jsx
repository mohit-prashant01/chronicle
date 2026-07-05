import {useState} from "react"
import { registerUser } from "../services/authService"

export default function Register(){
    const[form,setForm] = useState({
        username:"",
        email:"",
        password:""
    })

    const[loading,setLoading]=useState(false)
    const[error,setError]=useState("")
    const[success,setSuccess]=useState("")

    async function submit(){
            setLoading(true)
            setError("")
            setSuccess("")
            try{
                await registerUser(form)
                setSuccess("Registration successful")
            }
            catch(err){
                setError("Registration Failed")
            }
            finally{
                setLoading(false)
            }
    }

    return(
        <div className="space-u-4 max-w-sm">
            <input placeholder="username"
                   className="border p-2 w-full"
                   onChange={e=>setForm({
                           ...form,
                           username:e.target.value
                   })}
             />

             <input placeholder="email"
                    className="border p-2 w-full"
                    onChange={e=>setForm({
                            ...form,
                            email:e.target.value
                        })}
             />

             <input type="password"
                    placeholder="password"
                    className="border p-2 w-full"
                    onChange={e=>setForm({
                            ...form,
                            password:e.target.value
                    })}
             />

            <button onClick={submit}
                    className="border px-4 py-2"
                    disabled={loading}
            >
                {loading?"Registering...":"Register"}
            </button>
          
            {
                success && 
                <p className="text-green-600">
                    {success}
                </p>
            }

            {
                error &&
                <p className="text-red-500">
                    {error}
                </p>
            }

        </div>
    )
}