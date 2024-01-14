from typing import List
from threading import *
from time import perf_counter                                   #Linked list: value is a dict that has the country data and a link
from os import system

def read_buffer(countries: List[dict]) -> None:
        """Reads values from buffer, creates the dict, appends fdict to list."""
        
        with open(file="/home/amnesia2/Documents/Data/Country_data.csv", mode='r') as buffer:
            for line in buffer:
                name, total_surface, land, water, water_percentage, hdi, hdi_growth, imf_forcast_gdp, world_bank_forecast_gdp, un_forecast_gdp, imf_forecast_gdp_ppp, world_bank_forecast_gdp_ppp, cia_forecast_gdp_ppp, internet_users, un_continental_region, un_statistical_subregion, population_2022, population_2023, population_change = line.strip().split(',')
                country = {
                    "name": name,
                    "total_surface": total_surface,
                    "land": land, 
                    "water": water,
                    "water_percentage": water_percentage,
                    "hdi": hdi,
                    "hdi_growth": hdi_growth,
                    "imf_forcast_gdp": imf_forcast_gdp,
                    "world_bank_forecast_gdp": world_bank_forecast_gdp,
                    "un_forecast_gdp": un_forecast_gdp,
                    "imf_forecast_gdp_ppp": imf_forecast_gdp_ppp,
                    "world_bank_forecast_gdp_ppp": world_bank_forecast_gdp_ppp,
                    "cia_forecast_gdp_ppp": cia_forecast_gdp_ppp,
                    "internet_users": internet_users,
                    "un_continental_region": un_continental_region,
                    "un_statistical_subregion": un_statistical_subregion,
                    "population_2022": population_2022,
                    "population_2023": population_2023,
                    "population_change": population_change
                }
                countries.append(country)

def add_country(countries: List[dict], country: dict):
    countries.append(country)

def remove_country(countries: List[dict], index: int):
    countries.pop(index)

def insert_country(countries: List[dict], country: dict, index: int):
    try:
        countries.insert(index, country)
    except IndexError:
        print("invalid index")
        
def make_threads(countries: List[dict], country: dict, index: int):
    thread_read_buffer_start = perf_counter()
    thread_read_buffer = Thread(target=read_buffer, args=(countries, ))
    thread_read_buffer.start()
    thread_read_buffer.join()
    thread_read_buffer_end = perf_counter()
    #------------------------------------
        
    thread_add_country_start = perf_counter()
    thread_add_country = Thread(target=add_country, args=(countries, country, ))
    thread_add_country.start()
    thread_add_country.join()
    thread_add_country_end = perf_counter()
    #------------------------------------
    
    thread_remove_country_start = perf_counter()
    thread_remove_country = Thread(target=remove_country, args=(countries, index, ))
    thread_remove_country.start()
    thread_remove_country.join()
    thread_remove_country_end = perf_counter()
    #------------------------------------
    
    thread_insert_country_start = perf_counter()
    thread_insert_country = Thread(target=insert_country, args=(countries, country, index, ))
    thread_insert_country.start()
    thread_insert_country.join()
    thread_insert_country_end = perf_counter()
    #------------------------------------
    
    thread_remove_first_country_start = perf_counter()
    thread_remove_first_country = Thread(target=remove_country, args=(countries, 0))
    thread_remove_first_country.start()
    thread_remove_first_country.join()
    thread_remove_first_country_end = perf_counter()
    #------------------------------------
    
    thread_print_data_start = perf_counter()
    thread_print_data = Thread(target=print, args=(countries, ))
    thread_print_data.start()
    thread_print_data.join()
    thread_print_data_end = perf_counter()
    #------------------------------------
    
    system("clear")
    print("-------------------------Time taken by threads in list of dicts-------------------------")
    print(f"Importing data:                {thread_read_buffer_end-thread_read_buffer_start:.7f} seconds")
    print(f"Appending country:                   {thread_add_country_end-thread_add_country_start:.7f} seconds")
    print(f"remove country in: {index}:          {thread_remove_country_end-thread_remove_country_start:.7f} seconds")
    print(f"Insert country in {index}:           {thread_insert_country_end-thread_insert_country_start:.7f} seconds")
    # print(f"Remove first country:          {thread_remove_first_country_end-thread_remove_first_country_start:.7f} seconds")
    print(f"Printing data:                 {thread_print_data_end-thread_print_data_start:.7f} seconds")

def main():
    make_threads([], {}, 2)
    
if __name__ == '__main__':
    main()