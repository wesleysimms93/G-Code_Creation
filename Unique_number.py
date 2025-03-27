def test_unique_number():
    # Generate 40 test cases with pairs of numbers
    test_cases = [i for i in range(1,7924)]  # Example: [(0, 1), (1, 2), ..., (39, 40)]
    x_cases = [i for i in range(1,7924)]  # Example: [(0, 1), (1, 2), ..., (39, 40)]
    y_cases = [i for i in range(1,1524)]  # Example: [(0, 1), (1, 2), ..., (39, 40)]
    # Use a set to track unique results
    unique_results = set()
    
    for num1 in x_cases:
        for num2 in y_cases:
            # Call the unique_number function
            result = unique_number(num1, num2)
            
            # Print inputs and outputs for verification
            #print(f"unique_number({num1}, {num2}) -> {result}")
            
            # Check if the result is already in the set
            if result in unique_results:
                print(f"Test failed: Duplicate result {result} found for inputs {num1}, {num2}")
                return False
            
            # Add the result to the set
            unique_results.add(result)
    
    # Verify that the number of unique results matches the number of test cases
    #assert len(unique_results) == len(test_cases), "Test failed: Duplicate or missing results"
    
    print("All test cases passed! No duplicates found.")
    return True

# Example implementation of unique_number function
def unique_number(num1, num2):
    # Combine num1 and num2 uniquely using a mathematical approach
    return num1 +100 * num2

# Run the test
test_unique_number()