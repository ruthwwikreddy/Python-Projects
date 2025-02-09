print("Hello, and welcome to the temperature converter.")
print("""Type : 
 ( 1 ) -  For  ( Celsius )     -->    ( Fahrenheit )

 ( 2 ) -  For  ( Fahrenheit )  -->    ( Celsius )

 ( 3 ) -  For  ( Celsius )     -->    ( Kelvin )

 ( 4 ) -  For  ( Kelvin )      -->    ( Celsius )

 ( 5 ) -  For  ( Fahrenheit )  -->    ( Kelvin )

 ( 6 ) -  For  ( Kelvin )      -->    ( Fahrenheit )\n""")

choice = input()

if choice == "1":
    print("Enter the temperature in Celsius : ")
    temp = int(input())
    temp = temp * 9 / 5 + 32
    print("Degrees Fahrenheit : ", int(temp))

elif choice == "2":
    print("Enter the temperature in Fahrenheit : ")
    temp = int(input())
    temp = (temp - 32) * 5 / 9
    print("Degrees Celsius : ", int(temp))

elif choice == "3":
    print("Enter the temperature in Celsius: ")
    temp = int(input())
    temp += 273
    print("Degrees Kelvin : ", int(temp))

elif choice == "4":
    print("Enter the temperature in Kelvin: ")
    temp = int(input())
    temp -= 273
    print("Degrees Celsius : ", int(temp))

elif choice == "5":
    print("Enter the temperature in Fahrenheit: ")
    temp = int(input())
    temp = (temp - 32) * 5 / 9 + 273
    print("Degrees Kelvin : ", int(temp))

elif choice == "6":
    print("Enter the temperature : ")
    temp = int(input())
    temp = (temp - 273) * 9 / 5 + 32
    print("Degrees Fahrenheit in Kelvin: ", int(temp))
