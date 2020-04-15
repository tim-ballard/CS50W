import psycopg2
from flask import jsonify


def books_api(isbn):
    '''Returns JSON output for provided ISBN on books site API'''
    # Connect to database
    connection = psycopg2.connect(host="ec2-46-137-156-205.eu-west-1.compute.amazonaws.com",
                                  dbname="dailoi84mjuh0f",
                                  user="nzszhnfieumwiz",
                                  password="2e854b86a9d6a4e0b54f6513c4fdccfb2e615b53b084bc7a83049e2f308c0330")

    cursor = connection.cursor()

    sql = '''SELECT bk.title
      ,au.author
      ,bk.year
      ,bk.isbn
      ,COUNT(rw.review) review_count
      ,AVG(rw.score) average_score
    FROM books bk
        LEFT JOIN author au
           ON bk.author_id = au.id
        LEFT JOIN reviews rw
           ON bk.id = rw.book_id
    WHERE bk.isbn = %s
    GROUP BY bk.title
      ,au.author
      ,bk.year
      ,bk.isbn'''

    cursor.execute(sql, (isbn,))
    rows = cursor.fetchone()
    bookinfo = {}
    header = ['title', 'author', 'year', 'isbn', 'review_count', 'average_score']
    for i in range(6):
        bookinfo[header[i]] = rows[i]

    cursor.close()
    connection.close()

    if not bookinfo:
        return jsonify({"Error": "Book does not exist"}), 404

    return jsonify(bookinfo)


def main():
    print(books_api('0739328271'))
    print(books_api('3839'))
    return None


if __name__ == '__main__':
    main()
