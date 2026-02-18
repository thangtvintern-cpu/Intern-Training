import { Navigate, Outlet } from "react-router-dom"
import { useAuthStatus } from "../hooks/useAuth"



const PublicRoute = () => {
    const status = useAuthStatus()

    if (status === "authenticated") {
        return <Navigate to="/" replace />
    }
    return (
        <>
            <Outlet />
        </>
    )
}

export default PublicRoute