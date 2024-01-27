import csv
import os
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.quantity = quantity
        self.price = price
        self.__name = name
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Доступ к name
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Изменение name
        """
        self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_csv: str) -> None:
        """
        Инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, file_csv)

        cls.all.clear()
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Item(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(str_number: str) -> int:
        """
        Преобразует строковое представление числа в целое число.
        """
        return int(float(str_number))