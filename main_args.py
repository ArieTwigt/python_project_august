import argparse
from ast import arg
from custom_modules.car_functions import import_cars_by_brand

# initate a argument parser
parser = argparse.ArgumentParser()

# specify the arguments
parser.add_argument('--brand', required=True, type=str)
parser.add_argument('--colour', required=False, type=str, default='WIT')

# parse the arguments
args = parser.parse_args()

if __name__ ==  '__main__':
    
    # get the arguments
    selected_brand = args.brand
    selected_colour = args.colour
    
    # execute the function
    import_cars_by_brand(selected_brand, selected_colour)