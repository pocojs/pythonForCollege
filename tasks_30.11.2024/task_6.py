employees = {
    1: {"имя": "Максим", "должность": "уборщик", "зарплата": 40000},
    2: {"имя": "Александр", "должность": "директор", "зарплата": 300000},
    3: {"имя": "Братишка", "должность": "дев-опс", "зарплата": 150000}
}

def info_about_employees():
    for i in employees:
        print(employees[i])

def found_employer():
    employer_id = int(input("Введите номер сотрудника: "))
    if employer_id in employees:
        print(employees[employer_id])
    else:
        print(f"Cотрудник номер {employer_id} не найден")


def change_salary():
    employer_id = int(input("Введите id сотрудника: "))
    if employer_id in employees:
        updated_salary = int(input("Введите новую зарплату: "))
        employees[employer_id]["зарплата"] = updated_salary
        print(f"Зарплата сотрудника номер {employer_id} изменена на {updated_salary}.")
    else:
        print(f"Cотрудник номер {employer_id} не найден")


def del_employer():
    employer_id = int(input("Введите id сотрудника: "))
    if employer_id in employees:
        print(f"Сотрудник номер {employer_id} был удален из базы-данных")
        del employees[employer_id]
    else:
        print(f"Cотрудник номер {employer_id} не найден")


def user_menu():
    while True:
        print("\n1 - Показать всех сотрудников")
        print("2 - Найти сотрудника по ID")
        print("3 - Изменить зарплату сотрудника")
        print("4 - Удалить сотрудника")

        choice_num = input("\nВыберите действие: ")
        if choice_num == "1":
            info_about_employees()
        elif choice_num == "2":
            found_employer()
        elif choice_num == "3":
            change_salary()
        elif choice_num == "4":
            del_employer()
        else:
            print("")

user_menu()