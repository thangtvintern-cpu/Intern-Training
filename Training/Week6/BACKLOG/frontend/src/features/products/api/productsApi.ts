import { api } from "../../../lib/api/api"
import type { Category, DeleteProductResponse, Product } from "../types"
import type { UpdateProductType } from "../pages/UpdateProduct"
import type { AddToProductType } from "../pages/AddToProduct"




const baseUrl = "https://dummyjson.com/products"



export const updateProduct = async (product: UpdateProductType, id: number) => {
    try {
        const response = await api.patch<Product>(`${baseUrl}/${id}`, product)
        return response
    } catch (error) {
        throw error
    }
}


export const addProduct = async (product: AddToProductType) => {
    try {
        const response = await api.post<unknown>(`${baseUrl}/add`, product)
        return response
    } catch (error) {
        throw error
    }
}

export const deleteProduct = async (id: number) => {
    try {
        const response = await api.delete<DeleteProductResponse>(`${baseUrl}/${id}`)
        return response
    } catch (error) {
        throw error
    }
}


export const getAllCategories = async () => {
    try {
        const response = await api.get<Category[]>(`${baseUrl}/categories`)
        return response.map(cate => cate.name)
    } catch (error) {
        throw error
    }
}