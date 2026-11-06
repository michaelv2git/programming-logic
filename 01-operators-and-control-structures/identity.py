c1 = "a"
c2 = 1
c3 = False
c4 = 25.5

# is
# is not

if type(c1) is not str:
    print("Si")
elif type(c2) is int:
    print("Si")
elif type(c3) is bool:
    print("Si")
elif type(c4) is not float:
    print("Si")
else:
    print("No")