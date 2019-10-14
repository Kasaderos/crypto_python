print("input = ", end="")
s = input()
print("key = ", end="")
k = int(input())
res = ""
for c in s:
    res += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
print("output = ", res)
    
