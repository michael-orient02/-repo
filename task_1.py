class Pet:
    """
    Базовый класс для домашних животных.

    Атрибуты:
        name (str): Имя питомца.
        age (int): Возраст питомца.
        species (str): Вид животного.
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Инициализирует объект домашнего животного.

        Args:
            name (str): Имя питомца.
            age (int): Возраст питомца.
            species (str): Вид животного.
        """
        self.name = name
        self.age = age
        self.species = species

    def __str__(self) -> str:
        """Возвращает строковое представление питомца."""
        return f"{self.species} по имени {self.name}, возраст: {self.age} лет."

    def __repr__(self) -> str:
        """Возвращает строковое представление для отладки."""
        return f"Pet(name={self.name!r}, age={self.age}, species={self.species!r})"

    def make_sound(self) -> str:
        """Метод, возвращающий звук, который издает животное."""
        return f"{self.name} издает звук."


class Dog(Pet):
    """
    Дочерний класс, представляющий собаку.

    Атрибуты:
        breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализирует объект собаки, расширяя базовый класс.

        Args:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, age, species="Собака")
        self.breed = breed  # Новый атрибут

    def __str__(self) -> str:
        """Перегружаем строковое представление, добавляя информацию о породе."""
        return f"{self.species} {self.breed} по имени {self.name}, возраст: {self.age} лет."

    def make_sound(self) -> str:
        """
        Переопределяем метод make_sound().

        Причина: собаки лают, поэтому заменяем общий звук на "Гав-гав!".
        """
        return f"{self.name} говорит: 'Гав-гав!'"

    def fetch(self) -> str:
        """Метод, представляющий игру с собакой (принесение предмета)."""
        return f"{self.name} принес мячик!"


class Cat(Pet):
    """
    Дочерний класс, представляющий кошку.

    Атрибуты:
        is_indoor (bool): Является ли кошка домашней.
    """

    def __init__(self, name: str, age: int, is_indoor: bool) -> None:
        """
        Инициализирует объект кошки.

        Args:
            name (str): Имя кошки.
            age (int): Возраст кошки.
            is_indoor (bool): Является ли кошка домашней.
        """
        super().__init__(name, age, species="Кошка")
        self.is_indoor = is_indoor  # Новый атрибут

    def make_sound(self) -> str:
        """
        Переопределяем метод make_sound().

        Причина: кошки мяукают, поэтому заменяем общий звук на "Мяу!".
        """
        return f"{self.name} говорит: 'Мяу!'"

    def scratch(self) -> str:
        """Метод, представляющий царапанье мебели или когтеточки."""
        return f"{self.name} царапает когтеточку!"


# Пример использования
if __name__ == "__main__":
    dog = Dog("Бобик", 3, "Лабрадор")
    cat = Cat("Мурзик", 2, True)

    print(dog)  # Собака Лабрадор по имени Бобик, возраст: 3 лет.
    print(cat)  # Кошка по имени Мурзик, возраст: 2 лет.

    print(dog.make_sound())  # Бобик говорит: 'Гав-гав!'
    print(cat.make_sound())  # Мурзик говорит: 'Мяу!'

    print(dog.fetch())  # Бобик принес мячик!
    print(cat.scratch())  # Мурзик царапает когтеточку!
