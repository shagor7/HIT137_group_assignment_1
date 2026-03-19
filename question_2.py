# Validate user input for a number between 1 and 100
while True:
    try:
        limit = int(input("Enter a number (max 100): "))
        if 1 <= limit <= 100:
            break
        else:
            print("Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

primes = []

# Check for prime numbers from 2 to the given limit
for num in range(2, limit + 1):
    is_prime = True
# loop from 2 to the given limit, because 0 and 1 are not prime numbers.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

# Output
print("Prime numbers found:", *primes)
print("Total primes found:", len(primes))

if primes:  # check list not empty
    print("Largest prime:", max(primes))
    print("Smallest prime:", min(primes))
    print("Sum of all primes:", sum(primes))
else:
    print("No prime numbers found")