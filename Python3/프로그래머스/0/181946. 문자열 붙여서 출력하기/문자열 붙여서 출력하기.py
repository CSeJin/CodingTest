# 방법 1
# input_str = input()
# idx = input_str.index(' ')
# print(input_str[:idx]+input_str[idx+1:])

# 방법 2
# print(input().strip().replace(' ',''))

# 방법 3
str1, str2 = input().strip().split()
print(str1, str2, sep='')