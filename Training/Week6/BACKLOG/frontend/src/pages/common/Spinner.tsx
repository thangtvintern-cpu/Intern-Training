import { twMerge } from "tailwind-merge"


export const Spinner = ({ className }: { className?: string }) => {
    const finalClassName = twMerge("size-2 rounded-full border-2 border-border border-t-brand animate-spin", className)
    return (
        <div className="flex justify-center items-center">
            <div className={finalClassName}></div>
        </div>
    )
}