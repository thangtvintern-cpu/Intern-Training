import type { LoginRequest, LoginResponse, RegisterRequest, RefreshResponse, GetMeResponse } from "../types";
import { api } from "../../../lib/api/api";

export const authService = {
    login: async (data: LoginRequest): Promise<LoginResponse> => {
        return await api.post<LoginResponse>("/auth/login", data)
    },
    logout: async (): Promise<void> => {
        return await api.post("/auth/logout")
    },
    register: async (data: RegisterRequest): Promise<LoginResponse> => {
        return await api.post<LoginResponse>("/auth/register", data)
    },
    refresh: async (): Promise<RefreshResponse> => {
        return await api.post<RefreshResponse>("/auth/refresh")
    },
    getMe: async (): Promise<GetMeResponse> => {
        return await api.get<GetMeResponse>("/auth/me")
    }
}