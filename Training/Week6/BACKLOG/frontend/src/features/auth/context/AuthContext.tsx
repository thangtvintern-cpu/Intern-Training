import type { AuthState } from "../types";
import { createContext, useContext, useEffect, useReducer } from "react";
import type { ReactNode } from "react";
import { reducer, INITIAL_STATE } from "../store/reducer";
import type { LoginRequest, RegisterRequest } from "../types";
import { authService } from "../service/authService";
import { useNavigate } from "react-router-dom";
import { tokenService } from "../service/tokenService";

interface AuthActions {
    login: (data: LoginRequest, redirectTo?: string) => Promise<void>
    logout: () => Promise<void>
    register: (data: RegisterRequest) => Promise<void>
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

    const login = async (data: LoginRequest, redirectTo?: string) => {
        dispatch({ type: "LOGIN_START" })
        try {
            const response = await authService.login(data)
            tokenService.setToken(response.access_token)
            dispatch({ type: "LOGIN_SUCCESS", payload: response })
            if (redirectTo) {
                navigate(redirectTo, { replace: true })
            }
        } catch (error) {
            const message = error instanceof Error ? error.message : "Login failed"
            dispatch({ type: "LOGIN_FAILURE", payload: message })
            throw error
        }
    }

    const logout = async () => {
        try {
            await authService.logout()
            dispatch({ type: "LOGOUT" })
            tokenService.clearToken()
            navigate("/login", { replace: true })
        } catch (error) {
            const message = error instanceof Error ? error.message : "Logout failed"
            dispatch({ type: "LOGIN_FAILURE", payload: message })
            throw error
        }
    }

    const register = async (data: RegisterRequest) => {
        dispatch({ type: "REGISTER_START" })
        try {
            const response = await authService.register(data)
            tokenService.setToken(response.access_token)
            dispatch({ type: "REGISTER_SUCCESS", payload: response })
        } catch (err) {
            const message = err instanceof Error ? err.message : "Register failed"
            dispatch({ type: "REGISTER_FAILURE", payload: message })
            throw err
        }
    }

    return (
        <AuthStateContext.Provider value={state}>
            <AuthDispatchContext.Provider value={{ login, logout, register }}>
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