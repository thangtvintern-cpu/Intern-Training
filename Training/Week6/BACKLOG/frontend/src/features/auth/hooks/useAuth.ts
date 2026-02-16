import { useAuthActions, useAuthState } from "../context/AuthContext"


export const useAuth = () => {
    const state = useAuthState()
    const actions = useAuthActions()

    return {
        user: state.user,
        accessToken: state.access_token,
        status: state.status,
        isAuthenticated: state.status === "authenticated",
        isStartup: state.status === "startup",
        isLoading: state.status === "loading" || state.status === "startup",
        error: state.error,
        ...actions
    }
}