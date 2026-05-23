# Исходные данные
length = 5.5    # длина помещения в метрах
width = 4.2     # ширина помещения в метрах
height = 2.7    # высота помещения в метрах
paint_cost_per_m2 = 125  # стоимость покраски за м² (руб)

# Расчёты
floor_area = length * width  # площадь пола

# Площадь стен: периметр * высота
# Периметр = 2 * (длина + ширина)
wall_area = 2 * (length + width) * height

volume = length * width * height  # объём помещения

# Стоимость покраски стен
total_paint_cost = wall_area * paint_cost_per_m2
# Вывод результатов с округлением до 2 знаков
print("=== ГЕОМЕТРИЧЕСКИЕ ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Длина: {length} м")
print(f"Ширина: {width} м")
print(f"Высота: {height} м")
print()
print("=== РЕЗУЛЬТАТЫ РАСЧЁТОВ ===")
print(f"Площадь пола: {round(floor_area, 2)} м²")
print(f"Площадь стен: {round(wall_area, 2)} м²")
print(f"Объём помещения: {round(volume, 2)} м³")
print()
print("=== СТОИМОСТЬ ПОКРАСКИ ===")
print(f"Стоимость покраски 1 м²: {paint_cost_per_m2} руб")
print(f"Общая стоимость покраски стен: {round(total_paint_cost, 2)} руб")

