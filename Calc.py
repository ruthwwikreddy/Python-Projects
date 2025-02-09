print("Welcome to maths operation")
print("You can select any of the maths operation")
print("A - addition")
print("S - subtraction")
print("M - multiplication")
print("D - division")
print("P - percentage")

choice=input("Choose an option from above list:")

if choice =="M":
    a=input("Type your first number for multiplication:")
    b=input("Type your second number for multiplication:")
    c=int(a)*int(b)
    print("%s is your answer" %c)
elif choice =="D":
    d=input("Type your first numder for Divition:")
    e=input("Type your second number for Divition:")
    f=int(d)/int(e)
    print("%s is your answer" %f)
elif choice =="S":
    g=input("Type your first number for substaction:")
    h=input("Type your second number for sustaction:")
    i=int(g)-int(h)
    print("%s is your answer" %i)
elif choice =="A":
    j=input("Type your first number for addition:")
    k=input("Type your second number for addition:")
    l=int(j)+int(k)
    print ("%s is your answer" %l)
elif choice =="P":
    m=input("Type your first number for modulus or percentage")
    n=input("Type your second number for modulus or percentage ")
    o=int(m)%(n)
    print("%s is your answer" %o)
else:
    print("Invaid Input")
