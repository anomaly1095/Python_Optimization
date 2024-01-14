from typing import List
from threading import *
from time import perf_counter                                   
from os import system

def read_buffer(countries: List[dict]) -> None:
        """Reads values from buffer, creates the dict, appends fdict to list."""
        
        with open(file="/home/amnesia2/Documents/Data/GDP/gdp.csv", mode='r') as buffer:
            for line in buffer:
                name, gdp1980, gdp1981, gdp1982, gdp1983, gdp1984, gdp1985, gdp1986, gdp1987, gdp1988, gdp1989, gdp1990, gdp1991, gdp1992, gdp1993, gdp1994, gdp1995, gdp1996, gdp1997, gdp1998, gdp1999, gdp2000, gdp2001, gdp2002, gdp2003, gdp2004, gdp2005, gdp2006, gdp2007, gdp2008, gdp2009, gdp2010, gdp2011, gdp2012, gdp2013, gdp2014, gdp2015, gdp2016, gdp2017, gdp2018, gdp2019, gdp2020, gdp2021, gdp2022, gdp2023, gdp2024, gdp2025, gdp2026, gdp2027, gdp2028 = line.strip().split(',')
                country = {
                    'name': name,
                    'gdp1980': gdp1980,
                    'gdp1981': gdp1981,
                    'gdp1982': gdp1982,
                    'gdp1983': gdp1983,
                    'gdp1984': gdp1984,
                    'gdp1985': gdp1985,
                    'gdp1986': gdp1986,
                    'gdp1987': gdp1987,
                    'gdp1988': gdp1988,
                    'gdp1989': gdp1989,
                    'gdp1990': gdp1990,
                    'gdp1991': gdp1991,
                    'gdp1992': gdp1992,
                    'gdp1993': gdp1993,
                    'gdp1994': gdp1994,
                    'gdp1995': gdp1995,
                    'gdp1996': gdp1996,
                    'gdp1997': gdp1997,
                    'gdp1998': gdp1998,
                    'gdp1999': gdp1999,
                    'gdp2000': gdp2000,
                    'gdp2001': gdp2001,
                    'gdp2002': gdp2002,
                    'gdp2003': gdp2003,
                    'gdp2004': gdp2004,
                    'gdp2005': gdp2005,
                    'gdp2006': gdp2006,
                    'gdp2007': gdp2007,
                    'gdp2008': gdp2008,
                    'gdp2009': gdp2009,
                    'gdp2010': gdp2010,
                    'gdp2011': gdp2011,
                    'gdp2012': gdp2012,
                    'gdp2013': gdp2013,
                    'gdp2014': gdp2014,
                    'gdp2015': gdp2015,
                    'gdp2016': gdp2016,
                    'gdp2017': gdp2017,
                    'gdp2018': gdp2018,
                    'gdp2019': gdp2019,
                    'gdp2020': gdp2020,
                    'gdp2021': gdp2021,
                    'gdp2022': gdp2022,
                    'gdp2023': gdp2023,
                    'gdp2024': gdp2024,
                    'gdp2025': gdp2025,
                    'gdp2026': gdp2026,
                    'gdp2027': gdp2027,
                    'gdp2028': gdp2028,
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
def print_data(countries: list):
    for country in countries:
        print(country['name'])
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
    
    # thread_remove_first_country_start = perf_counter()
    # thread_remove_first_country = Thread(target=remove_country, args=(countries, 0))
    # thread_remove_first_country.start()
    # thread_remove_first_country.join()
    # thread_remove_first_country_end = perf_counter()
    #------------------------------------
    
    thread_print_data_start = perf_counter()
    thread_print_data = Thread(target=print_data, args=(countries, ))
    thread_print_data.start()
    thread_print_data.join()
    thread_print_data_end = perf_counter()
    #------------------------------------
    
    system("clear")
    print("-------------------------Time taken by threads in list of dicts-------------------------")
    print(f"Importing data:                {thread_read_buffer_end-thread_read_buffer_start:.7f} seconds")
    print(f"Appending country:             {thread_add_country_end-thread_add_country_start:.7f} seconds")
    print(f"remove country in: {index}:          {thread_remove_country_end-thread_remove_country_start:.7f} seconds")
    print(f"Insert country in {index}:           {thread_insert_country_end-thread_insert_country_start:.7f} seconds")
    # print(f"Remove first country:          {thread_remove_first_country_end-thread_remove_first_country_start:.7f} seconds")
    print(f"Printing data:                 {thread_print_data_end-thread_print_data_start:.7f} seconds")

def main():
    make_threads([], {}, 2)
    
if __name__ == '__main__':
    main()