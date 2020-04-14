# Allows access to read and modify inventory.csv
# Yrina Guarisma
# April 2020

import os
import csv


# Reads the CSV File
def readCSV (filename):
	item_list = []
	with open(filename, "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			item_list.append(row)
			
		f.close()
	return item_list


# Adds a line to the bottom of the inventory.csv File
def appendtoCSV(filename, line):
	with open(filename, "a") as f:
		f.write(line)
		f.write('\n')

# Rewrites CSV rows
def addNewValuesCSV (filename, dict_data):
	csv_columns = ['Location in Kitchen', 'Quantity', 'Item', 'Expiry Date', 'Need to Buy']
	with open(filename, 'w', newline = '') as f:
		writer = csv.DictWriter(f, fieldnames=csv_columns)
		writer.writeheader()
		for data in dict_data:
			writer.writerow(data)


# Print Formatting for an inventory item
def printItem (item):
	print("Matching Iventory Item(s):")
	for name, value in item.items(): 
		if name == "Item":
			print("{}: {}".format(name, value.upper()))
		else:
			print("{}: {}".format(name, value))
		
	print('\n')

# Main Function
def main():
	filename = os.getcwd() + r"\inventory.csv"
	items = readCSV(filename)
	keepGoing = False

	while keepGoing == False:
		action = input("Select a Number - 1: Query Item, 2: Add to List, 3: Modify Entry, 4: Items in Location ")

		if action == "1":
			okay = 0
			item_name = input("What is the item name? ")
			for item in items:
				if item_name.lower() in item["Item"].lower():
					printItem(item)
					okay = 1
			if okay == 0:
				print("No Items Found with that Name")
			
		if action == "4":
			okay = 0
			item_loc = input("What is the location you wish to search? ")
			for item in items:
				if item_loc.lower() in item["Location in Kitchen"].lower():
					printItem(item)
					okay = 1
			if okay == 0:
				print("No Items Found to that Location")

	
		if action == "2":
			new_item_name = input("What is the New Item Name?")
			new_item_location = input("What is the New Item Location?")
			new_item_Qu = input("What is the New Item Quantity?")
			new_item_NTB = input("Need to Buy?")
			new_item_Expiry = input("What is the New Item Expiry Year?")

			new_item_string = new_item_location + ', ' + new_item_Qu + ', ' + new_item_name  + ', ' + new_item_Expiry + ', ' + new_item_NTB
			print(new_item_string)
			appendtoCSV(filename, new_item_string)

	
		if action == "3":
			item_name = input("What is the item you wish to modify?")
			for item in items:
				if item_name.lower() in item["Item"].lower():
					printItem(item)
					isYes = input("Is this the item you wish to modify? Type y for yes: ")

					if 'y' in isYes.lower():
						category = input("Modify: Quantity, Location, Name, Expiry date, Need to Buy? ")
					
						if "q" in category.lower():
							new_quantity = input("What is the new quantity? ") 
							item["Quantity"] = new_quantity

						if "l" in category.lower():
							new_quantity = input("What is the new location? ") 
							item["Location in Kitchen"] = new_quantity

						if "n" in category.lower():
							new_quantity = input("What is the new name? ") 
							item["Name"] = new_quantity

						if "e" in category.lower():
							new_quantity = input("What is the new expiry date? ") 
							item["Expiry Date"] = new_quantity

						if "b" in category.lower():
							new_quantity = input("What is the new Need to Buy Status? ") 
							item["Need to Buy"] = new_quantity

						break
		
			addNewValuesCSV(filename, items)

		# Adding Function for user to use program again
		question = input("Would you like to use this progam again? 'y' for Yes, 'n' for No: ")
		if 'n' in question.lower():
			keepGoing = True

if __name__ =="__main__":
	main()
