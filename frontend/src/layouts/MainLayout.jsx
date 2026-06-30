import { Outlet } from "react-router-dom";

export default function MainLayout(){
    return(
        <div className="min-h-screen">
            <nav className="p-5 border -b">
                Chronicle
            </nav>

            <main className="max-w-6xl mx-auto p-6">
                <Outlet/>
            </main>
        </div>
    )
}