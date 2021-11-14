import math
def solution():
    list = range(1,101)
    return math.pow(sum(list),2) - sum([pow(item,2) for item in list])

if __name__ == "__main__":
	print(solution())