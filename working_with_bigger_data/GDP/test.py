def writefile():
  with open("/home/amnesia2/Documents/Python_Projects/working_with_bigger_data/GDP/test.txt", 'a') as buffer:
    for i in range(1979, 2029):
      if i == 1979:
          buffer.write("country.name, ")
      else:
          buffer.write(f"gdp.gdp{i}, ")

writefile()
