import requests
import csv


def get_goodreadsinfo(isbns):
    '''Uses Goodreads API returns review info list of dictionaries for isbns

    Returns JSON with columns - id,  isbn,  isbn13,  ratings_count,  reviews_count,
    text_reviews_count,  work_ratings_count,  work_reviews_count,
    work_text_reviews_count,  average_rating
    '''
    isbns_str = ','.join(str(isbn) for isbn in isbns)
    res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": "mHAuvIsPTm7Vaa3XDrw",  "isbns": isbns_str})

    info = res.json()
    return info['books']


def get_goodreadselm(isbn,  elname):
    '''Reads goodreads api and returns chosen element

    elname options:
    id,  isbn,  isbn13,  ratings_count,  reviews_count,
    text_reviews_count,  work_ratings_count,  work_reviews_count,
    work_text_reviews_count,  average_rating
    '''
    book = get_goodreadsinfo(isbn)
    return book[elname]


def get_reviewdata(isbn):
    '''Return info for book page'''
    book = get_goodreadsinfo(isbn)
    return {'ratings': book['ratings_count'],  'averate': book['average_rating']}


def dict_to_csv(listdicts, filename):
    '''Creates a CSV from the given list of dictionarys

    Keyword arguments:
    listdicts -- List of dictonary objects
    filename -- CSV destination filename
    '''
    output = filename + '.csv'
    fieldnames = listdicts[0].keys()
    with open(output, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, dialect='excel')
        writer.writeheader()
        writer.writerows(listdicts)


def main():
    books = ['1401308236', '0718144848', '0141010371', '0718144392', '1401301940', '1401301959', '0718152433', '0718158482', '1401322336', '0718154762', '0718156145', '0718154770', '0718156811', '071815780X', '0718158148', '006230562X', '0718181239', '0718178440', '0718183657', '0718187725', '0718187733', '0718187768']
    info = get_goodreadsinfo(books)
    dict_to_csv(info, 'GoodreadsOutput')


if __name__ == '__main__':
    main()
