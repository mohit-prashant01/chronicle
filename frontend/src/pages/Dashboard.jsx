import {useEffect,useState} from "react"
import {Link} from "react-router-dom"
import {getPosts} from "../services/postService"

export default function Dashboard(){
    const[posts,setPosts]=useState([])
    useEffect(()=>{
        getPosts().then(setPosts)
    },[])

    return(
        <div className = "space-y-6">
            <div className="flex justify-between">
                <h1 className="text-3xl font-bold">
                    Dashboard
                </h1>
                
                <Link to="/create"
                      className="border px-4 py-2">
                Create
                </Link>

            </div>

            <div className="space-y-4">
                {
                    posts.map(post=>(
                        <div key={post.id} className="border p-4">
                            <h2 className ="font-bold">
                                {post.title}
                            </h2>

                            <p>
                                {post.content}
                            </p>

                            <div className="text-sm mt-2">
                                {post.reading_time}
                                min read
                            </div>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}