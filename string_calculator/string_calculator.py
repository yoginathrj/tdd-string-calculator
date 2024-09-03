def string_calculator(numbers):
    # If the input string is empty, return 0
    if numbers == "":
        return 0
    
    delimiter = ","
    
    # Check if a custom delimiter is specified
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)  # Split the string into delimiter and number part
        delimiter = parts[0][2:]  # Extract the custom delimiter
        numbers = parts[1]  # Extract the actual numbers
    
    # Replace newline characters with the delimiter to handle multi-line inputs
    numbers = numbers.replace("\n", delimiter)
    
    # Convert the string of numbers into a list of integers
    num_list = list(map(int, numbers.split(delimiter)))

    # Check for any negative numbers in the list
    negative_numbers = [num for num in num_list if num < 0]
    if len(negative_numbers):
        # Raise an error if any negative numbers are found
        raise ValueError(f"Negative numbers not allowed: {negative_numbers}")    
    
    # Return the sum of the numbers in the list
    return sum(num_list)
