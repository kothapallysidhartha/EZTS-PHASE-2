#subsequence  question
"""the continious and non continious subsequence of a string/data structure is called subsequence
"""
def subsequences(index, current, s):
    # Base Case: If index reaches the end of the string
    if index == len(s):
        print(current)  # Print or store the subsequence
        return

    # Step 1: Include the current character
    subsequences(index + 1, current + s[index], s)

    # Step 2: Exclude the current character
    subsequences(index + 1, current, s)

# Example Usage
s = "abc"
subsequences(0, "", s)
