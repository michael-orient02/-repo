BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError(f"'id' должно быть положительным целым числом. Получено: {id_}")

        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"'name' должно быть непустой строкой. Получено: {name}")

        if not isinstance(pages, int) or pages <= 0:
            raise ValueError(f"'pages' должно быть положительным целым числом. Получено: {pages}")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
