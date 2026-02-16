import { RouterProvider } from "react-router-dom";
import { Toaster } from "react-hot-toast";
import { route } from "./router";
import { AuthProvider } from "../features/auth";



export default function AppProviders(){

    return (
        <AuthProvider>
        <RouterProvider router={route}/>
        <Toaster position="bottom-right" 
        toastOptions={{
            duration: 3000,
            style: {
                background: "#1e1e1e",
                color: "#fff",
                border: "1px solid #333",
            },
            success:{
                icon: "✅",
                iconTheme:{
                    primary: "#22c55e",
                    secondary: "#fff"
                }
            },
            error:{
                icon: "❌",
                iconTheme:{
                    primary: "#ef4444",
                    secondary: "#fff"
                }
            },
            loading:{
                icon: "⏳",
                iconTheme:{
                    primary: "#6366f1",
                    secondary: "#fff"
                }
            },
        }}
        />
        </AuthProvider>
    )
}