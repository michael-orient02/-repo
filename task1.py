import doctest


class Child:
    """
    Класс описывает параметры ребенка.

    """
    def __init__(self, height: float, weight: float, age: int):
        if age < 0:
            raise ValueError
        if not isinstance(age, int):
            raise TypeError
        self.age = age

        if height < 0:
            raise ValueError
        if not isinstance(height, float):
            raise TypeError
        self.height = height

        if weight < 0:
            raise ValueError
        if not isinstance(weight, float):
            raise TypeError
        self.weight = weight

        """
        :param: height: Рост ребёнка
        :param: weight: Вес ребёнка
        :param: age: Возраст ребёнка

        Пример:
        >>> test_4 = Child(116, 24, 6)
        """

    def growth(self, age: int):
        if age < 0:
            raise ValueError
        self.age = age
        """
        Метод имитирует рост ребенка до указанного количество лет
        :param: age: Количество лет

        Пример:
        >>> test_5 = Child(116, 24, 6)
        >>> test_5.growth(7) 
        """
        ...

    def describe(self):

        print(f"Dзраст {self.age} лет, рост {self.height} см, вес {self.weight} кг.")
        """
        Метод для вывода информации о ребенке.
        
        Пример:
        >>> test_9 = Child(116, 24, 6)
        >>> test_9.describe()
        """
        ...


class Tire:
    """
    Класс описывает параметры шины автомобиля.
    """
    def __init__(self, widht: int, height: int, pressure: float):
        if widht <= 0:
            raise ValueError
        if not isinstance(widht, int):
            raise TypeError
        self.widht = widht

        if height <= 0:
            raise ValueError
        if not isinstance(height, int):
            raise TypeError
        self.height = height

        if pressure <= 0:
            raise ValueError
        if not isinstance(pressure, float):
            raise TypeError
        self.pressure = pressure
        """
        :param: widht: Ширина шины
        :param: height: Высота шины
        :param: pressure: Давление в шине

        Пример:
        >>> test_6 = Tire(205, 55, 1.5)
        """

    def inflate(self, pressure: float):
        if pressure <= 0:
            raise ValueError
        self.pressure = pressure
        """
        Метод, который описывает процесс накачивания шины воздухом до определенного давления
        :param: pressure: Желаемое давление в барах

        Пример:
        >>> test_8 = Tire(205, 55, 1.5)
        >>> test_8.inflate(2.1)
        """
        ...

    def deflate(self, pressure: float):
        if pressure <= 0:
            raise ValueError
        self.pressure = pressure
        """
        Метод, который описывает процесс спускания воздуха из шины до определенного давления
        :param: pressure: Желаемое давление в барах

        Пример: 
        >>> test_7 = Tire(205, 55, 1.5)
        >>> test_7.deflate(1.1)
        """
        ...


class Text:
    """
    Класс описывает текста.
    """
    def __init__(self, font: str, size: int, number: int):
        self.font = font

        if size <= 0:
            raise ValueError
        if not isinstance(size, int):
            raise TypeError
        self.size = size

        self.number = number
        if not isinstance(number, int):
            raise TypeError
        """
        :param: text_font: Щрифт текста
        :param: text_size: Размер текста
        :param: number: Количество отступов


        Пример:
        >>> test_1 = Text('Times New Roman', 14)
        """

    def indent(self, number: int):
        self.number = number

        """
        Метод изменяет отсуп
        :param: number: Количество отступов

        Пример:
        >>> test_2 = Text('Times New Roman', 14)
        >>> test_2.indent(1)
        """
        ...

    def size(self, size: int):
        if size <= 0:
            raise ValueError
        self.size = size
        """
        Метод изменяет размер шрифта
        :param: size: Размер шрифта

        Пример:
        >>> test_3 = Text('Times New Roman', 14)
        >>> test_3.size(12)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
