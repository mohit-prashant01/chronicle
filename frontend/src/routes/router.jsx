import { createBrowserRouter } from "react-router-dom";
import MainLayout from "../layouts/MainLayout"
import Home from "../pages/Home"
import Login from "../pages/Login"
import Register from "../pages/Register"
import Dashboard from "../pages/Dashboard"
import CreatePost from "../pages/CreatePost"
import PostDetail from "../pages/PostDetail"
import NotFound from "../pages/NotFound"
import ProtectedRoute from "./ProtectedRoute";


export const router=createBrowserRouter(
    [
        {
            path:"/",
            element:<MainLayout/>,
            children:[
                {index:true,element:<Home/>},

                {path:"login",element:<Login/>},

                {path:"register",element:<Register/>},

                {path:"dashboard",
                    element:(
                        <ProtectedRoute>
                            <Dashboard/>
                        </ProtectedRoute>
                    )},

                {path:"create",
                    element:(
                        <ProtectedRoute>
                            <CreatePost/>
                        </ProtectedRoute>
                    )
                    },

                {path:"posts/:id",element:<PostDetail/>}               
            ]
        },
        {
            path:"*",
            element:<NotFound/>
        }
    ]
)