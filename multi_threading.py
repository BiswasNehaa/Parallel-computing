"""
Create multiple threads with their task:
-Thread a) Print the odd numbers between  0-20
-Thread b) Print the even numbers between  0-20
-Thread c) Print the prime numbers between  0-20
"""


import threading

# Create a lock so threads don't interleave print outputs mid-line
print_lock = threading.Lock()

# Thread A: Print Odd Numbers
def print_odds():
    odds= [n for n in range(0,21) if n % 2 != 0]
    with print_lock:
        print(f" Thread A ( Odd Numbers 0-20) : {odds}")
        

# Thread B: Print even Numbers
def print_evens():
    evens= [ n for n in range(0,21) if n%2 == 0]
    with print_lock:
        print(f"Thread B ( even numbers 0-20 ): {evens}")
 
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

       
# Thread C: Print prime Numbers   
def print_primes():
    primes=[n for n in range(0,21) if is_prime(n)]
    with print_lock:
        print(f"Thread C (Prime Numbers 0-20): {primes}")  


# 1. Instantiate the three threads
thread_a = threading.Thread(target=print_odds, name="Thread-Odd")
thread_b = threading.Thread(target=print_evens, name="Thread-Even")
thread_c = threading.Thread(target=print_primes, name="Thread-Prime")

# 2. Start all threads concurrently
thread_a.start()
thread_b.start()
thread_c.start()

# 3. Wait for all threads to finish before exiting
thread_a.join()
thread_b.join()
thread_c.join()

print("\nAll threads completed successfully!")