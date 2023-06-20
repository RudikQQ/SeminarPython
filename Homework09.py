import pandas as pd
                    #Task40
#  Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

                    #decision
​
df[df['population']<501]['median_house_value'].agg(['mean'])
                    # Вариант 2:
​
df[df['population']<501]['median_house_value'].mean()
206799.95140186916
                    # Task42
# Узнать какая максимальная households в зоне минимального значения population

                    #decision
​
df[df['population']==df['population'].min()]['households'].max()

​
                    # Вариант 2:
df[df['population']==df['population'].min()]['households'].agg(['max'])

