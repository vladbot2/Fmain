#1
# def display():
#     quote = '''"Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
# Bill Gates'''
#     print(quote)

# display()

#2
# def display(start, end):
#     if start > end:
#         start, end = end, start
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)

# display(4, 10)

#3
# def display(side, symbol, filled):
#     for i in range(side):
#         if filled or i == 0 or i == side - 1:
#             print(symbol * side)
#         else:
#             print(symbol + ' ' * (side - 2) + symbol)

# display(5, '*', True)
# display(5, '*', False)

#4
# def find(a, b, c, d, e):
#     return min(a, b, c, d, e)

# print(find(4, 7, 1, 9, 3))


#5
# def range(start, end):
#     if start > end:
#         start, end = end, start
#     product = 1
#     for num in range(start, end + 1):
#         product = num
#     return product

# print(range(2, 4))


#6
# def count(number):
#     return len(str(abs(number)))

# print(count(3456))


#7
# def palindrome(number):
#     str = (number)
#     return str == number[::-1]

# print(palindrome(123321))
# print(palindrome(421987))




