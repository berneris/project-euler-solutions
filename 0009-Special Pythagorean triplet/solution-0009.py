def solution():
    limit = 1000
    for a in range(1,limit + 1):
        for b in range(a + 1,limit + 1):
            c = limit - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

if __name__ == "__main__":
	print(solution())