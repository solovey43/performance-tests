from locust import HttpUser, task, between, TaskSet, SequentialTaskSet


# Пример 1. HttpUser с двумя задачами и распределением нагрузки
class MySimpleUser(HttpUser):
    host = "https://api.example.com"

    # Время ожидания между задачами: случайное значение от 1 до 2 секунд
    wait_time = between(1, 2)

    @task(4)
    def get_home(self):
        """
        Задача №1: отправляет GET-запрос на /home
        Частота выполнения — выше, чем у второй задачи
        """
        self.client.get("/home")

    @task(1)
    def get_dashboard(self):
        """
        Задача №2: отправляет GET-запрос на /dashboard
        Выполняется реже, с меньшим приоритетом
        """
        self.client.get("/dashboard")

# Пример 2. Использование TaskSet для группировки сценариев
# Группа задач: просмотр каталога
class BrowseCatalog(TaskSet):
    @task(3)
    def get_product(self):
        self.client.get("/product/123")

    @task(2)
    def get_category(self):
        self.client.get("/category/456")


# Группа задач: просмотр корзины
class BrowseBucket(TaskSet):
    @task
    def get_product(self):
        self.client.get("/bucket")


# Пользователь, который выполняет задачи из двух групп
class ShopUser(HttpUser):
    host = "https://api.example.com"
    tasks = [BrowseCatalog, BrowseBucket]
    wait_time = between(1, 3)


# Пример 3. Явное распределение нагрузки между TaskSet с использованием словаря
# Группа задач: просмотр каталога
class BrowseCatalog(TaskSet):
    @task(3)
    def get_product(self):
        self.client.get("/product/123")

    @task(2)
    def get_category(self):
        self.client.get("/category/456")


# Группа задач: просмотр корзины
class BrowseBucket(TaskSet):
    @task
    def get_product(self):
        self.client.get("/bucket")


# Пользователь, которому заданы веса для TaskSet в формате словаря
class ShopUser(HttpUser):
    host = "https://api.example.com"

    tasks = {
        BrowseCatalog: 3,
        BrowseBucket: 7
    }

    wait_time = between(1, 3)


# Пример 4. Использование SequentialTaskSet для строгой последовательности шагов
# Последовательный сценарий: оформление заказа
class CheckoutFlow(SequentialTaskSet):
    @task(3)
    def open_cart(self):
        self.client.get("/cart")

    @task(4)
    def checkout(self):
        self.client.post("/checkout")

    @task(3)
    def confirm(self):
        self.client.get("/order/confirm")


# Пользователь, выполняющий строго последовательный сценарий
class CheckoutUser(HttpUser):
    host = "https://api.example.com"
    tasks = [CheckoutFlow]
    wait_time = between(2, 4)







