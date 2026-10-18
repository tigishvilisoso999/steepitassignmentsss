total = 0

while True:
    number = input("შეიყვანე რიცხვი (ან stop): ")

    if number.lower() == "stop":
        break

    try:
        total += float(number)
    except ValueError:
        print("შეიყვანე სწორი რიცხვი!")

print("ჯამი არის:", total)