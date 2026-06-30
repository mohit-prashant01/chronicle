import axios from "axios"

export async function ping(){
    const res = await axios.get("http://127.0.0.1:8000")
    return res.data
}