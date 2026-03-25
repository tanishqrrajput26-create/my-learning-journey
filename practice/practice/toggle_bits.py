def toggle_bits(n):
  if n == 0:
       return 1
  binary_str = bin(n)[2:]

  toggled_str = "".join(['1' if b == '0' else '0' for b in binary_str])

  result = int(toggled_str ,2)
  return result 
num = int(input("Enter a +ve intger:  "))
print(f"Result after toggling:{toggle_bits(num)}")

#Enter a +ve intger: 12
#result after toggling: 3

#Ex:
#12= 1100  ---> 0011=3 (toggling hone ke baad )
