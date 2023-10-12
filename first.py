import pandas as pd

# Загружаем данные из файла visit_log.csv
visit_log = pd.read_csv('visit_log.csv', sep=';')

# Создаем столбец source_type и применяем правила для его заполнения

# Сначала создаем столбец source_type, который будет иметь те же значения, что и столбец traffic_source
# Это позволяет избежать потери данных в исходном столбце traffic_source
visit_log['source_type'] = visit_log['traffic_source']

# Если значение столбца traffic_source равно 'Yandex' или 'Google', то в столбце source_type ставим значение 'organic'
visit_log.loc[visit_log['traffic_source'].isin(['Yandex', 'Google']), 'source_type'] = 'organic'

# Если значение столбца traffic_source равно 'paid' и значение столбца region равно 'Russia', то в столбце source_type ставим значение 'ad'
visit_log.loc[(visit_log['traffic_source'].isin(['paid', 'email'])) & (visit_log['region'] == 'Russia'), 'source_type'] = 'ad'

# Если значение столбца traffic_source равно 'paid' и значение столбца region не равно 'Russia', то в столбце source_type ставим значение 'other'
visit_log.loc[(visit_log['traffic_source'].isin(['paid', 'email'])) & (visit_log['region'] != 'Russia'), 'source_type'] = 'other'

# Остальные значения столбца source_type остаются без изменений

# Выводим первые 5 строк датафрейма для проверки результата
print(visit_log.head())
