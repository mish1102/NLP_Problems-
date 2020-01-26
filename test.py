import csv

misspeled_cities_unique_id_list =[]
misspeled_cities_list =[]
# city = ''
def reader_file(file):
	with open(file,'r') as file:
		reader = csv.reader(file)
		for row in reader:
			city = row[0]
			misspeled_cities_list.append(city)
	# print(misspeled_cities_list)

def main():	
	with open('Correct_cities.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			city = row[0]
			unique_id = row[2]
			if(city not in misspeled_cities_list):
				# print(unique_id)
				misspeled_cities_unique_id_list.append(unique_id)
				# if(city!= misspeled_cities_list):
				# 	print(misspeled_cities_list)
		print(misspeled_cities_unique_id_list)


if __name__ == '__main__':
	file = 'Misspelt_cities.csv'
	reader_file(file)
	main()