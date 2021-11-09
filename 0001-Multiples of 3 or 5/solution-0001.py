def solution():
    result = 0
    for x in range(1000):
        if (x % 3 == 0 or x % 5 == 0):        
            result = result + x        
    return str(result)

if __name__ == "__main__":
	print(solution())