try:
    n = int(input("შეიყვანე სამკუთხედის სიმაღლე: "))

    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

except ValueError:
    print("შეიყვანე მთელი რიცხვი!")