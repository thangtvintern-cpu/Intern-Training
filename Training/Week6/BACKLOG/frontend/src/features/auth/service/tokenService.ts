

let _accessToken: string | null = null;
export const tokenService = {
    setToken: (token: string) => {
        _accessToken = token;
    },
    getToken: () => {
        return _accessToken
    },
    clearToken: () => {
        _accessToken = null
    },

    // flag để đánh dấu user đã login, khi logout phải clear
    setFlag: (flag:string) => localStorage.setItem("flag", flag),
    getFlag: () => localStorage.getItem("flag"),
    clearFlag: () => localStorage.removeItem("flag")
}