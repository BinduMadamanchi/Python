
def unique_longest_substring(input1):
#initialising the requried instances
  lastOccurrence = {}
  longestLength = 0
  longestPosition = 0
  startingPosition = 0
  currentLength = 0
  for a, b in enumerate(input1): #enumerate() function is used to iterate through a list while keeping track of the list items' indices
    l = lastOccurrence.get(b, -1)
    # If no repetition within, no problems.
    if l < startingPosition:
        currentLength += 1
    else:
        # Check if it is the longest so far
        if currentLength > longestLength:
            longestPosition = startingPosition
            longestLength = currentLength
        # Cut the prefix that has repetition
        currentLength -= l - startingPosition
        startingPosition = l + 1
    # In any case, update last occurrence
    lastOccurrence[b] = a
  # if the longest substring is a suffix
  if currentLength > longestLength:
    longestPosition = startingPosition
    longestLength = currentLength
  return input1[longestPosition:longestPosition + longestLength]
print("Enter the input String :")
user_input = input()
print(f"The Longest unique substring in the given string is '{unique_longest_substring(user_input)}',{len(unique_longest_substring(user_input))}")