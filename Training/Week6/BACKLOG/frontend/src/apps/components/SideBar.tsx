import { BellRing, Sun, User, Box, ArrowRightFromLine, ArrowLeftFromLine } from "lucide-react"
import { Link, NavLink } from "react-router-dom"
import { useAuth } from "../../features/auth";
import { useState } from "react";

const navItems = [
    { to: "/products", label: "products", icon: <Box /> },
    { to: "/temporary", label: "Tạm", icon: <BellRing /> },
    { to: "/temporary", label: "Tạm", icon: <Sun /> },
    { to: "/temporary", label: "Tạm", icon: <User /> },
]




const SideBar = () => {
    const { user, logout, status } = useAuth();
    const [menuOpen, setMenuOpen] = useState<boolean>(true)
    const [userModel, setUserModel] = useState<boolean>(false)


    return (
        <aside className={`z-20 flex flex-col shrink-0 text-text-secondary transition-all duration-300 ${menuOpen ? "w-56" : "w-16"} bg-surface border-r border-border px-4 py-6`}>

            {/* Logo */}
            <div className="flex items-center justify-around gap-3 mb-8 shrink-0 w-full">
                {menuOpen && (<><div className="size-9 shrink-0 rounded-xl   bg-brand text-white flex items-center justify-center font-extrabold text-base shadow-md">
                    T
                </div>
                    <span className="text-xl font-bold tracking-tight">
                        Backlog
                    </span></>)}
                {menuOpen ? <button className="shrink-0" onClick={() => setMenuOpen(!menuOpen)}>
                    <ArrowLeftFromLine />
                </button> : <button className="shrink-0" onClick={() => setMenuOpen(!menuOpen)}>
                    <ArrowRightFromLine />
                </button>}


            </div>

            {/* Menu title */}
            <p className="mb-2 text-xs font-semibold uppercase tracking-widest text-text-muted">
                Menu
            </p>

            {/* Menu */}
            <nav className="flex flex-col gap-1 flex-1">
                {navItems.map((item) => (
                    <NavLink
                        to={item.to}
                        key={item.label}
                        className={({ isActive }) => `flex items-center ${!menuOpen && "justify-center"} gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors
                                ${isActive
                                ? "bg-brand-soft text-brand font-semibold"
                                : "text-text-secondary hover:bg-surface-hover hover:text-text-primary"
                            }
          `
                        }
                    >
                        <span className="text-base leading-none shrink-0">{item.icon}</span>
                        {menuOpen && <span>{item.label}</span>}
                    </NavLink>
                ))}
            </nav>

            {/* User section */}
            <div className="pt-4 border-t border-border mx-auto w-full relative">
                <div className="flex gap-3">
                    <div className="size-9 shrink-0 rounded-full bg-surface-hover flex justify-center items-center mr-auto">
                        <User className="size-6" onClick={() => setUserModel(!userModel)} />
                    </div>

                    {status === "authenticated" && (
                        <div className="flex-1 min-w-0">
                            <p className="text-sm font-semibold truncate">
                                Hi,
                            </p>
                            <p className="text-xs text-text-muted capitalize">
                                {user?.firstName}
                            </p>
                        </div>
                    )}
                    {userModel && <div className="absolutely right-[-6] border-border border-2 flex flex-col items-center">
                        <button onClick={() => logout()}>Logout</button>
                    </div>}
                    {status === "authenticated" && (
                        <button
                            onClick={logout}
                            className="
            size-8 shrink-0 flex items-center justify-center
              rounded-lg bg-transparent border-none
              text-text-muted
              hover:bg-danger-soft hover:text-danger
              transition-colors
            "
                        >
                            ↪
                        </button>
                    )}
                </div>
            </div>

        </aside>
    )

}


export default SideBar