import { NavLink, Outlet } from "react-router-dom"
import { BellRing, Sun, User } from "lucide-react"




const Layout = () => {
    return (
        <div className="h-screen bg-bg text-text-primary flex">
            <aside className="flex flex-col h-full w-[10%]">
                <div className="flex flex-col gap-2 p-4 border-b border-border mb-2">
                    <div>T</div>
                    <span>Backlog</span>
                </div>
                <nav className="flex flex-col gap-2">
                    <NavLink to="/profile">Profile</NavLink>
                    <NavLink to="/">Tạm</NavLink>
                    <NavLink to="/">Tạm</NavLink>
                    <NavLink to="/">Tạm</NavLink>
                    <div className="flex items-center gap-2 mt-3">
                        <User />
                    </div>
                </nav>
            </aside>
            <main className="flex-1 flex flex-col">
                <header className="flex p-4 border-b border-border">
                    <div className="flex items-center justify-around w-full">
                        <nav className="flex items-center gap-4">
                            <NavLink to="/">Home</NavLink>
                            <NavLink to="/about">About</NavLink>
                            <NavLink to="/faqs">FAQs</NavLink>

                        </nav>
                        <div className="flex items-center gap-4">
                            <Sun />
                            <BellRing />
                        </div>
                    </div>
                </header>
                <div>
                    <Outlet />
                </div>

            </main>
        </div>
    )
}

export default Layout