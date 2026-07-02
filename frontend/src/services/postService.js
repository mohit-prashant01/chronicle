import client from "../api/client"

export async function createPost(data){
    const res=await client.post("/posts/",data)
    return res.data
}

export async function getPosts(){
    const res=await client.get("/posts")
    return res.data
}