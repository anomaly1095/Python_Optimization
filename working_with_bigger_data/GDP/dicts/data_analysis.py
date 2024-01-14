from typing import List
from threading import *
from matplotlib import pyplot as plt
from multiprocessing import Process
from psutil import virtual_memory
from time import perf_counter

def read_buffer(countries: List[dict]) -> None:
        """Reads values from buffer, creates the dict, appends fdict to list."""
        
        with open(file="/home/amnesia2/Documents/Data/GDP/gdp.csv", mode='r') as buffer:
            for line in buffer:
                name, gdp1980, gdp1981, gdp1982, gdp1983, gdp1984, gdp1985, gdp1986, gdp1987, gdp1988, gdp1989, gdp1990, gdp1991, gdp1992, gdp1993, gdp1994, gdp1995, gdp1996, gdp1997, gdp1998, gdp1999, gdp2000, gdp2001, gdp2002, gdp2003, gdp2004, gdp2005, gdp2006, gdp2007, gdp2008, gdp2009, gdp2010, gdp2011, gdp2012, gdp2013, gdp2014, gdp2015, gdp2016, gdp2017, gdp2018, gdp2019, gdp2020, gdp2021, gdp2022, gdp2023, gdp2024, gdp2025, gdp2026, gdp2027, gdp2028 = line.strip().split(',')
                country = {'name': name, 'GDP 1980': gdp1980, 'GDP 1981': gdp1981, 'GDP 1982': gdp1982, 'GDP 1983': gdp1983, 'GDP 1984': gdp1984, 'GDP 1985': gdp1985, 'GDP 1986': gdp1986, 'GDP 1987': gdp1987, 'GDP 1988': gdp1988, 'GDP 1989': gdp1989, 'GDP 1990': gdp1990, 'GDP 1991': gdp1991, 'GDP 1992': gdp1992, 'GDP 1993': gdp1993, 'GDP 1994': gdp1994, 'GDP 1995': gdp1995, 'GDP 1996': gdp1996, 'GDP 1997': gdp1997, 'GDP 1998': gdp1998, 'GDP 1999': gdp1999, 'GDP 2000': gdp2000, 'GDP 2001': gdp2001, 'GDP 2002': gdp2002, 'GDP 2003': gdp2003, 'GDP 2004': gdp2004, 'GDP 2005': gdp2005, 'GDP 2006': gdp2006, 'GDP 2007': gdp2007, 'GDP 2008': gdp2008, 'GDP 2009': gdp2009, 'GDP 2010': gdp2010, 'GDP 2011': gdp2011, 'GDP 2012': gdp2012, 'GDP 2013': gdp2013, 'GDP 2014': gdp2014, 'GDP 2015': gdp2015, 'GDP 2016': gdp2016, 'GDP 2017': gdp2017, 'GDP 2018': gdp2018, 'GDP 2019': gdp2019, 'GDP 2020': gdp2020, 'GDP 2021': gdp2021, 'GDP 2022': gdp2022, 'GDP 2023': gdp2023, 'GDP 2024': gdp2024, 'GDP 2025': gdp2025, 'GDP 2026': gdp2026, 'GDP 2027': gdp2027, 'GDP 2028': gdp2028}
                countries.append(country)
                
def create_graph(countries: List[dict]):
    start = perf_counter()
    for country in countries:
        name = country['name']
        values = list(country.values())[1:]
        
        plt.plot(range(1, len(values)+1), values, marker='o', label=name)
        plt.xlabel("Year")
        plt.ylabel("GDPs")
        plt.title(f"{name} data visualisation")
        plt.savefig(f"/home/amnesia2/Documents/Graphs/GDP/{name}.png")
        plt.clf()
    plt.close()
    end = perf_counter()
    with open("/home/amnesia2/Documents/Python_Projects/working_with_bigger_data/GDP/dicts/memory_usage.log", 'a') as f:
        memory_info = virtual_memory()
        f.write(f"{end - start:.7f} s\tUsed: {memory_info.used / (1024 ** 2):.2f} MB\tFree: {memory_info.free / (1024 ** 2):.2f} MB\tAvailable: {memory_info.available / (1024 ** 2):.2f} MB\tTotal: {memory_info.total / (1024 ** 2):.2f} MB\tPercent: {memory_info.percent:.2f}%\n")

def data_processes(countries: List[dict]):
    list1 = countries[0:57]
    list2 = countries[57:114]
    list3 = countries[114:171]
    list4 = countries[171:228]
    #--------------------------------------
    process1 = Process(target= create_graph, args= (list1, ))
    process1.start()
    #--------------------------------------
    process2 = Process(target= create_graph, args= (list2, ))
    process2.start()
    #--------------------------------------
    process3 = Process(target= create_graph, args= (list3, ))
    process3.start()
    #--------------------------------------
    process4 = Process(target= create_graph, args= (list4, ))
    process4.start()
    #--------------------------------------
    
def main():
    countries: List[dict] = []
    read_buffer(countries=countries)
    data_processes(countries=countries)
    
if __name__ == '__main__':
    main()