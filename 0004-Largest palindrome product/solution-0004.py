def solution():
    result = 0 
    for x in range(100,1000):
        for y in range(100,1000):            
            if str(x * y) == str(x * y)[ : : -1] and result < x * y:
                result = x * y
    return result

if __name__ == "__main__":
	print(solution())