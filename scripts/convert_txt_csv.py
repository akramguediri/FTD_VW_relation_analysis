# Open the text file for reading
with open('../data/FTD.txt', 'r') as f:
    lines = f.readlines()

# Remove trailing newline characters
lines = [line.strip() for line in lines]

# Replace '|' with ',' for each line except the header
csv_lines = [lines[0]]  # Header line as is
csv_lines.extend([line.replace(',', ' ').replace('|', ',') for line in lines[1:]])

# Write the modified content to a new CSV file
with open('../data/ftd_data.csv', 'w') as f:
    f.write('\n'.join(csv_lines))
