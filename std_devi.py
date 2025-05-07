# Step 1: Raw data
values = [500, 600, 1200, 1000, 400, 900]

# Step 2: Calculate mean (x̄)
n = len(values)
mean = sum(values) / n

# Step 3: Calculate squared differences (xi - x̄)²
squared_diffs = []
for value in values:
    diff = value - mean
    squared_diffs.append(diff ** 2)

# Step 4: Calculate variance (using (n - 1) for sample variance)
variance = sum(squared_diffs) / (n - 1)

# Step 5: Calculate standard deviation (s)
std_deviation = variance ** 0.5

# Output
print("Mean (x̄):", mean)
print("Variance (s²):", variance)
print("Sample Standard Deviation (s):", std_deviation)
