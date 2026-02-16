import { RouterProvider } from "react-router-dom";
import { Toaster } from "react-hot-toast";
import { route } from "./router";



export default function AppProviders(){

    return (
        <>
        <RouterProvider router={route}/>
        <Toaster/>
        </>
    )
}