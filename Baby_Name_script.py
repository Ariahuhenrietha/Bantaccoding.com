import re
import os

# File path to the text file
text_file_path = r'C:\Users\HP\OneDrive\Desktop\PYTHON PROGRAMMS\full_name.txt'

# Read the file
with open(text_file_path, 'r') as file:
    full_name = file.read().strip()

# Extract first name, middle name, and last name
names = full_name.split()
first_name = names[0]
middle_name = names[1]
last_name = names[2]

# Print the extracted names
print(f"First Name: {first_name}")
print(f"Middle Name: {middle_name}")
print(f"Last Name: {last_name}")

# Print the local file path
print(f"Local File Path: {os.path.abspath(text_file_path)}")

# Quick sort algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Binary search algorithm
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Define the path to the HTML file
html_file_path = r'C:\Users\HP\OneDrive\Desktop\PYTHON PROGRAMMS\baby2008.html'

# Read the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Extract baby names using regex (example assuming names are in <td> tags)
name_pattern = re.compile(r'<td>(\w+)</td>')
baby_names = name_pattern.findall(html_content)

# Remove duplicates and sort the names using quicksort
unique_baby_names = sorted(set(baby_names))
sorted_baby_names = quicksort(unique_baby_names)

# Print the sorted baby names
print(f"Sorted Baby Names: {sorted_baby_names}")

# Example usage of binary search
target_name = "David"
index = binary_search(sorted_baby_names, target_name)
if index != -1:
    print(f"Name '{target_name}' found at index {index}.")
else:
    print(f"Name '{target_name}' not found in the list.")
