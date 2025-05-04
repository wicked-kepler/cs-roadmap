# Lecture 5 - Float and Approximation Methods
> **Topic Overview:** approximation methods, floats

### Fraction representation
- In decimal form: 3/8 = 0.375 = 3\*10<sup>-1</sup> + 7\*10<sup>-2</sup> + 5\*10<sup>-3</sup>
- If there is no integer p such that x*(2<sup>p</sup>) is a whole number, then internal representation is always an approximation

### Storing floating point numbers
- Floating point is a pair of integers, the significant digits and the base 2 exponent
- (1, 1) -> 1*2<sup>1</sup> -> 10<sub>2</sub> -> 2.0
- (125, -2) -> 125*2<sup>-2</sup> -> 11111.01<sub>2</sub> -> 31.25
- The maximum number of significant digits governs the precision with which numbers can be represented
- Most modern computers use 32 bits to represent significant digits
- If a number is represented with more than **32 bits** in binary, the number will be rounded
- The error will only be on order of 2*10<sup>-10</sup>
- Never use == to test floats, instead test whether they are within small amount of each other

### Approximation methods
- Guess-and-check provides a simple algorithm for solving problems
- When set a potential solution is enumerable, exhaustive enumeration guaranteed to work
- It's a limiting way to solve problems
  - Increment is usually an integer but not always
  - Can't give us an approximate solution to varying degrees
- Approximation may not be able to find exact answers
- Floating point approxmiation errors are important to this method

 ### Finding roots
 - In an approximation algorithm to find the root of a number two parameters are set
   - **Epsilon** - how close are we to answer?
   - **Increment** - how much to increase our guess?
- Performance will vary based on these values in speed and accuracy
- Decreasing increment size - slower progrm, but more likely to get good answer
- Increasing epsilon - less accurate answer, but faster program
- ```
  x = 10
  epsilon = 0.01
  numGuesses = 0
  guess = 0.0
  increment = 0.0001
  while abs(guess ** 2 - x) >= epsilon and guess ** 2 <= x:
    guess += increment
    numGuesses += 1
  print('numGuesses =', numGuesses)
  if abs(guess ** 2 - x) >= epsilon:
    print('Failed on square root of', x)
  else:
    print(guess, 'is close to square root of', x)
