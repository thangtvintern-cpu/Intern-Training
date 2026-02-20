import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import toast from "react-hot-toast"
import z from "zod"
import { addProduct } from "../api/productsApi"
import { Spinner } from "../../../pages/common/Spinner"

const addToProductSchema = z.object({
    title: z.string().min(3, "Title must be at least 3 characters long"),
    description: z.string().min(10, "Description must be at least 10 characters long"),
    price: z.number().min(1, "Price must be at least 1"),
    stock: z.number().min(1, "Stock must be at least 1"),
    category: z.string().min(1, "Category must be at least 1 characters long"),
    brand: z.string().min(3, "Brand must be at least 3 characters long"),
    discountPercentage: z.number().min(1, "Discount percentage must be at least 1").max(100, "Discount percentage must be at most 100"),
})

export type AddToProductType = z.infer<typeof addToProductSchema>

interface AddToProducProps {
    onToggle: () => void
    categories: string[] | null
}
const AddToProduct = ({ onToggle, categories }: AddToProducProps) => {
    const { register, handleSubmit, formState: { errors, isSubmitting }, setError } = useForm<AddToProductType>({
        resolver: zodResolver(addToProductSchema),
        defaultValues: {
            title: "",
            description: "",
            price: 0,
            stock: 0,
            category: "",
            brand: "",
            discountPercentage: 0,
        }
    })

    const onSubmit = async (data: AddToProductType) => {
        try {
            await addProduct(data)
            onToggle()
            toast.success("Product added successfully")

        } catch (error) {
            toast.error("Failed to add product")
            setError("title", { type: "manual", message: "Failed to add product" })
        }
    }

    return (
        <div className="size-full flex flex-col p-4">
            <h1 className="text-2xl font-bold text-text-primary border-b border-border pb-2 mb-4">Create Product</h1>
            <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-4 ">
                <div className="flex flex-col gap-2">
                    <label htmlFor="title" className="form-label">Title</label>
                    <input type="text" id="title" className="form-input" {...register("title")} />
                    {errors.title && <p className="text-red-500">{errors.title.message}</p>}
                </div>
                <div className="flex flex-col gap-2">
                    <label htmlFor="description" className="form-label">Description</label>
                    <textarea id="description" {...register("description")} className="form-input min-h-[150px] resize-y"></textarea>
                    {errors.description && <p className="text-red-500">{errors.description.message}</p>}
                </div>
                <div className="flex justify-between items-center gap-2">
                    <div className="flex flex-col gap-1">
                        <label htmlFor="price" className="form-label">Price</label>
                        <input type="number" id="price" {...register("price", { valueAsNumber: true })} className="w-2/3 form-input" />
                        {errors.price && <p className="text-red-500">{errors.price.message}</p>}
                    </div>
                    <div className="flex flex-col gap-1">
                        <label htmlFor="stock" className="form-label">Stock</label>
                        <input type="number" id="stock" {...register("stock", { valueAsNumber: true })} className="w-2/3 form-input" />
                        {errors.stock && <p className="text-red-500">{errors.stock.message}</p>}
                    </div>
                    <div className="flex flex-col gap-1">
                        <label htmlFor="brand" className="form-label">Brand</label>
                        <input type="text" id="brand" {...register("brand")} className="w-2/3 form-input" />
                        {errors.brand && <p className="text-red-500">{errors.brand.message}</p>}
                    </div>

                </div>

                <div className="flex justify-between items-center gap-2">
                    <div className="flex flex-col gap-1">
                        <label htmlFor="category" className="form-label">Category</label>
                        <select id="category" {...register("category")} className="form-input">
                            {categories?.map((category) => (
                                <option key={category} value={category} className="form-input">
                                    {category}
                                </option>
                            ))}
                        </select>
                        {errors.category && <p className="text-red-500">{errors.category.message}</p>}
                    </div>
                    <div className="flex flex-col gap-1">
                        <label htmlFor="discountPercentage" className="form-label">Discount Percentage</label>
                        <input type="number" id="discountPercentage" {...register("discountPercentage", { valueAsNumber: true, min: 0, max: 100 })} className="form-input" />
                        {errors.discountPercentage && <p className="text-red-500">{errors.discountPercentage.message}</p>}
                    </div>
                </div>
                <div className="flex flex-col gap-2">

                </div>

            </form>
            <button className="custom-btn mt-auto" type="submit" disabled={isSubmitting} onClick={handleSubmit(onSubmit)}>
                {isSubmitting ? <Spinner className="size-6" /> : "Create"}
            </button>

        </div>
    )
}

export default AddToProduct