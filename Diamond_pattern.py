# Diamond pattern

n = int(input("Enter rows: "))

# Upper part
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")
    print()

# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")
    print() 
    
output:

 #  *
  #* *
 #* * *
#* * * *
 #* * *
  #* *
   #*
