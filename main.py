from custom_modules.calculation_functions import calc_circle, calc_pythagoras
from custom_modules.string_functions import capitalize_names


if __name__ == "__main__":
    my_c = calc_pythagoras(4,3)
    my_capitalized_names_list = capitalize_names('arie', 'john')
    print(my_c)
    print(my_capitalized_names_list)
