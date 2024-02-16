import csv
with open('samplecsv.csv') as file_obj:
	reader_obj = csv.DictReader(file_obj)
	for row in reader_obj:
		print(row)
