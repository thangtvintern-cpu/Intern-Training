import { NavLink, useNavigate } from "react-router-dom"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import { useAuthActions } from "../context/AuthContext"
import toast from "react-hot-toast"

const registerSchema = z.object({
    email: z.string().min(6, { message: "Email must be at least 6 characters" }),
    password: z.string().min(6, { message: "Password must be at least 6 characters" }),
    confirmPassword: z.string().min(6, { message: "Confirm password must be at least 6 characters" }),
    firstName: z.string().min(2, { message: "First name must be at least 2 characters" }),
    lastName: z.string().min(2, { message: "Last name must be at least 2 characters" }),
    dateOfBirth: z.string(),
    gender: z.string().min(1, { message: "Gender is required" }),
    mobile: z.string().min(9, { message: "Phone number must be at least 10 characters" }),
    terms: z.boolean().refine(value => value === true, { message: "You must accept the terms and conditions" }),
}).refine((data) => data.password === data.confirmPassword, {
    message: "Passwords do not match",
    path: ["confirmPassword"],
})

type RegisterType = z.infer<typeof registerSchema>

const RegisterPage = () => {
    const { registerRequest } = useAuthActions()
    const navigate = useNavigate()
    const { setError } = useForm<RegisterType>()
    const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm<RegisterType>({
        resolver: zodResolver(registerSchema),
        defaultValues: {
            email: "",
            password: "",
            confirmPassword: "",
            firstName: "",
            lastName: "",
            dateOfBirth: "",
            gender: "",
            mobile: "",
            terms: false,
        }
    })

    const onSubmit = async (data: RegisterType) => {
        try {
            await registerRequest(data)
            toast.success("Register success")
            navigate("/login", { replace: true })
        } catch (error: any) {
            if (error.response?.status === 400) {
                setError("email", { message: error.response.data.message })
            }
            toast.error("Register failed")
        }
    }


    return (
        <div className="w-full min-h-full bg-page text-text-primary flex justify-center items-center py-10">
            <div className="bg-surface w-3/5 rounded-lg shadow-md border border-border p-8">

                {/* Logo + Header */}
                <div className="flex flex-col items-center gap-4 mb-8">
                    <div className="size-9 rounded-xl 
                      bg-brand text-white 
                      flex items-center justify-center 
                      font-extrabold text-base shadow-sm">
                        T
                    </div>

                    <h1 className="text-2xl font-bold">
                        Welcome to Backlog
                    </h1>

                    <p className="text-base text-text-secondary">
                        Please register your account
                    </p>
                </div>

                {/* FORM */}
                <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-8">

                    {/*AUTH SECTION */}
                    <div className="grid grid-cols-1 gap-6">

                        <div>
                            <label htmlFor="email"
                                className="form-label">
                                Email
                            </label>
                            <input
                                {...register("email")}
                                type="email"
                                id="email"
                                placeholder="Enter your email"
                                className="form-input"
                            />
                            {errors.email && (
                                <p className="text-danger text-sm mt-2">
                                    {errors.email?.message as string}
                                </p>
                            )}
                        </div>

                        <div>
                            <label htmlFor="password"
                                className="form-label">
                                Password
                            </label>
                            <input
                                {...register("password")}
                                type="password"
                                id="password"
                                placeholder="Enter your password"
                                className="form-input"
                            />
                            {errors.password && (
                                <p className="text-danger text-sm mt-2">
                                    {errors.password?.message as string}
                                </p>
                            )}
                        </div>

                        <div>
                            <label htmlFor="confirmPassword"
                                className="form-label">
                                Confirm Password
                            </label>
                            <input
                                {...register("confirmPassword")}
                                type="password"
                                id="confirmPassword"
                                placeholder="Confirm your password"
                                className="form-input"
                            />
                            {errors.confirmPassword && (
                                <p className="text-danger text-sm mt-2">
                                    {errors.confirmPassword?.message as string}
                                </p>
                            )}
                        </div>
                    </div>

                    {/*INFORMATION */}
                    <div>
                        <h2 className="text-lg font-semibold mb-4 pb-2 border-b border-border">
                            Information
                        </h2>

                        <div className="grid grid-cols-2 gap-6">

                            <div>
                                <label htmlFor="firstName"
                                    className="form-label">
                                    First Name
                                </label>
                                <input
                                    {...register("firstName")}
                                    type="text"
                                    id="firstName"
                                    placeholder="Enter first name"
                                    className="form-input"
                                />
                                {errors.firstName && (
                                    <p className="text-danger text-sm mt-2">
                                        {errors.firstName?.message as string}
                                    </p>
                                )}
                            </div>

                            <div>
                                <label htmlFor="lastName"
                                    className="form-label">
                                    Last Name
                                </label>
                                <input
                                    {...register("lastName")}
                                    type="text"
                                    id="lastName"
                                    placeholder="Enter last name"
                                    className="form-input"
                                />
                                {errors.lastName && (
                                    <p className="text-danger text-sm mt-2">
                                        {errors.lastName?.message as string}
                                    </p>
                                )}
                            </div>

                            <div>
                                <label htmlFor="dateOfBirth"
                                    className="form-label">
                                    Date of Birth
                                </label>
                                <input
                                    {...register("dateOfBirth")}
                                    type="date"
                                    id="dateOfBirth"
                                    className="form-input"
                                />
                                {errors.dateOfBirth && (
                                    <p className="text-danger text-sm mt-2">
                                        {errors.dateOfBirth?.message as string}
                                    </p>
                                )}
                            </div>

                            <div>
                                <label htmlFor="gender"
                                    className="form-label">
                                    Gender
                                </label>
                                <select
                                    {...register("gender")}
                                    id="gender"
                                    className="form-input"
                                >
                                    <option value="">Select gender</option>
                                    <option value="male">Male</option>
                                    <option value="female">Female</option>
                                    <option value="other">Other</option>
                                </select>
                                {errors.gender && (
                                    <p className="text-danger text-sm mt-2">
                                        {errors.gender?.message as string}
                                    </p>
                                )}
                            </div>

                            <div className="col-span-2">
                                <label htmlFor="mobile"
                                    className="form-label">
                                    Phone Number
                                </label>
                                <input {...register("mobile")} type="text" id="mobile" placeholder="Enter phone number"
                                    className="form-input"
                                />
                                {errors.mobile && (
                                    <p className="text-danger text-sm mt-2">
                                        {errors.mobile?.message as string}
                                    </p>
                                )}
                            </div>

                        </div>
                    </div>

                    {/* Submit */}
                    <button
                        disabled={isSubmitting}
                        type="submit"
                        className="custom-btn"
                    >
                        Register
                    </button>
                </form>

                {/* Terms */}
                <div className="flex items-center justify-center gap-2 mt-6 text-text-secondary">
                    <input type="checkbox" id="terms" {...register("terms")} className="h-4 w-4 accent-brand" />
                    <label htmlFor="terms" className="text-sm">
                        I agree to the terms and conditions
                    </label>
                </div>

                {errors.terms && (
                    <p className="text-danger text-sm text-center mt-2">
                        {errors.terms?.message as string}
                    </p>
                )}

                {/* Footer */}
                <div className="flex justify-center mt-6">
                    <p className="text-text-secondary"> Already have an account?{" "}
                        <NavLink to="/login" className="text-brand hover:text-brand-hover font-medium">Login
                        </NavLink>
                    </p>
                </div>

            </div>
        </div>

    )
}

export default RegisterPage
