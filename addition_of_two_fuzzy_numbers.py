#Prompt the user to input two numbers
number1=int(input('First Number :'))
number2=int(input('Second Number :'))

#Calculate the fuzzy values for the numbers.
small1=(10-number1)*0.10
small2=(10-number2)*0.10
large1=number1*0.10
large2=number2*0.10

#Define a function that finds the minimum of two fuzzy numbers
def minimum(small1,small2,large1,large2):
  # Find the fuzzy values for each of the four possible combinations of numbers
  f1=min(small1,small2)
  f2=min(large1,large2)
  f3=min(small1,large2)
  f4=min(large1,small2)

  # Use the fuzzy values to calculate the minimum of the two numbers
  result=((f2*20)+(f3*10)+(f4*10))/(f1+f2+f3+f4)

  # Print the result
  print(f"Result for minimum is:  {result}")

# Define a function to multiply two fuzzy numbers
def multip(small1,small2,large1,large2):

  # Find the fuzzy values for each of the four possible combinations of numbers
  fmul1=(small1*small2)
  fmul2=(large1*large2)
  fmul3=(small1*large2)
  fmul4=(large1*small2)

  # Use the fuzzy values to calculate the product of the two numbers
  result2=((fmul2*20)+(fmul3*10)+(fmul4*10))/(fmul1+fmul2+fmul3+fmul4)

  # Print the result
  print(f"Result for multiplication is :  {result2}")

# Call the minimum and multiplication functions
minimum(small1,small2,large1,large2)
multip(small1,small2,large1,large2)