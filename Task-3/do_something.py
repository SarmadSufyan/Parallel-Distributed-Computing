import math

def do_something(size, out_list):
    """
    Performs CPU-intensive mathematical computations.
    
    This function calculates prime numbers up to 'size' and performs
    various mathematical operations to simulate real computational work.
    
    Args:
        size (int): The range up to which to perform computations
        out_list (list): Output list to store results
    """
    result = 0
    primes = []
    
    # Prime number calculation (CPU-intensive)
    for num in range(2, size):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    # Additional mathematical operations
    for i in range(size):
        result += math.sqrt(i + 1)
        result += math.sin(i) * math.cos(i)
        result += math.log(i + 1)
    
    # Store results
    out_list.append({
        'prime_count': len(primes),
        'math_result': result,
        'largest_prime': primes[-1] if primes else None
    })
    
    # Print output statement
    print(f"Process completed: Found {len(primes)} primes, "
          f"Largest prime: {primes[-1] if primes else 'None'}, "
          f"Math result: {result:.2f}")
    
    return result