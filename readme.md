Installation
-----

Clone the repo and run main.py

Algorithm
-----
For each number in the domain, start with base 2 and increment, checking for palindromes at each base, until a palindrome is found, then continue in the domain.

We calculate the number of digits for each base with log base that number. This allows us to know if there's an even number or odd number of digits for optimization.

By knowing the number of digits, we can recursively calculate only the first and last digits for each number in each base using modular arithmatic, which saves a huge amount of time (average complexity becomes very close to O(mn) instead O(mno) where m is the domain (1-1000), n is the number of bases iterated through for each number, and o is the number of digits in each palindrome since most failures will fail on first lookup causing o factor to become O(1) average)

The other optimization we make is that a number is always palindromic in a base one less than itself, so if we get that far we don't bother calculating (always converts to '11')

Unit Tests
-----
Unit tests check a couple edge cases and a couple of weird palindromic primes and big numbers against what we'd expect