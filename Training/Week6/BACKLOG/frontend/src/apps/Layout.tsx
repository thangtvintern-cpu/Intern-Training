import { NavLink, Outlet } from "react-router-dom"
import { BellRing, Sun, User } from "lucide-react"




const Layout = () => {
    return (
        <div className="h-screen bg-background text-primary overflow-hidden text-center">
            <div className="p-4 flex w-full">
                <aside className="flex flex-col h-full w-1/6">
                    <div className="gap-2 border-b border-border mb-5 w-full">
                        <div>T</div>
                        <span>Backlog</span>
                    </div>
                    <nav className="flex flex-col gap-2 flex-1">
                        <NavLink to="/profile">Profile</NavLink>
                        <NavLink to="/">Tạm</NavLink>
                        <NavLink to="/">Tạm</NavLink>
                        <NavLink to="/">Tạm</NavLink>
                        <div className="flex items-center gap-2 mt-3">
                            <User />
                        </div>
                    </nav>
                </aside>
                <main className="flex-1 p-4">
                    <header className="flex border-b border-border">
                        <div className="flex items-center w-full justify-center">
                            <nav className="flex justify-center flex-1 gap-4">
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

        </div>
    )
}

export default Layout