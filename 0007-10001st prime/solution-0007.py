def solution():
    prime_number = {
        "index": 1,
        "value": 2
    }
    i = 2 
    while prime_number["index"] <= 10001:          
        if is_prime(i):
            prime_number["index"] += 1
            prime_number["value"] = i
        i += 1 
    return prime_number["value"]

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
	print(solution())