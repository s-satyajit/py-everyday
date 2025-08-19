day = 4
month = 5

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("a weekday in april")
    case 6 | 7 if month == 5:
        print("a weekend in may")
    case _:
        print("no match")
        