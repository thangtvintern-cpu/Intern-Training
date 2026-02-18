
import { AuthProvider } from "../features/auth";
import AppInitial from "./AppInitial";
import Layout from "./Layout";




export default function AppProviders() {

    return (
        <AuthProvider>
            <AppInitial>
                <Layout />
            </AppInitial>
        </AuthProvider>
    )
}