c1 = 7
c2 = 4
c3 = 10

# And

if c1 > c3 and c2 > c3:
    print("Cumple")
elif c1 == c3 and c2 == c3:
    print("Es igual")
elif c1 < c3 and c2 < c3:
    print("No cumple")

# Or

if c1 > c3 or c2 > c3:
    print("Cumple")
elif c1 == c3 or c2 == c3:
    print("Es igual")
elif c1 < c3 or c2 < c3:
    print("No cumple")

# And Not

if c1 > c3 and not c2 > c3:
    print("Cumple")
elif c1 == c3 and not c2 == c3:
    print("Es igual")
elif c1 < c3 and not c2 < c3:
    print("No cumple")

# Or Not

if c1 > c3 or not c2 > c3:
    print("Cumple")
elif c1 == c3 or not c2 == c3:
    print("Es igual")
elif c1 < c3 or not c2 < c3:
    print("No cumple")