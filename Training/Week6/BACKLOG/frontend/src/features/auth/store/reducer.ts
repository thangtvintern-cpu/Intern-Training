
import type { AuthState, AuthAction } from "../types";

export const INITIAL_STATE: AuthState = {
    user: null,
    access_token: null,
    error: null,
    status: 'initial' as const,
}

export const reducer = (initialState: AuthState, action: AuthAction) => {
    switch (action.type) {

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

        case "TOKEN_REFRESH_SUCCESS":
            return {
                ...initialState,
                access_token: action.payload.access_token,
            }
        case "TOKEN_REFRESH_FAILURE":
            return {
                ...initialState,
                status: 'unauthenticated' as const,
                error: action.payload,
            }
        case "GET_ME_SUCCESS":
            return {
                ...initialState,
                status: 'authenticated' as const,
                user: action.payload.user,
            }
        case "GET_ME_FAILURE":
            return {
                ...initialState,
                status: 'unauthenticated' as const,
                error: action.payload,
            }
        case "NO_SESSION":
            return {
                ...initialState,
                status: 'unauthenticated' as const,
            }
        default:
            return initialState
    }
}
