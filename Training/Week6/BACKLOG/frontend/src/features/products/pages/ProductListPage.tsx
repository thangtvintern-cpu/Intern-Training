import { useEffect, useRef, useState } from "react"
import ErrorPage from "../../../pages/error/ErrorPage"
import usePagination from "../hooks/usePagination"
import UpdateProduct from "./UpdateProduct"
import type { Product } from "../types"
import { getAllCategories } from "../api/productsApi"
import AddToProduct from "./AddToProduct"
import LoadingPage from "../../../pages/common/LoadingPage"



const ProductList = () => {

    return (
        <div>

        </div>
    )
}



const ProductListPage = () => {
    const [skip, setSkip] = useState(0)
    const [limit, setLimit] = useState(15)
    const { data, loading, error } = usePagination({ props: { limit: limit, skip: skip } })
    const [selectedProduct, setSelectedProduct] = useState<Product | null>(null)
    const modalRef = useRef<HTMLDivElement>(null)
    const [categories, setCategories] = useState<string[] | null>(null)
    const [isAddProductOpen, setIsAddProductOpen] = useState(false)

    useEffect(() => {
        const loadCategories = async () => {
            const categories = await getAllCategories()
            setCategories(categories)
        }
        loadCategories()
    }, [])

    const handleOutsideClick = (e: React.MouseEvent) => {
        if (modalRef.current && !modalRef.current.contains(e.target as Node)) {
            setSelectedProduct(null)
            setIsAddProductOpen(false)
        }
    }


    const handleOpenModal = () => {
        setIsAddProductOpen(false)
        setSelectedProduct(null)
    }

    return (
        <>
            {loading ? <LoadingPage /> :
                error ? <ErrorPage />
                    : (<div className="relative">
                        <div className="mb-6 flex justify-between">
                            <h1 className="text-2xl font-bold text-text-primary">Products</h1>
                            <button onClick={() => setIsAddProductOpen(true)} className="px-4 py-2 rounded-lg bg-brand hover:bg-brand-hover text-white transition">
                                Add Product
                            </button>
                        </div>
                        <div className="flex justify-center items-center">
                            <ul className="flex flex-wrap gap-4 justify-center items-center">
                                {data?.products?.map((product) => (
                                    <li key={product.id} className="relative hover:scale-105 transition-all duration-300 ease-in-out"
                                        onClick={() => setSelectedProduct(product)}>
                                        <p className="absolute top-0 right-0 bg-danger text-white px-2 py-1 rounded-lg">
                                            {product.discountPercentage}%
                                        </p>
                                        <div className="flex flex-col gap-2 rounded-lg border border-border bg-surface p-4 w-50 h-80">
                                            <div className="overflow-hidden">
                                                <img src={product.images[0]} alt={product.title} className="aspect-square object-cover" />
                                            </div>
                                            <h1 className="text-lg font-bold text-text-primary line-clamp-2">
                                                {product.title}
                                            </h1>
                                            <p className="text-sm text-text-secondary">
                                                {product.price}
                                            </p>
                                        </div>
                                    </li>

                                ))}
                            </ul>

                        </div>
                        <div className="flex gap-4 mt-6 justify-center">
                            <button
                                onClick={() => setSkip(skip - limit)}
                                className="px-4 py-2 rounded-lg bg-brand hover:bg-brand-hover text-white transition"
                            >
                                Previous
                            </button>
                            <button
                                onClick={() => setSkip(skip + limit)}
                                className="px-4 py-2 rounded-lg bg-brand hover:bg-brand-hover text-white transition"
                            >
                                Next
                            </button>
                        </div>
                        {selectedProduct && (
                            <div onClick={handleOutsideClick} className="fixed inset-0 bg-black/50 z-40 flex items-center justify-center">
                                <div ref={modalRef} className="fixed right-0 p-4 top-0 bottom-0 w-1/3 flex justify-center items-center z-50 bg-surface rounded-lg shadow-lg">
                                    <UpdateProduct product={selectedProduct} categories={categories} onToggle={handleOpenModal} />
                                </div>
                            </div>
                        )}
                        {isAddProductOpen && (
                            <div onClick={handleOutsideClick} className="fixed inset-0 bg-black/50 z-40 flex items-center justify-center">
                                <div ref={modalRef} className="fixed right-0 p-4 top-0 bottom-0 w-1/3 flex justify-center items-center z-50 bg-surface rounded-lg shadow-lg">
                                    <AddToProduct onToggle={handleOpenModal} categories={categories} />
                                </div>
                            </div>
                        )}

                    </div>
                    )
            }

        </>

    )
}

export default ProductListPage