import type { AuthState } from "../types";
import { createContext, useContext, useEffect, useReducer } from "react";
import type { ReactNode } from "react";
import { reducer, INITIAL_STATE } from "../store/reducer";
import type { RegisterRequest } from "../types";
import { authService } from "../service/authService";
import { useNavigate } from "react-router-dom";
import { tokenService } from "../service/tokenService";
import toast from "react-hot-toast";

interface AuthActions {
    login: (data: URLSearchParams, redirectTo?: string) => Promise<void>
    logout: () => Promise<void>
    registerRequest: (data: RegisterRequest) => Promise<void>
}

const AuthStateContext = createContext<AuthState | null>(null)
const AuthDispatchContext = createContext<AuthActions | null>(null)

export const AuthProvider = ({ children }: { children: ReactNode }) => {
    const [state, dispatch] = useReducer(reducer, INITIAL_STATE)
    const navigate = useNavigate()

    useEffect(() => {
        const handleLogout = () => {
            dispatch({ type: "LOGOUT" })
            tokenService.clearToken()
            navigate("/login", { replace: true })
        }
        window.addEventListener("force-logout", handleLogout)
        return () => {
            window.removeEventListener("force-logout", handleLogout)
        }
    }, [navigate])

    const login = async (data: URLSearchParams, redirectTo?: string) => {
        try {
            setTimeout(() => { }, 3000)
            const { user, access_token } = await authService.login(data)
            tokenService.setToken(access_token)
            tokenService.setFlag(user.id)
            toast.success("Login success")
            dispatch({ type: "LOGIN_SUCCESS", payload: { user, access_token } })
            if (redirectTo) {
                navigate(redirectTo, { replace: true })
            }
        } catch (error) {
            const message = error instanceof Error ? error.message : "Login failed"
            toast.error("Login failed")
            dispatch({ type: "LOGIN_FAILURE", payload: message })
            throw error
        }
    }

    const logout = async () => {
        try {
            await authService.logout()
            dispatch({ type: "LOGOUT" })
            tokenService.clearToken()
            tokenService.clearFlag()
            toast.success("Logout success")
            navigate("/login", { replace: true })
        } catch (error) {
            const message = error instanceof Error ? error.message : "Logout failed"
            toast.error("Logout failed")
            dispatch({ type: "LOGIN_FAILURE", payload: message })
            throw error
        }
    }

    const registerRequest = async (data: RegisterRequest) => {
        await authService.register(data)
    }

    useEffect(() => {

        const tryGetAuth = async () => {
            const flag = tokenService.getFlag()
            if (flag) {
                try {
                    const { access_token } = await authService.refresh()
                    const { user } = await authService.getMe()
                    tokenService.setToken(access_token)
                    dispatch({ type: "GET_ME_SUCCESS", payload: { user } })
                } catch (err) {
                    const message = err instanceof Error ? err.message : "Failed to get user"
                    dispatch({ type: "GET_ME_FAILURE", payload: message })
                }
            }
            dispatch({ type: "NO_SESSION" })
        }
        tryGetAuth()
    }, [])


    return (
        <AuthStateContext.Provider value={state}>
            <AuthDispatchContext.Provider value={{ login, logout, registerRequest }}>
                {children}
            </AuthDispatchContext.Provider>
        </AuthStateContext.Provider>
    );
}

export const useAuthState = () => {
    const cxt = useContext(AuthStateContext)
    if (!cxt) throw new Error("useAuthState must be used within AuthProvider")
    return cxt
}

export const useAuthActions = () => {
    const cxt = useContext(AuthDispatchContext)
    if (!cxt) throw new Error("useAuthActions must be used within AuthProvider")
    return cxt
}