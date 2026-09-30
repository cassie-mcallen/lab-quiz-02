# I have chosen data set C

# Calculate the overall average fish count

def average_fish_count(fish_counts):
	"""Display and return the average of the given fish counts."""
	if not fish_counts:
		average = 0
	else:
		average = sum(fish_counts) / len(fish_counts)
	print(average)
	return average

# Compare the average fish count between locations

def average_fish_count_per_location(location_a, location_b, location_c):
	"""Return each location's average and display the highest-average location."""
	if location_a:
		average_a = sum(location_a) / len(location_a)
	else:
		average_a = 0
	if location_b:
		average_b = sum(location_b) / len(location_b)
	else:
		average_b = 0
	if location_c:
		average_c = sum(location_c) / len(location_c)
	else:
		average_c = 0

	if average_a >= average_b and average_a >= average_c:
		print("Location A has the highest average:", average_a)
	elif average_b >= average_c:
		print("Location B has the highest average:", average_b)
	else:
		print("Location C has the highest average:", average_c)

	return average_a, average_b, average_c

#The result demonstrates that location X has the highest average fish count at X.