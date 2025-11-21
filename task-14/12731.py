from string import printable as alph
for x in alph[:13]:
    num1=int(f"9{x}AB",13)
    num2=int(f"{x}46C",16)
    num3=int(f"B7{x}",15)
    num=num1+num2-num3
    if num%14==0:
        print(x,num//14)
