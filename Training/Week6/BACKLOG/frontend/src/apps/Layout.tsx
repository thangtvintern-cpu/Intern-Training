import { NavLink, Outlet } from "react-router-dom"
import { BellRing, Sun, User } from "lucide-react"

const navItems = [
    { to: "/", label: "Profile", icon: <User /> },
    { to: "/", label: "Tạm", icon: <BellRing /> },
    { to: "/", label: "Tạm", icon: <Sun /> },
    { to: "/", label: "Tạm", icon: <User /> },
]


const Layout = () => {



    return (
        <div className="flex min-h-screen bg-gray-50 font-sans text-black">


            <aside className="fixed inset-y-0 left-0 z-20 w-64 flex flex-col bg-white border-r border-gray-200 px-4 py-6">

                {/* logo */}
                <div className="flex items-center gap-3 px-2 mb-8">
                    <div className="size-9 shrink-0 rounded-xl bg-gradient-to-br from-indigo-500 to-indigo-400 flex items-center justify-center text-white font-extrabold text-base shadow-md shadow-indigo-200">
                        T
                    </div>
                    <span className="text-xl font-bold tracking-tight text-gray-900">Backlog</span>
                </div>

                {/* menu */}
                <p className="px-3 mb-2 text-[0.65rem] font-semibold uppercase tracking-widest text-gray-400">
                    Menu
                </p>
                <nav className="flex flex-col gap-1 flex-1">
                    {navItems.map((item) => (
                        <NavLink
                            to={item.to}
                            key={item.label}
                            className={({ isActive }) =>
                                `flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium no-underline transition-colors duration-150
            ${isActive
                                    ? "bg-indigo-50 text-indigo-600 font-semibold"
                                    : "text-gray-500 hover:bg-gray-100 hover:text-gray-800"
                                }`
                            }
                        >
                            <span className="text-base leading-none">{item.icon}</span>
                            {item.label}
                        </NavLink>
                    ))}
                </nav>

                {/* user */}
                <div className="pt-4 border-t border-gray-200">
                    <div className="flex items-center gap-3 px-2">
                        <div className="size-9 shrink-0 rounded-full bg-gray-200 flex items-center justify-center">
                            <User className="size-4 text-gray-500" />
                        </div>
                        <div className="flex-1 min-w-0">
                            <p className="text-sm font-semibold text-gray-800 truncate">User</p>
                            <p className="text-xs text-gray-400 capitalize">Admin</p>
                        </div>
                        <button className="size-8 shrink-0 flex items-center justify-center rounded-lg border-none bg-transparent text-gray-400 cursor-pointer transition-colors hover:bg-red-50 hover:text-red-500">
                            ↪
                        </button>
                    </div>
                </div>

            </aside>

            {/* main */}
            <main className="flex-1 ml-64 min-w-0 flex flex-col">
                <header className="sticky top-0 z-10 bg-white/80 backdrop-blur-sm border-b border-gray-200 px-6 py-3">
                    <div className="flex items-center gap-6">

                        {/* menu */}
                        <nav className="flex items-center gap-1 shrink-0">
                            {[
                                { to: "/", label: "Home" },
                                { to: "/about", label: "About" },
                                { to: "/contact", label: "Contact" },
                            ].map((link) => (
                                <NavLink
                                    key={link.label}
                                    to={link.to}
                                    className={({ isActive }) =>
                                        `px-3 py-1.5 rounded-md text-sm font-medium no-underline transition-colors
                                        ${isActive
                                            ? "bg-gray-100 text-gray-900"
                                            : "text-gray-500 hover:text-gray-800 hover:bg-gray-50"
                                        }`
                                    }
                                >
                                    {link.label}
                                </NavLink>
                            ))}
                        </nav>

                        {/* search */}
                        <div className="flex-1 max-w-2/5 shrink-0 m-auto">
                            <input
                                type="text"
                                placeholder="Search your training..."
                                className="w-full px-3 py-1.5 text-sm border border-gray-200 rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-300 focus:border-transparent transition"
                            />
                        </div>
                        <nav className="flex items-center gap-1 shrink-0">
                            <NavLink
                                to="/login"
                                className="px-3 py-1.5 text-sm font-medium text-gray-600 hover:text-gray-900 no-underline rounded-md hover:bg-gray-100 transition-colors"
                            >
                                Login
                            </NavLink>
                            <NavLink
                                to="/register"
                                className="px-3 py-1.5 text-sm font-medium text-white bg-indigo-500 hover:bg-indigo-600 no-underline rounded-md transition-colors"
                            >
                                Register
                            </NavLink>
                        </nav>
                        {/* user */}
                        <div className="flex items-center gap-3 ml-auto shrink-0">

                            <button onClick={() => { document.documentElement.classList.toggle("dark") }} className="size-8 flex items-center justify-center rounded-md text-gray-500 hover:bg-gray-100 hover:text-gray-800 transition-colors border-none bg-transparent cursor-pointer">
                                <Sun className="size-6" />
                            </button>
                            <button className="size-8 flex items-center justify-center rounded-md text-gray-500 hover:bg-gray-100 hover:text-gray-800 transition-colors border-none bg-transparent cursor-pointer">
                                <BellRing className="size-6" />
                            </button>
                        </div>

                    </div>
                </header>

                {/* Page content */}
                <div className="flex-1 p-6 flex items-center justify-center">
                    <Outlet />
                </div>

            </main>
        </div>
    )
}

export default Layout