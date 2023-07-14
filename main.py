from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()

@app.get('/main_page')
def home():
    return {'key': 'hello'}

@app.get('/pages/page_{pk}')
def get_page(pk: int, q = None):
    return {'key': pk, 'query': q}

@app.post('/book')
def post_book(item: Book):
    return item

@app.get('/info')
def get_info(q: str = Query(None, min_length=2, max_length=5, description='Search info', regex='')):
    return q
# None или ... (обязательно) или 'test' (по умолчанию)
# min_length, max_length длина по умолчанию
# description вспомогательное описание
# regex регулярное выражение