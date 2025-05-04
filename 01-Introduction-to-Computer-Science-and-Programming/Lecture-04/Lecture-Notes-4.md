# Lecture 4 - Loops over Strings, Guess-and-Check, Binary
> **Topic Overview:** interation, guess and check, binary, fractions
### Break Statements
- Imediately exits whateber loop it is in
- Skips remaining expressions in code block
- Exits only innermost loop
- ```
  my sum = 0
  for i in range(5):
    if i == 4:
      break
### Strings and Loops
- Code to check for letter i or u in a string
- ```
  for char in s:
    if char in 'iu':
      print("There is a i or u")
### Guess-and-check
- Process called exhaustive enumaration
- Applies to a problem where:
  - You are able to guess a value for solution
  - You are able to check if the solution is correct
- You can keep guessing until:
  - you find the solution or
  - have guessed all values
### Binary Numbers
- Numbers (and everything else) are represented as a sequence of bits (0 or 1)
- When we write numbers down, the notation uses base 10
- This produces **cognitive dissonance** - and it will influence how we write code
- Operations on some floats introduces a very small error
