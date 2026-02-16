

let _accessToken :string | null = null;
export const tokenService = {
    setToken : (token:string) => {
        _accessToken = token;
    },
    getToken : () => {
        return _accessToken
    },
    clearToken : () => {
        _accessToken = null
    }
}