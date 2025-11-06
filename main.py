from operations import Sum, Rest, Multiplication, Division

def main():
  print("Welcome to the Calculator App!")
  operation = input("Please select one of the following operations:\n1. Sum\n2. Rest\n3. Multiplication\n4. Division\nYour choice: ")
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  match operation:
    case "1":
      print(Sum(num1, num2))
    case "2":
      print(Rest(num1, num2))
    case "3":
      print(Multiplication(num1, num2))     
    case "4":
      print(Division(num1, num2)) 

if __name__ == "__main__":
    main()
