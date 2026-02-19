import { useEffect, useState } from "react"
import { api } from "../../lib/api/api"

export interface Product {
    id: number;
    title: string;
    price: number;
    brand: string;
    category: string;
    discountPercentage: number;
    description: string;
    images: string[];
    rating: number;
    stock: number;
    thumbnail: string;
}

export interface PaginationProps {
    limit: number;
    skip: number;
    total?: number;
}
export interface PaginationResponse {
    products: Product[];
    pagination: PaginationProps;
}

const usePagination = ({ props }: { props: PaginationProps }) => {
    const { limit, skip } = props
    const [data, setData] = useState<PaginationResponse | null>(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<boolean>(false)
    useEffect(() => {
        const getProducts = async () => {
            try {
                setLoading(true)
                const response = await api.get(`https://dummyjson.com/products?limit=${limit}&skip=${skip}`)
                setData(response as PaginationResponse)
            } catch (error) {
                setError(true)
            } finally {
                setLoading(false)
            }
        }
        getProducts()   
    }, [limit, skip])

    return { data, loading, error }

}

export default usePagination
