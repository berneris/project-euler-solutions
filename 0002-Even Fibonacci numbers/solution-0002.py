def solution():
    result = 0
    fibonacciX1 = 0
    fibonacciX2 = 1
    while fibonacciX1 <= 4000000:
        if fibonacciX1 %2 == 0:
            result += fibonacciX1
        fibonacciX1 , fibonacciX2 = fibonacciX2 , fibonacciX1 + fibonacciX2
    return result

if __name__ == "__main__":
	print(solution())