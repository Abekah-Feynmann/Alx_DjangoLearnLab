CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;

CREATE TABLE Authors(
    author_id INT AUTO_INCREMENT,
    author_name VARCHAR(215), 

    PRIMARY KEY (author_id)
);


CREATE TABLE Books(
    book_id INT AUTO_INCREMENT, 
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE,
    publication_date DATE, 

    PRIMARY KEY (book_id),

    CONSTRAINT fk_books_authors
        FOREIGN KEY (author_id)
        REFERENCES Authors(author_id)

);

CREATE TABLE Customers(
    customer_id INT AUTO_INCREMENT,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT,

    PRIMARY KEY (customer_id)
);


CREATE TABLE Orders(
    order_id INT AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,

    PRIMARY KEY (order_id),

    CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Details(
    orderdetail_id INT AUTO_INCREMENT,
    order_id INT NOT NULL, 
    book_id INT NOT NULL,
    quantity DOUBLE,

    PRIMARY KEY (orderdetail_id),

    CONSTRAINT fk_orderdetails_orders
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),

    CONSTRAINT fk_orderdetails_books
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    );

