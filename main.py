# база недвижимости
properties_db = [
    {"id": 1, "title": "Квартира в центре", "price": 8500000, "distance_to_center": 1.2},
    {"id": 2, "title": "Студия у метро", "price": 5200000, "distance_to_center": 3.5},
    {"id": 3, "title": "Апартаменты в спальном районе", "price": 6100000, "distance_to_center": 7.8},
    {"id": 4, "title": "Дом с участком", "price": 14000000, "distance_to_center": 15.0},
]


def calculate_price_difference(target_price, average_price):
    # на сколько процентов цена отличается от средней
    if average_price == 0:
        return 0.0
    return round((target_price - average_price) / average_price * 100, 2)


def filter_by_max_distance(objects_list, max_distance):
    # объекты, которые не дальше max_distance от центра
    result = []
    for obj in objects_list:
        if obj["distance_to_center"] <= max_distance:
            result.append(obj)
    return result


def main():
    avg_price = sum(obj["price"] for obj in properties_db) / len(properties_db)
    print("Средняя цена по базе:", avg_price, "руб.")

    while True:
        choice = input("\n1 - поиск по расстоянию до центра, 2 - сравнить цену со средней, 0 - выход: ")

        if choice == "1":
            try:
                found = filter_by_max_distance(properties_db, float(input("Расстояние до центра (км): ")))
            except ValueError:
                print("Ошибка: введите число!")
                continue
            for obj in found:
                print("-", obj["title"], obj["price"], "руб.", obj["distance_to_center"], "км")
            if not found:
                print("Объектов в такой локации не найдено.")

        elif choice == "2":
            try:
                obj_id = int(input("ID объекта (1-4): "))
            except ValueError:
                print("Ошибка: введите корректный ID!")
                continue
            for obj in properties_db:
                if obj["id"] == obj_id:
                    diff = calculate_price_difference(obj["price"], avg_price)
                    print(obj["title"], "отличается от средней цены на", diff, "%")
                    break
            else:
                print("Объект с таким ID не найден!")

        elif choice == "0":
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
