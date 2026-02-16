import { Navigate, Outlet } from "react-router-dom"
import { useAuthUser } from "../hooks/useAuth"
import type { Role } from "../types"

interface RoleGuardProps {
    allowedRoles: Role[]
}

const RoleGuard = ({ allowedRoles }: RoleGuardProps) => {
    const user = useAuthUser()
    if (!user) {
        return <Navigate to="/login" replace />
    }
    if (!allowedRoles.includes(user.role)) {
        return <Navigate to="/unauthorized" replace />
    }
    return <Outlet />
}

export default RoleGuard