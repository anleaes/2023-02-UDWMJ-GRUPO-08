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

class Order{
    total_price  
    status  
    client: Client
}

class Client{
    first_name  
    last_name  
    address  
    cell_phone  
    email  
    gender  
}
