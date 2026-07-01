import { Link } from "react-router-dom";

export default function Dashboard(){
    return(
        <div className="space-y-6">
            <h1 className="text-4xl font-bold">
                Dashboard
            </h1>

            <Link to="/create" className="border px-4 py-2 inline-block">
                Create Post
            </Link>
        </div>
    )
}