n = int(input())

numbers = map(int, input().split())

sum_of_squares = sum(map(lambda x: x**2, numbers))

print(sum_of_squares)
