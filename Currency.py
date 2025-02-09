print ("Type 1 for USD")
print ("Type 2 for INR")
print ("Type 3 for EUR")
print ("Type 4 for GBP")
choice = (input ("Enter your choice: "))
print ("Conversion from", choice, "to?")
print ("Type 1 for USD")
print ("Type 2 for INR")
print ("Type 3 for EUR")
print ("Type 4 for GBP")
choice2 = (input ("Enter your choice: "))
amount = float(input("Amount?"))
if choice == "1" and choice2 == "2":
    print (amount, "USD in INR is", (amount*79.00))
if choice == "1" and choice2 == "3":
    print (amount, "USD in EUR is", (amount*0.99))
if choice == "1" and choice2 == "4":
    print (amount, "USD in GBP is", (amount*0.83))
if choice == "2" and choice2 == "1":
    print (amount, "INR in USD is", (amount*0.013))
if choice == "2" and choice2 == "3":
    print (amount, "INR in EUR is", (amount*0.012))
if choice == "2" and choice2 == "4":
    print (amount, "INR in GBP is", (amount*0.010))
if choice == "3" and choice2 == "1":
    print (amount, "EUR in USD is", (amount*1.01))
if choice == "3" and choice2 == "2":
    print (amount, "EUR in INR is", (amount*80.81))
if choice == "3" and choice2 == "4":
    print (amount, "EUR in GBP is", (amount*0.84))
if choice == "4" and choice2 == "1":
    print (amount, "GBP in INR is", (amount*96.01))
if choice == "4" and choice2 == "2":
    print (amount, "GBP in USD is", (amount*1.20))
if choice == "4" and choice2 == "3":
    print (amount, "GBP in EUR is", (amount*1.19))
