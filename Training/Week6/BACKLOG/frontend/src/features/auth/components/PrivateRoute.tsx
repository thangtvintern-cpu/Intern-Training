import { Navigate, Outlet, useLocation } from "react-router-dom"
import { useAuthStatus } from "../hooks/useAuth"


const PrivateRoute = () => {
    const status = useAuthStatus()
    const location = useLocation()
    if (status === "unauthenticated") {
        return <Navigate to={"/login"} state={{ from: location.pathname }} replace />
    }
    return (
        <>
            <Outlet />
        </>
    )
}

export default PrivateRoute
