grades = {
    "математика": 5,
    "физика": 4,
    "информатика": 5,
    "химия": 3
}

average_score = sum(grades.values()) / len(grades)
print(f"Средний балл по всем предмета: {average_score}")

max_score = max(grades.items(), key=lambda grade: grade[1])
print(f"Лучшая оценка по предмету: {max_score[0]}")