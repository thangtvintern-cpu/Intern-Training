import { createBrowserRouter } from "react-router-dom";
import PublicRoute from "../features/auth/components/PublicRoute";
import LoginPage from "../features/auth/components/LoginPage";
import RegisterPage from "../features/auth/components/RegisterPage";
import PrivateRoute from "../features/auth/components/PrivateRoute";
import UserProfilePage from "../pages/private/UserProfilePage";
import HomePage from "../pages/public/HomePage";
import AboutPage from "../pages/public/AboutPage";
import FAQsPage from "../pages/public/FAQsPage";
import RoleGuard from "../features/auth/components/RoleGuard";
import AdminPage from "../pages/private/admin/AdminPage";
import AppProviders from "./components/AppProviders";
import AddToProduct from "../features/products/pages/AddToProduct";
import ContactPage from "../pages/public/Contact";
import ProductListPage from "../features/products/pages/ProductListPage";





export const route = createBrowserRouter([
    {
        element: <AppProviders />,
        children: [
            // không yêu cầu đăng nhập
            { element: <HomePage />, path: "/", index: true },
            { element: <AboutPage />, path: "/about" },
            { element: <FAQsPage />, path: "/faqs" },
            { element: <AddToProduct />, path: "/add-product" },
            { element: <ContactPage />, path: "/contact" },
            { element: <ProductListPage />, path: "/products" },

            //  không cho phép truy cập vào route này khi đã đăng nhập rồi
            {
                element: <PublicRoute />,
                children: [
                    { element: <LoginPage />, path: "/login" },
                    { element: <RegisterPage />, path: "/register" },
                ]
            },


            // yêu cầu phải đăng nhập mới được truy cập vào route này
            {
                element: <PrivateRoute />,
                children: [
                    // for user
                    { element: <UserProfilePage />, path: "/profile" },






                    // for admin
                    {
                        element: <RoleGuard allowedRoles={['admin']} />,
                        children: [
                            { element: <AdminPage />, path: "/admin" },

                        ]

                    }
                ]
            },

        ],
    },
])