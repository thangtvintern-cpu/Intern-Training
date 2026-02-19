import { useState } from "react"
import usePagination from "../../shared/hooks/usePagination"
import { NavLink } from "react-router-dom"
import toast from "react-hot-toast"



const HomePage = () => {
    const [skip, setSkip] = useState(0)
    const [limit, setLimit] = useState(10)
    const { data, loading, error } = usePagination({ props: { limit: limit, skip: skip } })
    const [selectedProduct, setSelectedProduct] = useState<number | null>(null)

    const handleUpdate = (e: React.MouseEvent) => {
        e.stopPropagation()
        setSelectedProduct(null)
        toast.success("Product updated successfully")
    }

    return (
        <>
            {loading ? (
                <p className="text-center text-5xl font-extrabold bg-indigo-500">Loading...</p>
            ) : error ? (
                <p className="text-center text-5xl font-extrabold bg-red-500">Error: {error}</p>
            ) :
                (<div className="relative">
                    <div className="mb-6 flex justify-between">
                        <h1 className="text-2xl font-bold">Products</h1>
                        <NavLink to="/add-product" className="px-4 py-2 rounded-lg bg-indigo-500 text-white">
                            Add Product
                        </NavLink>
                    </div>
                    <div className="">

                        <ul className="flex flex-wrap gap-4">
                            {data?.products?.map((product) => (
                                <li key={product.id} className="relative hover:scale-105 transition-all duration-300"
                                    onClick={() => setSelectedProduct(product.id)}>
                                    <p className="absolute top-0 right-0 bg-red-500 text-white px-2 py-1 rounded-lg">{product.discountPercentage}%</p>
                                    <div className="flex flex-col gap-2 rounded-lg border p-4">
                                        <div className="w-40 h-40overflow-hidden">
                                            <img src={product.images[0]} alt={product.title} className="aspect-square object-cover" />
                                        </div>
                                        <h1 className="text-lg font-bold line-clamp-2">{product.title}</h1>
                                        <p className="text-sm text-gray-500">{product.price}</p>
                                    </div>
                                    {selectedProduct === product.id && (
                                        <div className="absolute top-0 left-0 w-full h-full flex flex-col justify-center items-center bg-white rounded-lg shadow-lg">
                                            <div className="p-4 ">
                                                <h1 className="text-lg font-bold">{product.title}</h1>
                                                <p className="text-sm text-gray-500">{product.price}</p>

                                            </div>
                                            <div className="flex gap-2">
                                                <button className="mt-4 px-4 py-2 rounded-lg bg-indigo-500 text-white" onClick={(e) => handleUpdate(e)}>Update</button>
                                                <button onClick={(e) => { e.stopPropagation(); setSelectedProduct(null) }} className="mt-4 px-4 py-2 rounded-lg bg-indigo-500 text-white">Close</button>
                                            </div>
                                        </div>
                                    )}
                                </li>
                            ))}
                        </ul>

                    </div>
                    <div className="flex gap-4 mt-6 justify-center">
                        <button onClick={() => setSkip(skip - limit)} className="px-4 py-2 rounded-lg bg-indigo-500 text-white">Previous</button>
                        <button onClick={() => setSkip(skip + limit)} className="px-4 py-2 rounded-lg bg-indigo-500 text-white">Next</button>
                    </div>

                </div>
                )
            }
        </>

    )
}

export default HomePage