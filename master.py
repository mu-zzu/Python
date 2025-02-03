
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

threshold = int(input("Enter the threshold number: "))


filtered_numbers = [num for num in numbers if num < threshold]

print("Numbers less than", threshold, ":", filtered_numbers)
