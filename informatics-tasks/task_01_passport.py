# Объявление переменных
student_name = "Костина Елена Владимировна"
group_number = "ИС-22-1"
project_name = 'ЖК "Солнечный"'
floors = 9
height = 27.0
is_residential = True
construction_year = 2023

# Вывод информации
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {student_name}")
print(f"Группа: {group_number}")
print()
print(f"Объект: {project_name}")
print(f"Этажность: {floors} этажей")
print(f"Высота: {height} м")
print(f"Тип: {'Жилой' if is_residential else 'Нежилой'}")
print(f"Год постройки: {construction_year}")

# Комментарии:
# Где находится этот объект: г. Москва, ул. Солнечная, д. 15
# Почему вы выбрали именно его: Это современный жилой комплекс 
# в моем районе, построенный в прошлом году.
