import { useEffect, useState } from "react"
import { api } from "../../../lib/api/api"
import type { PaginationProps, PaginationResponse } from "../types"


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
