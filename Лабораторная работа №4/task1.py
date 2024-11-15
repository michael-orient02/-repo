import json


def task() -> float:
    file_path = 'input.json'

    with open(file_path, 'r') as file:
        data = json.load(file)

    total_sum = sum(item['score'] * item['weight'] for item in data)

    result = round(total_sum, 3)

    return result


print(task())
