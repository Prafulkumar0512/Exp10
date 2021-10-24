def DecimalToBinary(num):
        if num >= 1:
            DecimalToBinary(num // 2)
            print(num % 2,end='')

for i in range(0,10):
    print(f'{i}=',end="")
    DecimalToBinary(i)
    print("\n")