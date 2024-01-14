from typing import List
from threading import *
from time import perf_counter
from os import system

class Country:
    countries: List["Country"] = []

    def __init__(
        self,
        name: str = "",
        total_surface: float = 0.0,
        land: float = 0.0,
        water: float = 0.0,
        water_percentage: float = 0.0,
        hdi: float = 0.0,
        hdi_growth: float = 0.0,
        imf_forcast_gdp: float = 0.0,
        world_bank_forecast_gdp: float = 0.0,
        un_forecast_gdp: float = 0.0,
        imf_forecast_gdp_ppp: float = 0.0,
        world_bank_forecast_gdp_ppp: float = 0.0,
        cia_forecast_gdp_ppp: float = 0.0,
        internet_users: float = 0.0,
        un_continental_region: str = "",
        un_statistical_subregion: str = "",
        population_2022: float = 0.0,
        population_2023: float = 0.0,
        population_change: float = 0.0,
    ) -> None:
        self.name = name
        self.total_surface = total_surface
        self.land = land
        self.water = water
        self.water_percentage = water_percentage
        self.hdi = hdi
        self.hdi_growth = hdi_growth
        self.imf_forcast_gdp = imf_forcast_gdp
        self.world_bank_forecast_gdp = world_bank_forecast_gdp
        self.un_forecast_gdp = un_forecast_gdp
        self.imf_forecast_gdp_ppp = imf_forecast_gdp_ppp
        self.world_bank_forecast_gdp_ppp = world_bank_forecast_gdp_ppp
        self.cia_forecast_gdp_ppp = cia_forecast_gdp_ppp
        self.internet_users = internet_users
        self.un_continental_region = un_continental_region
        self.un_statistical_subregion = un_statistical_subregion
        self.population_2022 = population_2022
        self.population_2023 = population_2023
        self.population_change = population_change
        
    def __repr__(self) -> str:
        return f"{self.name} {self.total_surface} {self.land} {self.water} {self.water_percentage} {self.hdi} {self.hdi_growth} {self.imf_forcast_gdp} {self.world_bank_forecast_gdp} {self.un_forecast_gdp} {self.imf_forecast_gdp_ppp} {self.world_bank_forecast_gdp_ppp} {self.cia_forecast_gdp_ppp} {self.internet_users} {self.un_continental_region} {self.un_statistical_subregion} {self.population_2022} {self.population_2023} {self.population_change}"
    
    @classmethod
    def read_all_file(cls) -> None:
        """Reads values from buffer, creates country instances, and appends them to the countries list."""
        with open(file="/home/amnesia2/Documents/Data/Country_data.csv", mode='r') as buffer:
            for line in buffer:
                # Parse the line and create a new Country instance
                name, total_surface, land, water, water_percentage, hdi, hdi_growth, imf_forcast_gdp, world_bank_forecast_gdp, un_forecast_gdp, imf_forecast_gdp_ppp, world_bank_forecast_gdp_ppp, cia_forecast_gdp_ppp, internet_users, un_continental_region, un_statistical_subregion, population_2022, population_2023, population_change = line.strip().split(',')
                new_country = Country(name, total_surface, land, water, water_percentage, hdi, hdi_growth, imf_forcast_gdp, world_bank_forecast_gdp, un_forecast_gdp, imf_forecast_gdp_ppp, world_bank_forecast_gdp_ppp, cia_forecast_gdp_ppp, internet_users, un_continental_region, un_statistical_subregion, population_2022, population_2023, population_change)
                    
                # Append the new_country to the class variable countries
                cls.countries.append(new_country)

    @classmethod
    def remove_country(cls, index: int, country: "Country")->"Country":
        """remove item n the index specified

        Args:
            index (int): index of the value to remove
        """
        try:
            country = cls.countries.pop(index)
            return country
        except IndexError:
            print("Index Out of range!")
            exit(code = -1)
    
    @classmethod
    def append_country(cls, country: "Country")->None:
        """Appends a country object in the Country list

        Args:
            country (Country): Country object to insert
        """
        try:
            cls.countries.append(country)
        except ValueError:
            print("invalid type used")
            
    @classmethod
    def insert_country_in_x(cls, index: int, country: "Country")->None:
        """Inserts a country object in the Country list

        Args:
            index (int): index of new value 
            country (Country): Country object to insert
        """
        try:
            cls.countries.insert(index, country)
        except IndexError:
            print("Invalid index!")
            exit(code = -1)
            
    @classmethod
    def print_data(cls):
        print(cls.countries)
        
    @classmethod
    def create_threads(cls, index: int, country: "Country"):
        fetch_file_thread_start = perf_counter()
        fetch_file_thread = Thread(target=cls.read_all_file)
        fetch_file_thread.start()
        fetch_file_thread.join()
        fetch_file_thread_end = perf_counter()
        
        #--------------------------------------------------------
        
        append_country_thread_start = perf_counter()
        append_country_thread = Thread(target=cls.append_country, args=(country, ))
        append_country_thread.start()
        append_country_thread.join()
        append_country_thread_end = perf_counter()
        
        #--------------------------------------------------------
        
        remove_country_thread_start = perf_counter()
        remove_country_thread = Thread(target=cls.remove_country, args=(index, country))
        remove_country_thread.start()
        remove_country_thread.join()
        remove_country_thread_end = perf_counter()
        #--------------------------------------------------------
        
        insert_country_thread_start = perf_counter()
        insert_country_thread = Thread(target=cls.insert_country_in_x, args=(index, country, ))
        insert_country_thread.start()
        insert_country_thread.join()
        insert_country_thread_end = perf_counter()
        
        #--------------------------------------------------------
        
        print_data_start = perf_counter()
        print_data = Thread(target=cls.print_data)
        print_data.start()
        print_data.join()
        print_data_end = perf_counter()
        
        #--------------------------------------------------------
        system("clear")
        print("-------------------------Time taken by threads in lists of objects-------------------------")
        print(f"Data import from buffer:               {fetch_file_thread_end-fetch_file_thread_start:.7f} seconds")
        print(f"Appending a country:                   {append_country_thread_end-append_country_thread_start:.7f} seconds")
        print(f"Country removal from index {index}:          {remove_country_thread_end-remove_country_thread_start:.7f} seconds")
        print(f"Inserting in index {index}:                  {insert_country_thread_end-insert_country_thread_start:.7f} seconds")
        print(f"Printing data:                         {print_data_end-print_data_start:.7f} seconds")
        
        
        
def main():
    Country.create_threads(index= 2, coutry = Country())
    
    pass
if __name__ == '__main__':
    main()