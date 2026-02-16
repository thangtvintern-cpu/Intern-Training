
import type { AuthState, AuthAction } from "../types";

export const INITIAL_STATE: AuthState = {
    user: null,
    access_token: null,
    error: null,
    status: 'startup' as const,
}

export const reducer = (initialState: AuthState, action: AuthAction) => {
    switch (action.type) {
        case "APP_STARTUP":
        case "REGISTER_START":
        case "LOGIN_START":
            return {
                ...initialState,
                status: 'loading' as const,
                error: null,
            }
        case "LOGIN_SUCCESS":
            return {
                ...initialState,
                status: 'authenticated' as const,
                user: action.payload.user,
                access_token: action.payload.access_token,
            }
        case "LOGIN_FAILURE":
            return {
                ...initialState,
                status: 'unauthenticated' as const,
                error: action.payload,
            }
        case "LOGOUT":
            return {
                ...initialState,
                status: 'unauthenticated' as const,
                user: null,
                access_token: null,
            }
        case "REGISTER_SUCCESS":
            return {
                ...initialState,
                status: 'authenticated' as const,
                user: action.payload.user,
                access_token: action.payload.access_token,
            }
        case "REGISTER_FAILURE":
            return {
                ...initialState,
                status: 'unauthenticated' as const,
                error: action.payload,
            }
        case "TOKEN_REFRESHED":
            return {
                ...initialState,
                status: 'authenticated' as const,
                access_token: action.payload.access_token,
            }
        default:
            return initialState
    }
}
