import argparse
from ast import arg
from custom_modules.car_functions import import_cars_by_brand

# initate a argument parser
parser = argparse.ArgumentParser()

# specify the arguments
parser.add_argument('--brand', required=True, type=str)
parser.add_argument('--colour', required=False, type=str, default='WIT')
parser.add_argument('--csv_export', required=False, type=bool, default=False)
parser.add_argument('--db_export', required=False, type=bool, default=False)
parser.add_argument('--from_db', required=False, type=bool, default=False)

# parse the arguments
args = parser.parse_args()

if __name__ ==  '__main__':
    
    # get the arguments
    selected_brand = args.brand
    selected_colour = args.colour
    export_to_csv = args.csv_export
    export_to_db = args.db_export
    from_db = args.from_db
    
    # execute the function
    df = import_cars_by_brand(selected_brand, 
                         selected_colour, 
                         export_to_csv=export_to_csv,
                         export_to_db=export_to_db,
                         from_db=from_db
                         )
    
    # print out the cars
    print(df)