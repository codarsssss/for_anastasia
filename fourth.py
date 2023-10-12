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
# Аргумент how='left' определяет тип объединения как left join
merged_data = pd.merge(client_base, rzd, on='client_id', how='left')
merged_data = pd.merge(merged_data, auto, on='client_id', how='left')
merged_data = pd.merge(merged_data, air, on='client_id', how='left')

print(merged_data)
