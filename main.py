tribonacciNumbersCache = [0, 0, 1]
for i in range(3, 100):
    tribonacciNumbersCache.append(
        tribonacciNumbersCache[i - 1] + tribonacciNumbersCache[i - 2] + tribonacciNumbersCache[i - 3])

tribonacciNumbers = [73, 10, 4, 15, 20, 7]
tribonacciNumbersValue = []
for number in tribonacciNumbers:
    tribonacciNumbersValue.append(tribonacciNumbersCache[number - 1])

print(tribonacciNumbersValue)
