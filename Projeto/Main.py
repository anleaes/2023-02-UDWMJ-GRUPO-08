@startuml

class Category{
    id
    name
    description
}

class Product{
    name
    description  
    date_fabrication  
    is_active  
    category: Category
}

class OrderItem{
    quantity  
    unitary_price  
    order: Order
    product: Product
}
