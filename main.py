#Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  for x in range(2, number):
    if number % x == 0:
      is_prime = False
  if is_prime:
    print(f"Die untersucht Zahl {number} ist eine Primzahl.")
  else:
    print(f"Die untersuchte Zahl {number} ist keine Primzahl.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



