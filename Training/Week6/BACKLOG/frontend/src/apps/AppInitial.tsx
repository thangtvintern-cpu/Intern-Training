import { useAuthStatus } from "../features/auth"
import LoadingPage from "../pages/common/LoadingPage"





const AppInitial = ({ children }: { children: React.ReactNode }) => {
    const status = useAuthStatus()

    if (status === "checking" || status === "loading") return <LoadingPage />
    return (
        <>
            {children}
        </>
    )
}

export default AppInitial