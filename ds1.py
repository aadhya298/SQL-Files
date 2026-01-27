import numpy as np
data_type=[('name', 'S15'), ('class', int), ('height', float)]
students_details=[("James", 3, 4), ('mail', 6, 12.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

students= np.array(students_details, dtype=data_type)
print(f"Original array: {students}")
print(f"Sort by height:{np.sort(students,order='height')}")
