# Lecture 6 - Bisection Search

> **Topic Overview:** bisection search, Newton-Raphson

### Bisection search
- Applies to problems with an inherent order to the range of possible answers
- Suppose we know the answer lies between some interval
  - Guess the midpoint of the interval
  - If it's not the answer, check if the answer is greater than or less than the midpoint
  - Change the interval
  - Repeat
- Finding a square root using bisection search:
- ```
  x = 10
  epsilon = 0.01
  num_guesses = 0
  low = 0
  high = x
  guess = (high + low) / 2.0

  while abs(guess ** 2 - x) >= epsilon:
    if guess ** 2 < x:
      low = guess
    else:
      high = guess
    num_guesses + 1

  print('num_guesses =', str(num_guesses))
  print(str(guess), 'is close to the square root of', str(x))

### Logarithmic growth
- Process cuts set of things to check in half at each stage
- **Guess-and-check vs. bisection search:**
  - Checking answer one-by-one iteratively is linear in the number of possible guesses
  - Checking asnwer by guessing halfway point is logarithmic on the number of possible guesses
  - Log algorithms are much more efficient
- Number of searches:
  - n/2<sup>k</sup> = 1
  - n = 2<sup>k</sup>
  - k = log<sub>2</sub>(n)

### Newton-Raphson
- The Newton-Raphson method is a general approximation algorithm to find roots of a polynomial in one variable
- Newton and Raphson showed that if g is an approximation to the root, then g - p(g)/p'(g) is a better approximation
- Newton-Raphson says given a guess g for root of k a better guess is g - g(g<sup>2</sup> - k)/2g
- ```
  epsilon = 0.01
  k = 24.0
  guess = k / 2.0
  num_guesses = 0

  while abs(guess ** 2 - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess ** 2) - k)/(2 * guess))

  print('num_guesses =', str(num_guesses))
  print('Square root of', str(k), 'is about', str(guess))
