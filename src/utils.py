import json
import os

from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def crate_objects_from_json(data):
    all_category = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        all_category.append(Category(**category))

    return all_category


if __name__ == "__main__":
    raw_data = read_json("../data/data.json")
    category_data = crate_objects_from_json(raw_data)
