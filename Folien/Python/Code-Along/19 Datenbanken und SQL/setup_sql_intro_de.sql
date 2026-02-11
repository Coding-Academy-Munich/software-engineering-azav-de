-- Setup script for SQL Intro slides
-- Creates and populates the customers, products, and orders tables
-- Compatible with SQLite

-- ============================================================
-- Table creation
-- ============================================================

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- ============================================================
-- Customers (5)
-- ============================================================

INSERT INTO customers (name, address) VALUES ('John Smith', '123 Elm St');
INSERT INTO customers (name, address) VALUES ('Jane Doe', '456 Oak St');
INSERT INTO customers (name, address) VALUES ('David Parker', '587 Oak St');
INSERT INTO customers (name, address) VALUES ('Emma Wilson', '123 Maple Ave');
INSERT INTO customers (name, address) VALUES ('Charlie Brown', '456 Pine St');

-- ============================================================
-- Products (5)
-- ============================================================

INSERT INTO products (id, product_name, price, description)
    VALUES (346, 'Kichererbsen', 0.59, 'Gesunde Kichererbsen');
INSERT INTO products (id, product_name, price, description)
    VALUES (2341, 'Tomatensuppe', 1.99, 'Leckere Tomatensuppe');
INSERT INTO products (id, product_name, price, description)
    VALUES (939504, 'Tomatensuppe', 2.49, 'Premium Tomatensuppe');
INSERT INTO products (id, product_name, price)
    VALUES (939505, 'Thunfisch', 19.99);
INSERT INTO products (id, product_name, price)
    VALUES (939506, 'Frischer Lachs', 29.99);

-- ============================================================
-- Orders (10)
-- ============================================================

INSERT INTO orders (customer_id, product_id, quantity) VALUES (1, 2341, 2);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (2, 939504, 1);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (1, 346, 3);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (1, 2341, 2);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (3, 939505, 1);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (4, 939506, 2);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (2, 939505, 3);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (3, 346, 5);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (4, 2341, 1);
INSERT INTO orders (customer_id, product_id, quantity) VALUES (1, 939506, 1);
