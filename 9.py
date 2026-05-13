def strs_are_balanced(st1: str, st2: str):
    for i in st1:
        if i not in st2.lower():
            return False

    return True


s1 = "yn"
s2 = "PyNative"
s3 = "ynf"
s4 = "PyNative"

print(strs_are_balanced(s1, s2))
print(strs_are_balanced(s3, s4))
