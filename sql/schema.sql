CREATE SCHEMA bank_schema;

CREATE TABLE bank_schema.banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) UNIQUE NOT NULL,
    app_name VARCHAR(255)
);

CREATE TABLE bank_schema.reviews (
    review_id INT PRIMARY KEY,
    bank_id INT REFERENCES bank_schema.banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score DOUBLE PRECISION,
    source VARCHAR(255)
);
