employees = [("Иван", 25, "инженер"), ("Анна", 32, "менеджер"), ("Борис", 45, "директор"), ("Мария", 28, "аналитик")] 

age_more_thirty = filter(lambda age: age[1] > 30, employees)

name_sort = sorted(age_more_thirty, key=lambda name: name[1])

print(name_sort)