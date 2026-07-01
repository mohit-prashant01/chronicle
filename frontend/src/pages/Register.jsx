import {useState} from "react"
import { registerUser } from "../services/authService"

export default function Register(){
    const[form,setForm] = useState({
        username:"",
        email:"",
        password:""
    })

    async function submit(){
        await registerUser(form)
        alert("Registered")
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
            >Register</button>

        </div>
    )
}