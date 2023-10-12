import pandas as pd


data = pd.read_csv("ratings.csv")

# Группировка данных по userId и подсчет количества оценок
ratings_count = data.groupby("userId").size().reset_index(name="count")

# Фильтрация пользователей с количеством оценок более 100
filtered_users = ratings_count[ratings_count["count"] > 100]

# Объединение данных с минимальным и максимальным timestamp для каждого пользователя
user_lifetime = data.groupby("userId").agg(lifetime=("timestamp", lambda x: x.max() - x.min())).reset_index()

# Вычисление среднего времени жизни пользователей
average_lifetime = user_lifetime[user_lifetime["userId"].isin(filtered_users["userId"])].mean()["lifetime"]

print(average_lifetime)
