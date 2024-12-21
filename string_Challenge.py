def StringChallenge(strParam):
    # Initialize a variable to keep track of the maximum number of unique characters
    max_unique = 0
    
    # Outer loop: Iterate through each character in the string (strParam) one by one
    for i in range(len(strParam)):
        
        # Inner loop: Start from the next character after 'i' and iterate to the end of the string
        for j in range(i + 1, len(strParam)):
            
            # If characters at positions i and j are the same, we have found a substring 
            # between those two positions where the characters are identical at both ends.
            if strParam[i] == strParam[j]:
                
                # Extract the substring between the characters at positions i and j (not including i and j)
                substring = strParam[i + 1:j]
                
                # Calculate the number of unique characters in the substring by converting it to a set
                unique_chars = len(set(substring))
                
                # Update max_unique if the number of unique characters in the current substring is greater
                # than the previous maximum value
                max_unique = max(max_unique, unique_chars)
    
    # After iterating through all possible pairs of characters, return the maximum number of unique characters found
    return max_unique

# Test the function with user input
print(StringChallenge(input()))  # Accepts an input string and calls the StringChallenge function
