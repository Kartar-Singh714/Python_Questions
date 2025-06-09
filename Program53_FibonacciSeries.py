# Wap The Fibonacci series is the sequence where each number is the sum of the previous two numbers of the sequence. The first two numbers are 0 and 1 which are used to generate the whole series.
#
# Example
# Input: n = 5
# Output: 0 1 1 2 3
# Explanation: The first 5 terms of the Fibonacci series are 0, 1, 1, 2, 3.
# Input: N = 7
# Output: 0 1 1 2 3 5 8
# Explanation: The first 7 terms of the Fibonacci series are 0, 1, 1, 2, 3, 5, 8

num = input("Input the number to print the fibonacci series: ")
summation = 0
prev = 0
latest = 1
print(0)
for i in range(1, int(num)):
    summation = latest + prev
    prev = latest
    latest = summation







    # for j in range(i+1):
    #     output = output + j
    #     print(output)


