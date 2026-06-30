import { Outlet,Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function MainLayout(){
    const {isAuthenticated,logout}=useAuth()

    return(
        <div className="min-h-screen">
            <nav className="p-5 border -b flex justify-between">
                <Link to="/">Chronicle</Link>
                <div className="fkex gao-4">
                    {
                        isAuthenticated?<>
                            <button onClick={logout}>
                                Logout
                            </button>
                            <Link to="/dashboard">
                              Dashboard
                            </Link>
                        </>:
                        <>
                        <Link to="/login">Login</Link>
                        <Link to="/register">Register</Link>
                        </>
                    }
                </div>
            </nav>

            <main className="max-w-6xl mx-auto p-6">
                <Outlet/>
            </main>
        </div>
    )
}