import { useEffect,useState } from "react"
import { useNavigate,useParams } from "react-router-dom"
import { getPost,updatePost,deletePost } from "../services/postService"

export default function PostDetail(){
    const{id}=useParams()
    const navigate = useNavigate()
    const[post,setPost]=useState(null)
    const[loading,setLoading]=useState(true)
    const[error,setError]=useState("")
    const[isEditing,setIsEditing]=useState(false)
    const[title,setTitle]=useState("")
    const[content,setContent]=useState("")


    useEffect(()=>{
        fetchPost()
    },[id])

    async function fetchPost(){
        try{
            const data=await getPost(id)
            setPost(data)
            setTitle(data.title)
            setContent(data.content)
        }
        catch{
            setError("Post not found")
        }
        finally{
            setLoading(false)
        }
    }

    async function handleUpdate(){
        try{
            const updated = await updatePost(id,{title,content})

            setPost(updated)
            setIsEditing(false)
        }
        catch{
            alert("Unable to update post")
        }
    }


    async function handleDelete(){
        const confirmDelete = window.confirm("Delete this post?")

        if(!confirmDelete)return
        
        try{
            await deletePost(id)
            navigate("/dashboard")
        }
        catch{
            alert("Unable to delete post")
        }
    }


    if(loading){
        return <h2>Loading...</h2>
    }

    if(error){
        return <h2>{error}</h2>
    }


    return(
        <div className = "max-w-3xl mx-auto space-y-6">
            {
                isEditing?(
                    <> 
                    <input className="border w-full p-2"
                           value={title}
                           onChange={(e)=>setTitle(e.target.value)} 
                           />

                    <textarea className="border w-full p-20"
                              value={content}
                              onChange={(e)=>setContent(e.target.value)}
                    />

                    <button className="border px-4 py-2"
                            onClick={handleUpdate}
                            >Save
                    </button>
                    
                    </>
                ):(
                    <>
                    <h1 className="text-4xl font-bold">
                        {post.title}
                    </h1>

                    <p className="text-gray-500">
                        {post.reading_time} min read
                    </p>

                    <p className="whitespace-prewrap">
                        {post.content}
                    </p>

                    <div className="flex gap-4">
                        <button className="border px-4 py-2"
                                onClick={()=>setIsEditing(true)}>
                                    Edit
                        </button>

                        <button className="border px-4 py-2 text-red-600"
                                onClick={handleDelete}>
                                    Delete
                        </button>
                    </div>
                    </>
                )
            }
        </div>
    )
}