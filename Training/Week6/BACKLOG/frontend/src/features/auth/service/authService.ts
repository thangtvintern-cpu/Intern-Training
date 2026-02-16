import type { LoginRequest,AuthResponse,RegisterRequest, RefreshResponse } from "../types";
import { api } from "../../../lib/api/api";

export const authService = {
    login : async (data:LoginRequest): Promise<AuthResponse> => {
        return await api.post<AuthResponse>("/auth/login",data)
    },
    logout : async (): Promise<void> => {
        return await api.post("/auth/logout")
    },
    register : async (data:RegisterRequest): Promise<AuthResponse> => {
        return await api.post<AuthResponse>("/auth/register",data)
    },
    refresh : async (): Promise<RefreshResponse> => {
        return await api.post<RefreshResponse>("/auth/refresh")
    },
    getMe : async (): Promise<AuthResponse> => {
        return await api.get<AuthResponse>("/auth/me")
    }
}