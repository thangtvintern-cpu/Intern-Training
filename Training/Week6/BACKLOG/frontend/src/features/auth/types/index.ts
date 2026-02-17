export type Role = "admin" | "user"
export interface User {
    id: string;
    email: string;
    name: string;
    role: Role;
    created_at: string;
    updated_at?: string;
}
export type AuthStatus = "checking" | "loading" | "unauthenticated" | "authenticated"

export interface AuthState {
    user: User | null;
    access_token: string | null;
    error: string | null;
    status: AuthStatus;
}
export interface RefreshResponse {
    access_token: string;
}
export interface GetMeResponse {
    user: User;
}
export interface LoginRequest {
    email: string;
    password: string;
}

export interface LoginResponse {
    access_token: string;
    user: User;
}

export interface RegisterRequest {
    email: string;
    password: string;
    name: string;
    age: number;
    gender: string;
    phone_number: string;
}



export type AuthAction =

    { type: "LOGIN_START" }
    | { type: "LOGIN_SUCCESS", payload: LoginResponse }
    | { type: "LOGIN_FAILURE", payload: string }
    | { type: "LOGOUT" }
    | { type: "REGISTER_START" }
    | { type: "REGISTER_SUCCESS", payload: LoginResponse }
    | { type: "REGISTER_FAILURE", payload: string }
    | { type: "APP_STARTUP" }
    | { type: "TOKEN_REFRESH_START" }
    | { type: "TOKEN_REFRESH_SUCCESS", payload: RefreshResponse }
    | { type: "TOKEN_REFRESH_FAILURE", payload: string }
    | { type: "GET_ME_START" }
    | { type: "GET_ME_SUCCESS", payload: GetMeResponse }
    | { type: "GET_ME_FAILURE", payload: string }
    | { type: "NO_SESSION"}
