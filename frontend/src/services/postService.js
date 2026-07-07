import client from "../api/client"

export async function createPost(data){
    const res=await client.post("/posts/",data)
    return res.data
}

export async function getPosts(){
    const res=await client.get("/posts/")
    return res.data
}

export async function getPost(id){
    const res = await client.get(`/posts/${id}`)
    return res.data
}

export async function updatePost(id,data){
    const res = await client.patch(`/posts/${id}`,data)
    return res.data
}

export async function deletePost(id){
    await client.delete(`/posts/${id}`)
}