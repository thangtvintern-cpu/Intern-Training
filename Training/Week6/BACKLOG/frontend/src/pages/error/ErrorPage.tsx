import { useNavigate } from "react-router-dom"


const ErrorPage = () => {
    const navigate = useNavigate()
    return (
        <div className="flex min-h-screen flex-col items-center justify-center bg-background text-foreground px-4 text-center">
            <h1 className="text-4xl font-bold">Something went wrong</h1>
            <p className="mt-2 text-muted-foreground">
                An unexpected error has occurred.
            </p>

            <button
                onClick={() => navigate("/")}
                className="mt-6 rounded-md bg-primary px-4 py-2 text-primary-foreground hover:opacity-90 transition"
            >
                Go back home
            </button>
        </div>
    )
}

export default ErrorPage