# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    ...  # TODO считать содержимое csv файла

    a = open(INPUT_FILENAME, "r")
    b = open(OUTPUT_FILENAME, "w")

    reader = csv.DictReader(a)
    k = []
    for i in reader:
        k.append(i)

    ...  # TODO Сериализовать в файл с отступами равными 4

    json.dump(k, b, indent = 4)
    b.close()
    a.close()


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")



