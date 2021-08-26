A = 35
A_F = 100
B = 65
C = 50
C_S = 250
D = 85
word = input("enter : ")
l = []
for i in range(len(word)):
  l.append(word[i])
l.sort()

A_count = l.count('A')
B_count = l.count('B')
C_count = l.count('C')
D_count = l.count('D')
total = 0
if A_count < 4:
  total = A_count * A
  
if C_count < 6:
  total = total + C_count * C
  
if A_count >= 4:
  total2 = A_count / 4
  total2 = int(total2)
  count = A_count - 4
  total2 = total2 *A_F + count*A
  total = total + total2
  
if B_count > 0:
  bc = B_count * B

  total = total + bc

if C_count >= 6:
  total3 = C_count / 6
  total3 = int(total3)
  count = C_count - 6
  total3 = total3*C_S + count*C
  total = total+total3
  
if D >0 :
  Dc = D_count * D
  total = total + Dc
  print(f"{total}.00")
