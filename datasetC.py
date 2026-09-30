# Calculate the overall average fish count


def average_fish_count(fish_counts):
	"""Display and return the average of the given fish counts."""
	if not fish_counts:
		average = 0
	else:
		average = sum(fish_counts) / len(fish_counts)
	print(average)
	return average

