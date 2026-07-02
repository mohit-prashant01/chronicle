import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createPost } from "../services/postService";

export default function CreatePost(){
    const navigate = useNavigate()
    const[title,setTitle]=useState("")
    const[content,setContent]=useState("")

    async function submit(){
        await createPost({title,content})
        navigate("/dashboard")
    }


    return(
        <div className="max-w-xl space-y-4">
            <h1 className="text-3xl font-bold">
                Create Post
            </h1>

            <input className="border w-full p-2"
                   placeholder="title"
                   onChange={e=> setTitle(e.target.value)}
             />



            <textarea rows={10}
                      className="border w-full p-2"
                      placeholder="content"
                      onChange={e=> setContent(e.target.value)}
            />

            <button className="border px-5 py-2"
                    onClick={submit}>
                    Publish
            </button>

        </div>
    )
}