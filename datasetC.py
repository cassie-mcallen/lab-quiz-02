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

#The result demonstrates that site A has the highest average fish count at 42.58. This is above the average fish count across all sites, which is 30.56, meaning that site A is above the general trend in fish population.

#Data Visualisation chart

fish_records = [
	("Site A", "Jan", 18), ("Site C", "Feb", 43), ("Site B", "Feb", 25),
	("Site B", "Feb", 24), ("Site B", "Jan", 13), ("Site A", "Feb", 35),
	("Site C", "Mar", 48), ("Site B", "Feb", 23), ("Site A", "Jan", 20),
	("Site A", "Mar", 27), ("Site C", "Feb", 45), ("Site C", "Mar", 57),
	("Site B", "Mar", 26), ("Site B", "Feb", 27), ("Site B", "Jan", 22),
	("Site C", "Mar", 39), ("Site A", "Jan", 29), ("Site C", "Jan", 31),
	("Site B", "Jan", 29), ("Site A", "Feb", 25), ("Site C", "Jan", 38),
	("Site B", "Mar", 26), ("Site A", "Mar", 20), ("Site B", "Mar", 14),
	("Site C", "Feb", 53), ("Site B", "Jan", 25), ("Site C", "Feb", 50),
	("Site B", "Mar", 28), ("Site C", "Mar", 41), ("Site C", "Jan", 30),
	("Site A", "Mar", 28), ("Site C", "Jan", 36), ("Site A", "Feb", 35),
	("Site A", "Feb", 21), ("Site A", "Mar", 25), ("Site A", "Jan", 24),
]

fish_totals = {}
record_counts = {}
for site, month, count in fish_records:
	key = (site, month)
	if key not in fish_totals:
		fish_totals[key] = 0
		record_counts[key] = 0
	fish_totals[key] += count
	record_counts[key] += 1

site_symbols = {"Site A": "A", "Site B": "B", "Site C": "C"}

print("\nAverage Fish Count by Site and Month")
print("Average fish count; each symbol is about one fish")
print("Bar key: A = Site A, B = Site B, C = Site C")
print("Location / Month | 0         10        20        30        40        50")
for month in ("Jan", "Feb", "Mar"):
	for site in ("Site A", "Site B", "Site C"):
		key = (site, month)
		if key in fish_totals:
			average = fish_totals[key] / record_counts[key]
			bar = site_symbols[site] * round(average)
			print(f"{site} {month:>3}          | {bar} {average:.2f}")

#The chart demonstrates that across all months, site C has a significantly higher average fish count in comparison to sites A and B. 
#The chart also shows that January is the month with the lowest average fish counts across all sites, while Febuary had the highest.