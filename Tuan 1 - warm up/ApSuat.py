def change(a):
    ans = a * 0.453592 / 2.54**2
    return ans
a = float(input())
print("{:g}".format(change(a)))

