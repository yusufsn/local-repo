##STYLE 1
for i in range(1,11):
    print'*'

##STYLE 2
##print('*'*10)

##STYLE 3
##for i in range(1,11):
##    print('*'*10)

##STYLE 4
##for i in range(1,11):
##    print('*'*i)

##STYLE 5
##for i in range(10,0,-1):
##    print('*'*i)

##STYLE 6
##for i in range(10,0,-1):
##    print(' '*(i-1) + '*'*(11-i))

##STYLE 7
##for i in range(1,11):
##    print(' '*(i-1)+'*'*(11-i))

##STYLE 8
##for i in range(10,0,-1):
##    print(' '*(i-1) + '*'*(11-i)+'*'*(10-i))

##STYLE 9
##for i in range(10,0,-1):
##    print(' '*(10-i) + '*'*i+'*'*(i-1))

##STYLE 10 (Kupu-kupu vertikal)
##for i in range(1,11):
##    print('*'*i+' '*(10-i)+' '*(10-i)+'*'*i)
##for i in range(9,0,-1):
##    print('*'*i+' '*(10-i)+' '*(10-i)+'*'*i)

##STYLE 11 (Kupu-kupu horisontal)
##for i in range(1,11):
##    print(' '*(i-1)+'*'*(11-i)+'*'*(10-i))
##for i in range(2,11):
##    print(' '*(10-i)+'*'*i+'*'*(i-1))

##STYLE 12
x=str(input("Masukkan karakter = "))
print("\n")
for i in range(1,11):
    print(x*(11-i)+' '*(i-1)+' '*(i-1)+x*(11-i))
for i in range(2,11):
    print(x*i+' '*(10-i)+' '*(10-i)+x*i)
