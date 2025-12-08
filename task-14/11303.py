from string import printable as alph
for x in alph[:20]:
    num1=int(f"627{x}J8",20)
    num2=int(f"H45I{x}HIJ",20)
    num3=int(f"4IDB49J{x}7",20)
    num=num1+num2+num3
    if num%19 ==0:
        print(x,num//19)