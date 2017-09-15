def lengthOfLastWord(A):
    A = A.rstrip()
    A = A.lstrip()
    if len(A) == 0:
        return 0
    else:
        count = 1
        for i in range(len(A)-1, -1, -1):
            print("Count:", count, " i:", i, A[i])
            if A[i] == ' ':
                return count-1
            elif i == 0:
                return count
            else:
                count += 1



s = "Hello World"
print(lengthOfLastWord(s))


