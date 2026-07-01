import client from "../api/client"

export async function registerUser(data){
    const res= await client.post("/auth/register",data)
    return res.data
}

export async function loginUser(email,password){
    const body=new URLSearchParams()
    body.append("username",email)
    body.append("password",password)

    const res= await client.post("/auth/login",body,
        {
            headers:{
                "Content-Type":"application/x-www-form-urlencoded"
            }
        }
    )
    return res.data
}