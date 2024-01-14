from typing import List
from threading import *
from time import perf_counter                                                                                   #230 countries    48 years of data
from os import system

class Country:
    countries: List["Country"] = []
    
    def __init__(
        self,
        name: str = '',
        gdp1980: float = 0.0,
        gdp1981: float = 0.0,
        gdp1982: float = 0.0,
        gdp1983: float = 0.0,
        gdp1984: float = 0.0,
        gdp1985: float = 0.0,
        gdp1986: float = 0.0,
        gdp1987: float = 0.0,
        gdp1988: float = 0.0,
        gdp1989: float = 0.0,
        gdp1990: float = 0.0,
        gdp1991: float = 0.0,
        gdp1992: float = 0.0,
        gdp1993: float = 0.0,
        gdp1994: float = 0.0,
        gdp1995: float = 0.0,
        gdp1996: float = 0.0,
        gdp1997: float = 0.0,
        gdp1998: float = 0.0,
        gdp1999: float = 0.0,
        gdp2000: float = 0.0,
        gdp2001: float = 0.0,
        gdp2002: float = 0.0,
        gdp2003: float = 0.0,
        gdp2004: float = 0.0,
        gdp2005: float = 0.0,
        gdp2006: float = 0.0,
        gdp2007: float = 0.0,
        gdp2008: float = 0.0,
        gdp2009: float = 0.0,
        gdp2010: float = 0.0,
        gdp2011: float = 0.0,
        gdp2012: float = 0.0,
        gdp2013: float = 0.0,
        gdp2014: float = 0.0,
        gdp2015: float = 0.0,
        gdp2016: float = 0.0,
        gdp2017: float = 0.0,
        gdp2018: float = 0.0,
        gdp2019: float = 0.0,
        gdp2020: float = 0.0,
        gdp2021: float = 0.0,
        gdp2022: float = 0.0,
        gdp2023: float = 0.0,
        gdp2024: float = 0.0,
        gdp2025: float = 0.0,
        gdp2026: float = 0.0,
        gdp2027: float = 0.0,
        gdp2028: float = 0.0,
    ) -> None:
        self.name = name
        self.gdp1980 = gdp1980
        self.gdp1981 = gdp1981
        self.gdp1982 = gdp1982
        self.gdp1983 = gdp1983
        self.gdp1984 = gdp1984
        self.gdp1985 = gdp1985
        self.gdp1986 = gdp1986
        self.gdp1987 = gdp1987
        self.gdp1988 = gdp1988
        self.gdp1989 = gdp1989
        self.gdp1990 = gdp1990
        self.gdp1991 = gdp1991
        self.gdp1992 = gdp1992
        self.gdp1993 = gdp1993
        self.gdp1994 = gdp1994
        self.gdp1995 = gdp1995
        self.gdp1996 = gdp1996
        self.gdp1997 = gdp1997
        self.gdp1998 = gdp1998
        self.gdp1999 = gdp1999
        self.gdp2000 = gdp2000
        self.gdp2001 = gdp2001
        self.gdp2002 = gdp2002
        self.gdp2003 = gdp2003
        self.gdp2004 = gdp2004
        self.gdp2005 = gdp2005
        self.gdp2006 = gdp2006
        self.gdp2007 = gdp2007
        self.gdp2008 = gdp2008
        self.gdp2009 = gdp2009
        self.gdp2010 = gdp2010
        self.gdp2011 = gdp2011
        self.gdp2012 = gdp2012
        self.gdp2013 = gdp2013
        self.gdp2014 = gdp2014
        self.gdp2015 = gdp2015
        self.gdp2016 = gdp2016
        self.gdp2017 = gdp2017
        self.gdp2018 = gdp2018
        self.gdp2019 = gdp2019
        self.gdp2020 = gdp2020
        self.gdp2021 = gdp2021
        self.gdp2022 = gdp2022
        self.gdp2023 = gdp2023
        self.gdp2024 = gdp2024
        self.gdp2025 = gdp2025
        self.gdp2026 = gdp2026
        self.gdp2027 = gdp2027
        self.gdp2028 = gdp2028
        
    def __repr__(self) -> str:
        return f"{self.name}"
    
    @classmethod
    def read_all_file(cls) -> None:
        """Reads values from buffer, creates country instances, and appends them to the countries list."""
        with open(file="/home/amnesia2/Documents/Data/GDP/gdp.csv", mode='r') as buffer:
            i = 0
            for line in buffer:
                # Parse the line and create a new Country instance
                name, gdp1980, gdp1981, gdp1982, gdp1983, gdp1984, gdp1985, gdp1986, gdp1987, gdp1988, gdp1989, gdp1990, gdp1991, gdp1992, gdp1993, gdp1994, gdp1995, gdp1996, gdp1997, gdp1998, gdp1999, gdp2000, gdp2001, gdp2002, gdp2003, gdp2004, gdp2005, gdp2006, gdp2007, gdp2008, gdp2009, gdp2010, gdp2011, gdp2012, gdp2013, gdp2014, gdp2015, gdp2016, gdp2017, gdp2018, gdp2019, gdp2020, gdp2021, gdp2022, gdp2023, gdp2024, gdp2025, gdp2026, gdp2027, gdp2028 = line.strip().split(',')
                new_country = Country(name, gdp1980, gdp1981, gdp1982, gdp1983, gdp1984, gdp1985, gdp1986, gdp1987, gdp1988, gdp1989, gdp1990, gdp1991, gdp1992, gdp1993, gdp1994, gdp1995, gdp1996, gdp1997, gdp1998, gdp1999, gdp2000, gdp2001, gdp2002, gdp2003, gdp2004, gdp2005, gdp2006, gdp2007, gdp2008, gdp2009, gdp2010, gdp2011, gdp2012, gdp2013, gdp2014, gdp2015, gdp2016, gdp2017, gdp2018, gdp2019, gdp2020, gdp2021, gdp2022, gdp2023, gdp2024, gdp2025, gdp2026, gdp2027, gdp2028)
                    
                # Append the new_country to the class variable countries
                cls.countries.append(new_country)
                print(cls.countries[i].gdp1983)
                i += 1

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
        
        country = Country()
        append_country_thread_start = perf_counter()
        append_country_thread = Thread(target=cls.append_country, args=(country, ))
        append_country_thread.start()
        append_country_thread.join()
        append_country_thread_end = perf_counter()
        
        #--------------------------------------------------------
        
        remove_country_thread_start = perf_counter()
        remove_country_thread = Thread(target=cls.remove_country, args=(index, country, ))
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
    Country.create_threads(index= 2, country= Country(name="tata"))
    
    pass
if __name__ == '__main__':
    main()