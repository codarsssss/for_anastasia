import pandas as pd

# Чтение содержимого файла
df = pd.read_csv('URLs.txt', header=None)

# Описание регулярного выражения
regex = r'/\d{8}-'

# Фильтрация страниц с текстами новостей по шаблоку регулярного выражения
filtered_urls = df[df[0].str.contains(regex)]

print(filtered_urls)
