score = input("Enter Score: ")

try:
    s = float(score)
    if s < 0.0 or s > 1.0:
        print("Error: Score is out of range. Please enter a value between 0.0 and 1.0.")
    else:
        if s >= 0.9:
            print("A")
        elif s >= 0.8:
            print("B")
        elif s >= 0.7:
            print("C")
        elif s >= 0.6:
            print("D")
        else:
            print("F")
except:
    print("Error: Invalid input. Please enter a numeric value.")
