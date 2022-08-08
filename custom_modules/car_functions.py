import requests
import pandas as pd
import os
from sqlalchemy import create_engine


def import_cars_by_brand(brand: str, 
                         selected_color: str='ZWART', 
                         export_to_csv=False,
                         export_to_db=False,
                         from_db=False) -> list:
    '''
    Returns a list of cars by the specified brand
    
    params:
    * brand, a car brand
    * colour
    '''
    
    db_name = "data.db"
    con = create_engine(f'sqlite:///{db_name}')
    
    if from_db:
        qry = "select * from cars where merk = ? limit 5"
        imported_cars_df = pd.read_sql_query(qry, con=con, params=(brand,))
        return imported_cars_df
    
    
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"
    response = requests.get(endpoint)
    
    response.status_code
    
    cars_list = response.json()
    
    filtered_cars_list = [car
                          for car in cars_list
                          if car['eerste_kleur'] == selected_color]
    
    # convert the cars list to a data frame
    cars_df = pd.DataFrame(filtered_cars_list)
    
    # option for export to csv
    if export_to_csv:
        folder_name = f"cars_data/{brand}"
        os.makedirs(folder_name, exist_ok=True)
        filename = f"{folder_name}/cars_{brand}.csv"
        print(f"Exporting to file:\n{filename}\n")
        cars_df.to_csv(filename, 
                   sep=";",
                   index=None)
    
    
    # option for export do database
    if export_to_db:
        print("\nExporting to database")
        
        cars_df.to_sql("cars", con=con, if_exists="append", index=False)
        print("Succesfully exported to database")
        return cars_df
    
    
  