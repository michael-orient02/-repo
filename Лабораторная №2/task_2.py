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

# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает следующий идентификатор для новой книги.
        Если книг нет, возвращает 1.
        Если книги есть, возвращает id последней книги + 1.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги по id.
        Если книги с таким id нет, вызывает ValueError.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
