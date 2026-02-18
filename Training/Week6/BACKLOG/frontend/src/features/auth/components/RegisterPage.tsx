import { NavLink } from "react-router-dom"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import { useAuthActions } from "../context/AuthContext"

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
        await registerRequest(data)
    }


    return (
        <div className="w-full h-full text-gray-500 flex justify-center items-center">
            <div className="bg-transparent w-3/5 rounded-lg shadow-lg p-8">
                <div className="flex flex-col items-center gap-4 mb-4">
                    <div className="size-9 shrink-0 rounded-xl bg-linear-to-br from-indigo-500 to-indigo-400 flex items-center justify-center text-white font-extrabold text-base shadow-md shadow-indigo-200">
                        T
                    </div>
                    <h1 className="text-2xl font-bold text-black">Welcome to Backlog</h1>
                    <p className="text-base text-gray-400">Please register your account</p>
                </div>
                <div>
                    <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-6">
                        <div>
                            <label htmlFor="email" className="text-sm font-bold mb-2 inline-block">Email</label>
                            <input {...register("email")} placeholder="Enter your email" type="email" id="email" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
                            <p className="text-red-500 text-sm mt-2">{errors.email?.message as string}</p>
                        </div>
                        <div >
                            <label htmlFor="password" className="text-sm font-bold mb-2 inline-block">Password</label>
                            <input {...register("password")} placeholder="Enter your password" type="password" id="password" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
                            <p className="text-red-500 text-sm mt-2">{errors.password?.message as string}</p>
                        </div>
                        <div>
                            <label htmlFor="confirmPassword" className="text-sm font-bold mb-2 inline-block">Confirm Password</label>
                            <input {...register("confirmPassword")} placeholder="Enter your confirm password" type="password" id="confirmPassword" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
                            <p className="text-red-500 text-sm mt-2">{errors.confirmPassword?.message as string}</p>
                        </div>
                        <div className="">
                            <h2 className="text-xl font-bold mb-2 border-b border-gray-500 pb-2">Information</h2>
                            <div className="grid grid-cols-2 gap-2">
                                <div className="col-span-1">
                                    <label htmlFor="firstName" className="text-sm font-bold mb-2 inline-block">First Name</label>
                                    <input {...register("firstName")} placeholder="Enter your first name" type="text" id="firstName" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
                                    <p className="text-red-500 text-sm mt-2">{errors.firstName?.message as string}</p>
                                </div>
                                <div className="col-span-1">
                                    <label htmlFor="lastName" className="text-sm font-bold mb-2 inline-block">Last Name</label>
                                    <input {...register("lastName")} placeholder="Enter your last name" type="text" id="lastName" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
                                    <p className="text-red-500 text-sm mt-2">{errors.lastName?.message as string}</p>
                                </div>
                                <div className="col-span-1">
                                    <label htmlFor="dateOfBirth" className="text-sm font-bold mb-2 inline-block">Date of Birth</label>
                                    <input {...register("dateOfBirth")} placeholder="Enter your date of birth" type="date" id="dateOfBirth" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
                                    <p className="text-red-500 text-sm mt-2">{errors.dateOfBirth?.message as string}</p>
                                </div>
                                <div className="col-span-1">
                                    <label htmlFor="gender" className="text-sm font-bold mb-2 inline-block">Gender</label>
                                    <select {...register("gender")} id="gender" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition">
                                        <option value="">Select gender</option>
                                        <option value="male">Male</option>
                                        <option value="female">Female</option>
                                        <option value="other">Other</option>
                                    </select>
                                    <p className="text-red-500 text-sm mt-2">{errors.gender?.message as string}</p>
                                </div>
                                <div className="col-span-2">
                                    <label htmlFor="mobile" className="text-sm font-bold mb-2 inline-block">Phone Number</label>
                                    <input {...register("mobile")} placeholder="Enter your phone number" type="text" id="mobile" className="w-full px-3 py-2.5 placeholder:text-gray-400 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition" />
                                    <p className="text-red-500 text-sm mt-2">{errors.mobile?.message as string}</p>
                                </div>



                            </div>
                        </div>
                        <button disabled={isSubmitting} type="submit" className="w-full px-3 py-2.5 text-base font-bold bg-indigo-500 hover:bg-indigo-600 no-underline rounded-md transition-colors text-black">Register</button>
                    </form>
                </div>
                <div className="flex justify-center items-center mt-6 gap-2">
                    <input type="checkbox" id="terms" className="h-4 w-4" {...register("terms")} />
                    <label htmlFor="terms" className="text-base font-bold text-gray-500 inline-block">I agree to the terms and conditions</label>
                    <p className="text-red-500 text-sm mt-2">{errors.terms?.message as string}</p>
                </div>
                <div className="flex justify-center items-center mt-6">
                    <p className="text-base text-gray-400">If you have an account? <NavLink to="/login" className="text-indigo-500 hover:text-indigo-600 no-underline">Login</NavLink></p>
                </div>
            </div>
        </div>
    )
}

export default RegisterPage
