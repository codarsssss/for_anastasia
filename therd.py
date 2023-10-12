import pandas as pd

# Загрузка данных из CSV файла в объект DataFrame
data = pd.read_csv("ratings.csv")

# Группировка данных по userId и подсчет количества оценок
ratings_count = data.groupby("userId").size().reset_index(name="count")

# Фильтрация пользователей с количеством оценок более 100
filtered_users = ratings_count[ratings_count["count"] > 100]

# Группировка данных по userId с вычислением минимального и максимального timestamp только для отфильтрованных пользователей
user_lifetime = data[data['userId'].isin(filtered_users['userId'])].groupby("userId").agg(
    min_timestamp=("timestamp", "min"),
    max_timestamp=("timestamp", "max")
).reset_index()

# Вычисление времени жизни (разницы между максимальным и минимальным timestamp) для каждого пользователя
user_lifetime["lifetime"] = user_lifetime["max_timestamp"] - user_lifetime["min_timestamp"]

# Вывод среднего времени жизни для каждого пользователя
print(user_lifetime)
