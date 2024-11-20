import json

# Початкові дані
countries_data = [
    {"name": "Україна", "area": 603500, "population": 41902416, "continent": "Європа"},
    {"name": "Єгипет", "area": 1002450, "population": 102334404, "continent": "Африка"},
    {"name": "Канада", "area": 9984670, "population": 38008005, "continent": "Північна Америка"},
    {"name": "Індія", "area": 3287263, "population": 1393409038, "continent": "Азія"},
    {"name": "Франція", "area": 643801, "population": 65273511, "continent": "Європа"},
    {"name": "Кенія", "area": 580367, "population": 53771296, "continent": "Африка"},
    {"name": "Китай", "area": 9596961, "population": 1444216107, "continent": "Азія"},
    {"name": "Бразилія", "area": 8515767, "population": 212559417, "continent": "Південна Америка"},
    {"name": "Німеччина", "area": 357022, "population": 83240525, "continent": "Європа"},
    {"name": "ПАР", "area": 1219090, "population": 59308690, "continent": "Африка"}
]

# Функція для запису JSON-файлу як об'єкт з ключем 'countries'
def save_json(data, filename="countries.json"):
    data_object = {"countries": data}  # Обгортка в об'єкт з ключем 'countries'
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data_object, f, ensure_ascii=False, indent=4)

# Функція для завантаження JSON-файлу
def load_json(filename="countries.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["countries"]  # Повертаємо тільки список країн

# Функція для виведення вмісту JSON-файлу
def display_countries():
    data = load_json()
    print("Список країн:")
    for country in data:
        print(country)

# Функція для перевірки наявності країни за назвою
def country_exists(name, data):
    return any(country["name"].lower() == name.lower() for country in data)

# Функція для додавання нової країни
def add_country():
    data = load_json()
    name = input("Введіть назву країни: ")

    # Перевірка наявності країни в списку
    if country_exists(name, data):
        print(f"Країна '{name}' вже існує в списку.")
        return

    country = {
        "name": name,
        "area": int(input("Введіть площу країни: ")),
        "population": int(input("Введіть населення країни: ")),
        "continent": input("Введіть частину світу (Європа, Азія, Африка, тощо): ")
    }
    data.append(country)
    save_json(data)
    print("Країну додано успішно!")

# Функція для видалення країни за назвою
def delete_country():
    data = load_json()
    name = input("Введіть назву країни для видалення: ")

    # Перевірка наявності країни в списку
    if not country_exists(name, data):
        print(f"Країни '{name}' немає в списку.")
        return

    data = [country for country in data if country["name"].lower() != name.lower()]
    save_json(data)
    print(f"Країну '{name}' видалено успішно!")

# Функція для пошуку країни за полем
def search_country():
    field = input("Введіть поле для пошуку (name, area, population, continent): ").lower()
    value = input("Введіть значення для пошуку: ")

    data = load_json()
    found = [country for country in data if str(country.get(field, "")).lower() == value.lower()]

    if found:
        print("Знайдені країни:")
        for country in found:
            print(country)
    else:
        print("Країн з такими даними не знайдено.")

# Функція для пошуку країн в Африці або Азії та запису результату в окремий JSON файл
def filter_asia_africa():
    data = load_json()
    result = [country for country in data if country["continent"] in ["Африка", "Азія"]]

    if result:
        # Виведення результатів на екран
        print("Країни, що знаходяться в Африці або Азії:")
        for country in result:
            print(country)

        # Збереження результатів у новий JSON файл
        save_json(result, filename="asia_africa_countries.json")
        print("Результати також записані в файл 'asia_africa_countries.json'")
    else:
        print("Країн з Африки або Азії не знайдено.")

# Головна функція для діалогового режиму
def main():
    save_json(countries_data)  # Початкове збереження даних у файл

    while True:
        print("\nОберіть дію:")
        print("1. Вивести вміст JSON-файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Пошук даних за полем")
        print("5. Пошук країн в Африці або Азії та запис результату")
        print("6. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            display_countries()
        elif choice == "2":
            add_country()
        elif choice == "3":
            delete_country()
        elif choice == "4":
            search_country()
        elif choice == "5":
            filter_asia_africa()
        elif choice == "6":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Виклик головної функції
if __name__ == "__main__":
    main()
