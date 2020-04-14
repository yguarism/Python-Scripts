# This program creates a workout regiment based on a CSV List of Exercises created by the User
# Input: CSV
# Output: Text File Workout
# Yrina Guarisma
import os
import itertools
import csv
import re
import sys
from random import seed
from random import randint
from fbchat import Client
from fbchat.models import *

class Exercise:
	name = ""
	primGroup = ""
	secondGroup = ""

	def __init__(self, name, PG, SG):
		self.name = name
		self.primGroup = PG
		self.secondGroup = SG
	def __str__(self):
		return "Name: {}, Primary Group: {}, Secondary Group: {}".format(self.name, self.primGroup, self.secondGroup)
	def __eq__(self, other):
		if self.name == other.name:
			if self.primGroup == other.primGroup:
				if self.secondGroup == other.secondGroup:
					return True
		return False
# Reads the CSV File
def readCSV (filename):
	exercises_list = []
	counts = {"Abs": 0, "Back": 0, "Chest": 0, "Legs": 0}
	with open(filename, "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			if row["Primary Group"] in counts:
				temp = Exercise(row["Name"], row["Primary Group"], row["Secondary Group"])
				counts[row["Primary Group"]] += 1
				exercises_list.append(temp)
			else:
				print("Error: Invalid Primary Group for Entry: {}. Please Fix the CSV.".format(row["Name"]))
			
		f.close()

	return exercises_list, counts

# Chooses Exercises for routine
def chooseFullExercises (exercise_list, num_exercises):
	PG_count = {"Abs":0, "Back":0, "Chest":0, "Legs":0}
	SG_count = {}
	routine = []
	min_PG = 0
	threshhold = int(num_exercises/2)
	
	while min_PG < num_exercises:
		found = False
		# Choose a random exercise from the list
		seed()
		index = randint(0, len(exercise_list)-1)
		exercise = exercise_list[index]
		
		# Check if exercise already exists in routine
		for exer in routine:
			if exercise == exer:
				found = True
				break

		print (exercise)
		print (PG_count.get(exercise.primGroup, -1))
		print (SG_count.get(exercise.secondGroup, -2))
		# Only check if exercise not in routine already
		if found == False:
			# Check the primary group of the exercise has not reached threshhold
			if PG_count.get(exercise.primGroup, -1) < num_exercises:
				# Error Case for Incorrect Group Naming
				if PG_count.get(exercise.primGroup, -1) == -1:
					print(exercise)
					print("Naming Error for Above Exercise, Please Fix!")
				
				# Check the secondary group of the exercise has not reached threshhold
				elif SG_count.get(exercise.secondGroup, -2) < threshhold:
					# Add exercise to routine
					routine.append(exercise)
					 
					# Add Primary group added to routine in count dictionary
					PG_count[exercise.primGroup] += 1

					# Add Secondary group to count dictionary if not blank
					if exercise.secondGroup != "":
						if SG_count.get(exercise.secondGroup, -2) == -2:
							SG_count[exercise.secondGroup] = 1
						else:
							SG_count[exercise.secondGroup] += 1
					min_PG = min(PG_count.values()) 

	return routine

# Helps Choose random exercises from a specific Muscle Type
def chooseSpecificExercise(exercise_type, exercise_list, num_exercises, routine):
	SG_count = {}
	count_numexercises_added = 0

	if num_exercises > 3:
		threshhold = int(num_exercises/2)
	else:
		threshhold = int(num_exercises)
	# Choose a random exercise from the list
	while count_numexercises_added < num_exercises:
		found = False
		seed()
		index = randint(0, len(exercise_list)-1)
		exercise = exercise_list[index]
		# Check if exercise already exists in routine
		for exer in routine:
			if exercise == exer:
				found = True
				break
		
		# Only check if exercise not in routine already
		if found == False:
			if exercise.primGroup == exercise_type:
				if SG_count.get(exercise.secondGroup, -2) < threshhold:
					if exercise.secondGroup != "":
						if SG_count.get(exercise.secondGroup, -2) == -2:
							SG_count[exercise.secondGroup] = 1
						else:
							SG_count[exercise.secondGroup] += 1

					routine.append(exercise)
					count_numexercises_added += 1	

# Find first element in routine with a specific Primary Group Name	
def matchExer (name, routine):
	for exercise in routine:
		if exercise.primGroup.lower() == name.lower():
			routine.remove(exercise)
			return routine, exercise

# Orders the routine in a random order of Abs, Legs, Back, Chest alternating
def OrderFullRoutine(group_names, routine, num_exercises):
	ordered_routine = []
	order_options = list(map(" ".join, itertools.permutations(group_names)))
	
	# Choose a random order for the exercises to be in
	seed()
	index = randint(0, len(order_options)-1)
	order = order_options[index].split()
	print(order)

	for i in range(0, num_exercises):
		for name in order:
			routine, exercise = matchExer(name, routine)
			ordered_routine.append(exercise)

	return ordered_routine

def writetoText (filename, routine):
	with open(filename, "w+") as f:
		f.write("The Exercise Routine: \n")
		for exercise in routine:
			f.write(exercise.name + "\n")

def fbMessage(routine):
	client = Client('yrinamaple@gmail.com', '<3volleyball14')
	text = []
	for item in routine:
		text.append(item.name)
	txt = ', '.join(text)
	print(txt)
	input("w")
	users = client.searchForUsers('Lucas Pilozo-Hibbit')
	person_id = users[0].uid
	print(users)
	input("w")
	#print(person_id)
	client.send(Message(text= "This is sent from my program :P. Your fun Routine is: {}".format(txt)), thread_id = person_id, thread_type = ThreadType.USER)

	client.logout()


def main():

	print("Welcome! This program has been designed to create a random workout routine just for you :) ")
	
	valid_musclegroups = ["abs", "legs", "chest", "back"]
	routine = []
	
	# Open the CSV File, Return 1 List of Exercise Objects
	filename = os.getcwd() + r"\exercises.csv"
	exercises_list, counts = readCSV(filename)
	
	# Number of Muscle Groups Desired in Workout
	num_musclegroups = input("How many Groups do you want to work? (1,2,3, or 4): ")
	# Create a Full Body Workout if user chooses 4
	if "4" in num_musclegroups.lower():
		print("Full-Body Workout")
		group_names = ["Abs", "Legs", "Back", "Chest"]
		# full body exercise this is how many of each is desired
		num_exercises = int(input("How many exercises per muscle group? "))
		
		if num_exercises > min(counts.values()):
			print("Error: Not Enough Exercises to complete this Request. Add more Exercises")
			sys.exit(0)
		else:
			routine = chooseFullExercises (exercises_list, num_exercises)

			# Order Exercises Properly 
			ordered_routine = OrderFullRoutine(group_names, routine, num_exercises)

	# Create a workout with 3, 2, 1 muscle groups
	else:
		group_names = input("Which Muscle Groups? (Abs, Legs, Chest, Back): ")
		# Error case: Must input names separated by a space
		w = re.search(r"[0-9,.;:\"\'+\-_!@#]", group_names)
		if w != None:
			print("Error: Invalid Characters Found")
			sys.exit(0)

		group_names = group_names.split(" ")
		# Error Case for Mismatch b/w number of muscle groups desired and number muscle groups entered
		if len(group_names) != int(num_musclegroups):
			print("Error: Number Muscle Groups Desired, Not Equal Number of Muscle Groups Entered")
			sys.exit(0)

		num_exercises = int(input("How many exercises per muscle group? "))
		
		# Error Case for not enough entries
		if num_exercises > min(counts.values()):
			print("Error: Not Enough Exercises to complete this Request. Add more Exercises")
			sys.exit(0)

		# Error Case for if one of the entrys is not abs, legs, chest, back
		for group in group_names:
			if group.lower() not in valid_musclegroups:
				print("Error: Entry must be either Abs, Back, Chest, Legs")
				sys.exit(0)
		
			chooseSpecificExercise(group, exercises_list, num_exercises, routine)
			for elem in routine:
				print(elem)
		
		ordered_routine = OrderFullRoutine(group_names, routine, num_exercises)

	

	# Create Output File and Open Text File for User
	outputfilename = os.getcwd() + r"\routine.txt"
	
	#fbMessage(ordered_routine)
	writetoText(outputfilename, ordered_routine)
	os.startfile(outputfilename)
	

if __name__ =="__main__":
	main()