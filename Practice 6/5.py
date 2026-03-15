S = input()

if any(c.lower() in "aeiou" for c in S):
    print("Yes")
else:
    print("No")
