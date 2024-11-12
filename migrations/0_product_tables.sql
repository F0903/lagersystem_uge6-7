-- Table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_type VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT pk_product_id PRIMARY KEY (product_id),
    CONSTRAINT uq_name UNIQUE(name),
);

-- Table for dynamic product attributes
CREATE TABLE product_attributes (
    product_id INT,
    attribute_name VARCHAR(255),
    attribute_value VARCHAR(255),
    CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES products(product_id),
    CONSTRAINT uq_product_attribute UNIQUE (product_id, attribute_name)
);