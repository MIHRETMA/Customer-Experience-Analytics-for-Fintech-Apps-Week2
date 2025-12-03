import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",              # PostgreSQL is running on your machine
    database="bank_reviews",       # Database name 
    user="admin",                  # PostgreSQL username
    password="admin123"            # PostgreSQL password
)

# Create a cursor object — used to execute SQL commands
cur = conn.cursor()

# Create tables
with open("schema.sql", "r") as f:
    cur.execute(f.read())
conn.commit()

# Load banks
df_banks = pd.read_csv("reviews_processed.csv")
unique_banks = df_banks["bank_name"].drop_duplicates() # Get unique bank names

# Loop through each row in unique_banks and insert into banks table
for bank in unique_banks:

    # Execute SQL INSERT for each row
    # ON CONFLICT DO NOTHING avoids errors if the primary key already exists
    cur.execute(
        """
        INSERT INTO bank_schema.banks (bank_name)
        VALUES (%s)
        ON CONFLICT DO NOTHING;
        """,
        (bank,)
    )


# Load reviews
df_reviews = pd.read_csv("reviews_with_sentiment.csv")

df_reviews = df_reviews.rename(columns={
    "bert_sentiment": "sentiment_label",
    "bert_score": "sentiment_score"
})

bank_lookup = pd.read_sql("SELECT bank_id, bank_name FROM bank_schema.banks;", conn)
print(bank_lookup)

df_reviews = df_reviews.merge(bank_lookup, on="bank_name", how="left")

for _, row in df_reviews.iterrows():

    # Insert each review into PostgreSQL
    cur.execute(
        """
        INSERT INTO bank_schema.reviews 
            (review_id, bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source)
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
        """,
        (
            int(row["review_id"]),       # Review ID (primary key)
            int(row["bank_id"]),   # Foreign key referencing banks table
            row["review_text"],          # Full text review
            int(row["rating"]),          # Numerical rating
            row["review_date"],          # Date string
            row["sentiment_label"],      # Sentiment label
            row["sentiment_score"],      # Sentiment score
            row["source"]                # Review source 
        )
    )


conn.commit()
cur.close()
conn.close()
