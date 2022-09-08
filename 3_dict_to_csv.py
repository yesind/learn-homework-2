"""
Работа csv
1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv
"""
import csv

def main():
    some_dictionaty = [{'name':'Mark', 'age':25,'job':'Doctor'},
            {'name':'Alice', 'age':30,'job':'Teacher'},
            {'name':'Nik', 'age':35,'job':'Driver'},
            {'name':'Alex', 'age':40,'job':'Engineer'}]
    
    with open('DZ2.csv', 'w', encoding='utf-8', newline='') as f:
        heads = ['name', 'age', 'job']
        file_writer = csv.DictWriter(f, heads, delimiter=',')
        file_writer.writeheader()
        for user in some_dictionaty:
            file_writer.writerow(user)
 

if __name__ == "__main__":
    main()