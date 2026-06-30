import {createContext, useContext, useEffect, useState} from "react"

const AuthContext = createContext()

export function AuthProvider({children}){
    const[token,setToken]=useState(null)

    useEffect(()=>{
        const saved = localStorage.getItem("token")
        if(saved){
            setToken(saved)
        }
    },[])

    function login(accessToken){
        localStorage.setItem("token",accessToken)
        setToken(accessToken)
    }

    function logout(){
        localStorage.removeItem("token")
        setToken(null)
    }

    return(
        <AuthContext.Provider value = {
            {
                token,
                isAuthenticated:!!token,
                login,
                logout
            }
        }>
            {children}
            </AuthContext.Provider>
    )
}


export function useAuth(){
    return useContext(AuthContext)
}