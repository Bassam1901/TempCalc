#Temprature Calculator
def kelvin_celisus(m):
  if m == 'k':
    print("temperature in Celsius =")
    c=float(input())
    k = c + 273
    print("temperature in kelvin = ",k)
  if m == "c":
    print("temperature in Kelvin =")
    k=float(input())
    c = k - 273
    print("temperature in Celisus = ",c)

def Fahrenheit_celisus(n):
  if n == 'f':
    print("temperature in Celsius =")
    c=float(input())
    f= (c * 1.8) + 32 
    print("temperature in Fahrenheit = ",f)
  if  n == "c":
    print("temperature in Fahrenheit =")
    f=float(input())
    c = (f - 32)*1.8
    print("temperature in Celisus = ",c)

def kelvin_Fahrenheit(a):
  if a == 'k':
    print("temperature in Fahrenheit =")
    f=float(input())
    c = (f - 32)*1.8
    k = c + 273
    print("temperature in kelvin = ",k)
  if a == "f":
    print("temperature in Kelvin =")
    k=float(input())
    c = k - 273
    f= (c * 1.8) + 32 
    print("temperature in Fahrenheit = ",f)
num = 1
while num == 1:
  print("Enter 1 to convert between Kelvin and celisus")
  print("Enter 2 to convert between Fahrenheit and celisus")
  print("Enter 3 to convert between Kelvin and Fahrenheit")
  o=int(input())
  if o==1:
    print(" Enter k for from celisus to Kelvin")
    print("Enter c for from  Kelvin to celisus")
    m=str(input())
    kelvin_celisus(m)
  
  if o==2:
    print(" Enter f from celisus to Fahrenheit")
    print("Enter c for Fahrenheit to celisus")
    n=str(input())
    Fahrenheit_celisus(n)
  
  if o==3 :
    print(" Enter k from Fahrenheit to Kelvin")
    print("Enter f for from Kelvin to Fahrenheit")
    a=str(input())
    kelvin_Fahrenheit(a)
  
  print("Do you want to convert another temprature?\nYes=1\nNo=0")
  ans=int(input())
  if ans==1:
    num=1
  if ans==0:
    num=0
    print("Thank you for using our project !<3")
    
  









  
