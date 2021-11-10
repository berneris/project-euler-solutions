def solution():
    number = 600851475143
    prime_factor_list = []
    i = 2
    while number >= i:
        if number % i == 0:
            number /= i
            prime_factor_list.append(i)
            i = 2
        else:
            i += 1
    return prime_factor_list.pop()

if __name__ == "__main__":
	print(solution())