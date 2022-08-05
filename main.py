from custom_modules.api_functions import import_cars_by_brand
import sys


if __name__ == "__main__":
    selected_brand = sys.argv[1]
    print(selected_brand)
    my_cars = import_cars_by_brand(selected_brand)
    print(my_cars)
    