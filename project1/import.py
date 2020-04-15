import psycopg2
from psycopg2 import Error

# Connect to database
connection = psycopg2.connect(host="ec2-46-137-156-205.eu-west-1.compute.amazonaws.com",
                              dbname="dailoi84mjuh0f",
                              user="nzszhnfieumwiz",
                              password="2e854b86a9d6a4e0b54f6513c4fdccfb2e615b53b084bc7a83049e2f308c0330")

cursor = connection.cursor()

create_tables = '''
CREATE TABLE IF NOT EXISTS booksload (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year VARCHAR NOT NULL);

CREATE TABLE IF NOT EXISTS author (
    id SERIAL PRIMARY KEY,
    author VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    year VARCHAR NOT NULL,
    author_id INTEGER REFERENCES author
);
'''
try:
    cursor.execute(create_tables)
    connection.commit()
    print('Tables Successfully created')

except (Exception, psycopg2.DatabaseError) as error:
    print("Error creating tables", error)


# Load books from csv
sql = "COPY booksload (isbn,title,author,year) FROM STDIN WITH CSV HEADER DELIMITER AS ',' QUOTE AS '\"'"
csv_file = 'books.csv'

with open(csv_file, 'r') as f:
    cursor.copy_expert(sql, f)
    connection.commit()


# Update Author and Books Tables
load_tables = '''
INSERT INTO author (author)
SELECT author
FROM public.booksload
GROUP BY author;

INSERT INTO books (isbn, title, year, author_id)
SELECT isbn,
       title,
       year,
       au.id author_id
FROM public.booksload bk
    LEFT JOIN public.author au
        ON bk.author = au.author;

DROP TABLE booksload;
'''
try:
    cursor.execute(load_tables)
    connection.commit()
    print('Tables Successfully loaded')

except (Exception, psycopg2.DatabaseError) as error:
    print("Error loading tables", error)


cursor.close()
connection.close()
