


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

export interface DeleteProductResponse {
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
    isDeleted: boolean;
    deletedOn: string;
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


export interface Category {
    slugs: string
    name: string
    url: string
}

