import { NavLink } from "react-router-dom"
import { z } from "zod"
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import { useAuthActions } from "../context/AuthContext"



const LoginType = z.object({
    email: z.string().min(6, { message: "Email must be at least 6 characters" }),
    password: z.string().min(6, { message: "Password must be at least 6 characters" }),
})

type LoginType = z.infer<typeof LoginType>

const LoginPage = () => {
    const { setError } = useForm<LoginType>()
    const { login } = useAuthActions()
    const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm<LoginType>({
        resolver: zodResolver(LoginType),
        defaultValues: {
            email: "",
            password: "",
        }
    })
    const onSubmit = async (data: LoginType) => {
        try {
            const form = new URLSearchParams()
            form.append("username", data.email)
            form.append("password", data.password)
            await login(form)
        } catch (error) {
            setError("email", { message: "Email or password is incorrect" })
        }
    }


    return (
        // <div className="w-full h-4/5 text-black flex justify-center items-center">
        //     <div className="bg-transparent w-2/5 rounded-lg shadow-lg p-8">
        //         <div className="flex flex-col items-center gap-4 mb-4">
        //             <div className="size-9 shrink-0 rounded-xl bg-linear-to-br from-indigo-500 to-indigo-400 flex items-center justify-center text-white font-extrabold text-base shadow-md shadow-indigo-200">
        //                 T
        //             </div>
        //             <h1 className="text-2xl font-bold ">Welcome to Backlog</h1>
        //             <p className="text-base text-gray-400">Please login to your account</p>
        //         </div>
        //         <div>
        //             <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-6">
        //                 <p className="text-red-500 text-sm mb-3">{errors.email?.message as string}</p>
        //                 <div>
        //                     <label htmlFor="email" className="text-sm font-bold text-gray-500 mb-2 inline-block">Email</label>
        //                     <input {...register("email")} placeholder="Enter your email" type="email" id="email" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
        //                 </div>
        //                 <div>
        //                     <label htmlFor="password" className="text-sm font-bold text-gray-500 mb-2 inline-block">Password</label>
        //                     <input {...register("password")} placeholder="Enter your password" type="password" id="password" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
        //                 </div>
        //                 <button disabled={isSubmitting} type="submit" className="w-full px-3 py-2.5 text-base font-bold bg-indigo-500 hover:bg-indigo-600 no-underline rounded-md transition-colors">Login</button>
        //             </form>
        //         </div>
        //         <div className="flex justify-center items-center mt-6">
        //             <p className="text-base text-gray-400">Don't have an account? <NavLink to="/register" className="text-indigo-500 hover:text-indigo-600 no-underline">Register</NavLink></p>
        //         </div>
        //     </div>
        // </div>
        <div className="w-full h-4/5 bg-page text-text-primary flex justify-center items-center">
            <div className="bg-surface w-2/5 rounded-lg shadow-md p-8 border border-border">

                {/* Logo + Title */}
                <div className="flex flex-col items-center gap-4 mb-6">
                    <div className="size-9 shrink-0 rounded-xl 
                      bg-brand text-white 
                      flex items-center justify-center 
                      font-extrabold text-base 
                      shadow-sm">
                        T
                    </div>

                    <h1 className="text-2xl font-bold">
                        Welcome to Backlog
                    </h1>

                    <p className="text-base text-text-secondary">
                        Please login to your account
                    </p>
                </div>

                {/* Form */}
                <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-6">

                    {/* Error message */}
                    {errors.email && (
                        <p className="text-danger text-sm">
                            {errors.email?.message as string}
                        </p>
                    )}

                    {/* Email */}
                    <div>
                        <label
                            htmlFor="email"
                            className="form-label"
                        >
                            Email
                        </label>

                        <input
                            {...register("email")}
                            type="email"
                            id="email"
                            placeholder="Enter your email"
                            className="form-input"
                        />
                    </div>

                    {/* Password */}
                    <div>
                        <label
                            htmlFor="password"
                            className="form-label"
                        >
                            Password
                        </label>

                        <input
                            {...register("password")}
                            type="password"
                            id="password"
                            placeholder="Enter your password"
                            className="form-input"
                        />
                    </div>

                    {/* Submit */}
                    <button
                        disabled={isSubmitting}
                        type="submit"
                        className="custom-btn"
                    >
                        Login
                    </button>
                </form>

                {/* Footer */}
                <div className="flex justify-center items-center mt-6">
                    <p className="text-base text-text-secondary">
                        Don't have an account?{" "}
                        <NavLink
                            to="/register"
                            className="text-brand hover:text-brand-hover font-medium no-underline"
                        >
                            Register
                        </NavLink>
                    </p>
                </div>
            </div>
        </div>

    )
}

export default LoginPage
