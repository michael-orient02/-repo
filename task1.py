import doctest


class Child:
    def __init__(self, height: float, weight: float, age: int):
        if height < 0:
            raise ValueError
        self.height = height

        if weight < 0:
            raise ValueError
        self.weight = weight

        if age < 0:
            raise ValueError
        if isinstance(age, int):
            raise TypeError
        self.age = age

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
        >>> test_5.growth(3) 
        """
        ...

    def sleep(self):
        """
        Метод, который описывает процесс cна ребенка
        """
        ...


class Tire:
    def __init__(self, widht: int, height: int, pressure: float):
        if widht <= 0:
            raise ValueError
        self.widht = widht

        if height <= 0:
            raise ValueError
        self.height = height

        if pressure <= 0:
            raise ValueError
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
    def __init__(self, font: str, size: int, number: int):
        self.font = font

        if size <= 0:
            raise ValueError
        self.size = size

        self.number = number
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
