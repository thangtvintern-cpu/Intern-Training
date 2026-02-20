import { BellRing, Sun } from "lucide-react"
import { NavLink } from "react-router-dom"
import { useAuth } from "../../features/auth";




const Header = () => {

    const { status } = useAuth();

    return (
        <header className="
      sticky top-0 z-10
      bg-surface/80 backdrop-blur-sm
      border-b border-border
      px-6 py-3
    ">
            <div className="flex items-center gap-6">

                {/* Top Nav */}
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
                                `
                px-3 py-1.5 rounded-md text-sm font-medium
                transition-colors
                ${isActive
                                    ? "bg-surface-hover text-text-primary"
                                    : "text-text-secondary hover:text-text-primary hover:bg-surface-hover"
                                }
              `
                            }
                        >
                            {link.label}
                        </NavLink>
                    ))}
                </nav>

                {/* Search */}
                <div className="flex-1 max-w-2/5 shrink-0 m-auto">
                    <input
                        type="text"
                        placeholder="Search your training..."
                        className="
              w-full px-3 py-1.5 text-sm rounded-lg
              bg-surface-muted
              border border-border
              text-text-primary
              placeholder:text-text-muted
              focus:outline-none
              focus:ring-2
              focus:ring-brand
              transition
            "
                    />
                </div>

                {/* Auth buttons */}
                {status !== "authenticated" && (
                    <nav className="flex items-center gap-1 shrink-0">
                        <NavLink
                            to="/login"
                            className="
                px-3 py-1.5 text-sm font-medium rounded-md
                text-text-secondary
                hover:text-text-primary
                hover:bg-surface-hover
                transition-colors
              "
                        >
                            Login
                        </NavLink>

                        <NavLink
                            to="/register"
                            className="
                px-3 py-1.5 text-sm font-medium rounded-md
                text-white
                bg-brand
                hover:bg-brand-hover
                transition-colors
              "
                        >
                            Register
                        </NavLink>
                    </nav>
                )}

                {/* Right icons */}
                <div className="flex items-center gap-3 ml-auto shrink-0">

                    <button
                        onClick={() =>
                            document.documentElement.classList.toggle("dark")
                        }
                        className="
              size-8 flex items-center justify-center
              rounded-md bg-transparent border-none
              text-text-secondary
              hover:bg-surface-hover hover:text-text-primary
              transition-colors
            "
                    >
                        <Sun className="size-6" />
                    </button>

                    <button
                        className="
              size-8 flex items-center justify-center
              rounded-md bg-transparent border-none
              text-text-secondary
              hover:bg-surface-hover hover:text-text-primary
              transition-colors
            "
                    >
                        <BellRing className="size-6" />
                    </button>

                </div>
            </div>
        </header>
    )
}


export default Header
