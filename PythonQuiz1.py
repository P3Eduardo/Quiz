x = int(raw_input("Input the first number: "))
y = int(raw_input("Input the second number: "))
Op = raw_input("Choose an operation: ")

if Op == '+':
    print(x+y)
elif Op == '-':
    print(x-y)
elif Op == '*':
    print(x*y)
elif Op == '/':
    print(x/y)
elif Op == '%':
    print(x%y)


i = 1
while i <= 100:
  print(i)
  i += 1
  if i == 3%i:
    print("Fizz")
  elif Op == 5%i:
        print(x%y)
