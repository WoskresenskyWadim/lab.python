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

