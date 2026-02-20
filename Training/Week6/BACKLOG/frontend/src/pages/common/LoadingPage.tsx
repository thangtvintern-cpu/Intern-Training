

const LoadingPage = () => {
    return (
        <div className="min-h-[60vh] flex flex-col justify-center items-center gap-6 bg-page text-text-primary">

            <div className="relative">
                <div className="size-14 rounded-full border-4 border-border border-t-brand animate-spin"></div>
            </div>

            <div className="text-center">
                <p className="text-lg font-semibold">Loading data...</p>
                <p className="text-sm text-text-secondary mt-1">
                    Please wait a moment
                </p>
            </div>

        </div>

    )
}

export default LoadingPage