from fastapi import FastAPI, Query, Path
from schemas import Book, Author

app = FastAPI()

@app.get('/main_page')
def home():
    return {'key': 'hello'}

@app.get('/pages/page_{pk}')
def get_page(pk: int, q = None):
    return {'key': pk, 'query': q}

@app.post('/book')
def post_book(item: Book, author: Author):
    return {"item": item, "author": author}

# Запрос: Query параметры и валидация
@app.get('/book')
def get_book(q: str = Query(None, min_length=2, max_length=5, description='Search info', regex='')):
    return q
# None или ... (обязательно) или 'test' (по умолчанию)
# min_length, max_length длина по умолчанию
# description вспомогательное описание
# regex регулярное выражение
#gt, ls для диапазона

# Параметры: Path параметры и валидация
@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20)):
    return {'pk': pk}
#gt=1 - значение больше 1
#le=20 - значение меньше 20

# для формирования request body - Body