import pandas as pd

# Задание данных
rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

# Объединение таблиц rzd, auto, air по столбцу client_id

# Создаем копию client_base !без столбца с адресом!
revenue_data = client_base[['client_id']]

# Аргумент how='left' определяет тип объединения как left join
revenue_data = revenue_data.merge(rzd, on='client_id', how='left')
revenue_data = revenue_data.merge(auto, on='client_id', how='left')
revenue_data = revenue_data.merge(air, on='client_id', how='left')

# Создаем копию таблицы
revenue_data_with_address = revenue_data.copy()

# Добавляем адрес в копию
revenue_data_with_address['address'] = client_base['address']

print("Таблица с тремя типами выручки для каждого client_id без указания адреса клиента:")
print(revenue_data)

print("Таблица с тремя типами выручки для каждого client_id с указанием адреса клиента:")
print(revenue_data_with_address)
