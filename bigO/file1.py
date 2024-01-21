from time import perf_counter

def test1(size_list: int, index_insertion):
	
	# allocates list size
	start_creation = perf_counter()
	list1 = [0] * size_list 
	end_creation = perf_counter()
	total_creation = end_creation - start_creation

	start_append = perf_counter()
	for i in range(0, size_list):
		list1.append(i)
	end_append = perf_counter()
	total_append = end_append - start_append

	start_insertion = perf_counter()
	list1.insert(index_insertion, "A")
	end_insertion = perf_counter()
	total_insertion = end_insertion - start_creation

	return total_creation, total_append, total_insertion  

def main():
	start = perf_counter()
	size = 100000
	index = 90000
	total_creation, total_append, total_insertion = test1(size, index)
	end = perf_counter()
	
	with open(file = "/home/amnesia2/Documents/Python_Projects/Py_Optimize/bigO/file1.log", mode = 'a') as f:
		f.write(f"--------List_size: {size} Insertion Index:  {index}-------\n")
		f.write(f"Creation time: {total_creation:.7f}\n")
		f.write(f"Appending time: {total_append:.7f}\n")
		f.write(f"Insertion time: {total_insertion:.7f}\n")
		f.write(f"Total time: {end-start:.7f}\n")
		f.write(f"-----------------------------------\n")	

if __name__ == '__main__':
	main()

