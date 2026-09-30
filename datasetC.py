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


fish_count = [
	18, 43, 25, 24, 13, 35, 48, 23, 20, 27, 45, 57,
	26, 27, 22, 39, 29, 31, 29, 25, 38, 26, 20, 14,
	53, 25, 50, 28, 41, 30, 28, 36, 35, 21, 25, 24,
]
average_fish_count(fish_count)

# Compare the average fish count between sites

def average_fish_count_per_site(site_a, site_b, site_c):
	"""Display and return the average fish count for each site."""
	if site_a:
		average_a = sum(site_a) / len(site_a)
	else:
		average_a = 0
	if site_b:
		average_b = sum(site_b) / len(site_b)
	else:
		average_b = 0
	if site_c:
		average_c = sum(site_c) / len(site_c)
	else:
		average_c = 0

	if average_a >= average_b and average_a >= average_c:
		print("Site A has the highest average:", average_a)
	elif average_b >= average_c:
		print("Site B has the highest average:", average_b)
	else:
		print("Site C has the highest average:", average_c)

	return average_a, average_b, average_c


site_a = [18, 35, 20, 27, 29, 25, 20, 28, 35, 21, 25, 24]
site_b = [25, 24, 13, 23, 26, 27, 22, 29, 26, 14, 25, 28]
site_c = [43, 48, 45, 57, 39, 31, 38, 53, 50, 41, 30, 36]
average_fish_count_per_site(site_a, site_b, site_c)

#The result demonstrates that site X has the highest average fish count at X.