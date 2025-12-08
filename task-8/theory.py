from itertools import*

# product - ф-ия которая формирует все возможные комбинации длиной repeat
alph="12"
for val in product(alph,repeat=2)
    val = "".join(val)
# permutations - ф-ия которая формирует все возможные перестановки
for val in permutations(alph):
    val = "".join(val)

# enumerate нумерует элементы последовательности от start
res=enumerate(alph,start =1)
print(*res)