import { useAuthActions, useAuthState } from "../context/AuthContext"


export const useAuth = () => {
    const state = useAuthState()
    const actions = useAuthActions()

    return {
        user: state.user,
        accessToken: state.access_token,
        status: state.status,
        isAuthenticated: state.status === "authenticated",
        isStartup: state.status === "checking",
        isLoading: state.status === "loading" || state.status === "checking",
        error: state.error,
        ...actions
    }
}


export const useAuthStatus = () => {
    return useAuthState().status
}


export const useAuthUser = () => {
    return useAuthState().user
}

