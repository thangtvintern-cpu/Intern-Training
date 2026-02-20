import { useAuthStatus } from "../../features/auth"
import LoadingPage from "../../pages/common/LoadingPage"





const AppInitial = ({ children }: { children: React.ReactNode }) => {
    const status = useAuthStatus()

    if (status === "initial") return <LoadingPage />
    return (
        <>
            {children}
        </>
    )
}

export default AppInitial