# Класс Store для управления магазинами
class Store:
    def __init__(self, name, address):
        """
        Конструктор класса Store.
        Инициализирует название, адрес магазина и пустой словарь с товарами.
        """
        self.name = name            # Название магазина
        self.address = address      # Адрес магазина
        self.items = {}             # Ассортимент: ключ — название товара, значение — цена

    def add_item(self, item_name, price):
        """
        Метод для добавления товара в ассортимент.
        Если товар с таким названием уже есть — цена обновляется.
        """
        self.items[item_name] = price

    def remove_item(self, item_name):
        """
        Метод для удаления товара из ассортимента.
        Если товара нет — ничего не делает.
        """
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """
        Метод для получения цены товара по названию.
        Если товар не найден — возвращает None.
        """
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """
        Метод для обновления цены товара.
        Если товар отсутствует — выводит предупреждение.
        """
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")

# === Создание нескольких магазинов ===

# Магазин 1
store1 = Store("Фрукты24", "ул. Центральная, 1")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

# Магазин 2
store2 = Store("ОвощиМаркет", "пр. Ленина, 45")
store2.add_item("carrots", 0.4)
store2.add_item("potatoes", 0.3)

# Магазин 3
store3 = Store("Сладости+", "ул. Победы, 78")
store3.add_item("chocolate", 1.2)
store3.add_item("cookies", 0.9)

# === Тестирование методов на одном магазине (store1) ===

print(f"\nМагазин: {store1.name}, Адрес: {store1.address}")

# Добавим новый товар
store1.add_item("pears", 0.65)
print("Добавлен pears:", store1.items)

# Получим цену на bananas
banana_price = store1.get_price("bananas")
print("Цена на bananas:", banana_price)

# Обновим цену на apples
store1.update_price("apples", 0.55)
print("Обновленная цена на apples:", store1.items)

# Попробуем обновить цену на несуществующий товар
store1.update_price("mango", 1.5)  # Должно вывести предупреждение

# Удалим товар pears
store1.remove_item("pears")

print("После удаления pears:", store1.items)

# Проверим цену на удалённый товар
pears_price = store1.get_price("pears")
print("Цена на pears (должно быть None):", pears_price)