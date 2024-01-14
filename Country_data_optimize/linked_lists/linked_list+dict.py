from typing import Dict
from threading import *
from time import perf_counter                                   #Linked list: value is a dict that has the country data and a link
from os import system

class Node:
    def __init__(self, value: dict, link: "Node" = None) -> None:
        self.value = value
        self.link = link

class LinkedList:
    def __init__(self, head_node: Node) -> None:
        self.head_node = head_node
    
    def new_head(self, new_node: Node)->None:
        new_node.link = self.head_node
        self.head_node = new_node
        
    def remove_head(self)->None:
        if self.head_node:
            self.head_node = self.head_node.link
    
    def insert_node(self, index: int, new_node: Node)->None:
        if index == 0:
            self.new_head(new_node)
            return
        
        i = 1
        temporary_head = self.head_node
        while temporary_head.link is not None:
            if i == index:
                new_node.link = temporary_head.link
                temporary_head.link = new_node
                return
            temporary_head = temporary_head.link
            i += 1
            
    def remove_node(self, index: int)->None:
        if index == 0:
            self.remove_head()
            return

        i = 1
        temporary_head = self.head_node
        while temporary_head.link is not None:
            if i == (index-1) and temporary_head.link:
                temporary_head.link = temporary_head.link.link
                break
            temporary_head = temporary_head.link
            i += 1
    
    def print_content(self):
        temporary_head = self.head_node
        while temporary_head is not None:
            print(temporary_head.value)
            temporary_head = temporary_head.link
        

def read_file(linkedlist: LinkedList) -> None:
        """Reads values from buffer, creates the dict, creates node with the dict in it adds it to the linked list."""
        
        with open(file="/home/amnesia2/Documents/Data/Country_data.csv", mode='r') as buffer:
            for line in buffer:
                # Parse the line and create a new Country instance
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
                linkedlist.new_head(new_node= Node(value=country, link= linkedlist.head_node))
    
def make_threads(linkedlist: LinkedList, node: Node, index: int):
    thread_read_buffer_start = perf_counter()
    thread_read_buffer = Thread(target=read_file, args=(linkedlist, ))
    thread_read_buffer.start()
    thread_read_buffer.join()
    thread_read_buffer_end = perf_counter()
    #------------------------------------
        
    thread_new_head_start = perf_counter()
    thread_new_head = Thread(target=linkedlist.new_head, args=(node, ))
    thread_new_head.start()
    thread_new_head.join()
    thread_new_head_end = perf_counter()
    #------------------------------------
    
    thread_remove_head_start = perf_counter()
    thread_remove_head = Thread(target=linkedlist.remove_head)
    thread_remove_head.start()
    thread_remove_head.join()
    thread_remove_head_end = perf_counter()
    #------------------------------------
    
    thread_insert_node_start = perf_counter()
    thread_insert_node = Thread(target=linkedlist.insert_node, args=(index, node))
    thread_insert_node.start()
    thread_insert_node.join()
    thread_insert_node_end = perf_counter()
    #------------------------------------
    
    thread_remove_node_start = perf_counter()
    thread_remove_node = Thread(target=linkedlist.remove_node, args=(index, ))
    thread_remove_node.start()
    thread_remove_node.join()
    thread_remove_node_end = perf_counter()
    #------------------------------------
    
    thread_print_data_start = perf_counter()
    thread_print_data = Thread(target=linkedlist.print_content)
    thread_print_data.start()
    thread_print_data.join()
    thread_print_data_end = perf_counter()
    #------------------------------------
    
    system("clear")
    print("-------------------------Time taken by threads in linked lists of dicts-------------------------")
    print(f"Importing data:             {thread_read_buffer_end-thread_read_buffer_start:.7f} seconds")
    print(f"New head:                   {thread_new_head_end-thread_new_head_start:.7f} seconds")
    print(f"Remove node from {index}:         {thread_remove_node_end-thread_remove_node_start:.7f} seconds")
    print(f"Insert node in {index}:           {thread_insert_node_end-thread_insert_node_start:.7f} seconds")
    # print(f"Remove head:                {thread_remove_head_end-thread_remove_head_start:.7f} seconds")
    print(f"Printing data:              {thread_print_data_end-thread_print_data_start:.7f} seconds")

def main():
    node = Node(value={"link to work with": None}, link=None)
    linkedlist = LinkedList(head_node=Node(value={"first node": None}, link=None))
    make_threads(linkedlist=linkedlist, node=node, index= 2)
    
if __name__ == '__main__':
    main()