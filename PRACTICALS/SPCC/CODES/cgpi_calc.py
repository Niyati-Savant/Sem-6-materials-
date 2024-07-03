while True:
    total=int(input("Enter total marks: "))
    score=int(input("Your marks: "))
    percent = (score/total)*100
    print(percent)
    if percent>= 80.00:
        print('O')
    elif percent>= 75.00:
        print('A')
    elif percent >= 70.00:
        print('B')
    elif percent >= 60.00:
        print('C')
    elif percent >= 50.00:
        print('D')
    elif percent >= 45.00:
        print('E')
    elif percent >= 40.00:
        print('P')
    else:
        print('F')