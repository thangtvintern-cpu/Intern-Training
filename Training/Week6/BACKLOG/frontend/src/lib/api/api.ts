import axios, { AxiosError, type AxiosRequestConfig } from "axios"
import { tokenService } from "../../features/auth/service/tokenService"
import { authService } from "../../features/auth/service/authService"

const axiosInstance = axios.create({
    baseURL: `${import.meta.env.VITE_API_URL}/api/v1`,
    headers: {
        "Content-Type": "application/json",
    },
    withCredentials: true,

})

axiosInstance.interceptors.request.use((config) => {
    const token = tokenService.getToken()
    if (token) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})



axiosInstance.interceptors.response.use((response) => response,
    async (error: AxiosError) => {
        const request = error.config as any
        if (error.response?.status === 401 && request && !request._retry) {
            request._retry = true
            try {
                const { access_token } = await authService.refresh()
                tokenService.setToken(access_token)
                if (request.headers) {
                    request.headers.Authorization = `Bearer ${access_token}`
                }
                return axiosInstance(request)
            } catch (error) {
                tokenService.clearToken()
                window.dispatchEvent(new Event("force-logout"))
                return Promise.reject(error)
            }
        }
        return Promise.reject(error)
    }
);

export const api = {
    get: <T>(url: string, config?: AxiosRequestConfig): Promise<T> =>
        axiosInstance.get<T>(url, config).then((res) => res.data),

    post: <T>(url: string, data?: unknown, config?: AxiosRequestConfig): Promise<T> =>
        axiosInstance.post<T>(url, data, config).then((res) => res.data),

    put: <T>(url: string, data?: unknown, config?: AxiosRequestConfig): Promise<T> =>
        axiosInstance.put<T>(url, data, config).then((res) => res.data),

    patch: <T>(url: string, data?: unknown, config?: AxiosRequestConfig): Promise<T> =>
        axiosInstance.patch<T>(url, data, config).then((res) => res.data),

    delete: <T>(url: string, config?: AxiosRequestConfig): Promise<T> =>
        axiosInstance.delete<T>(url, config).then((res) => res.data),
};
