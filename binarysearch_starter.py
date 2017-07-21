import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)

# Start your search algorithm here.
#def binarySearch(alist, item):
 #   first = 0
#	    last = len(alist)-1
#	    found = False
	
 #   while first<=last and not found:
#	        midpoint = (first + last)//2
#	        if alist[midpoint] == item:
#	            found = True
#	        else:
#	            if item < alist[midpoint]:
#	                last = midpoint-1
#	            else:
#	                first = midpoint+1
#	
#	    return found
	
#	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
#	print(binarySearch(testlist, 3))

#	print(binarySearch(testlist, 13))