import { Outlet } from "react-router-dom"

import SideBar from "./components/SideBar";
import Header from "./components/Header";


const Layout = () => {



    return (

        <div className="flex min-h-screen bg-page text-text-primary font-sans">

            {/* Sidebar */}
            <SideBar />
            {/*  Main */}
            <main className="flex-1 min-w-0 flex flex-col transition-all duration-200">
                {/* Header */}

                <Header />

                {/* Page Content */}
                <div className="flex-1 p-6 flex items-center justify-center">
                    <Outlet />
                </div>
            </main>
        </div>

    )
}

export default Layout