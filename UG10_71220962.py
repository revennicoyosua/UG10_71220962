def add(angka1, angka2):
    return angka1 + angka2
def subtract(angka1, angka2):
    return angka1 - angka2
def multiply(angka1, angka2):
    return angka1 * angka2
def divide(angka1, angka2):
    return angka1 / angka2

print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while true:
    choice = input("enter choice(1/2/3/4): ")
    if choice in('1', '2', '3', '4'):
        num1 = float(input("masukan angka pertama: "))
        num2 = float(input("masukan angka kedua: "))

        if choice == '1':
            print(num1, "+", num2, "=", Add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Divide(num1, num2))

        next_calculation = input("let's do next calculation (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("invalid input")
    
