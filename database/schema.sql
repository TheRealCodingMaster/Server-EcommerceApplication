-- Schema for Ecommerce App Database

-- Table for storing products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT
);

-- Table for storing users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing orders
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    total_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing order items
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL
);

-- Example data for products
INSERT INTO products (name, price, description) VALUES
    ('Product A', 19.99, 'Description for Product A'),
    ('Product B', 29.99, 'Description for Product B'),
    ('Product C', 39.99, 'Description for Product C');

-- Example data for users
INSERT INTO users (username, password_hash, email) VALUES
    ('user1', 'hashed_password1', 'user1@example.com'),
    ('user2', 'hashed_password2', 'user2@example.com');
