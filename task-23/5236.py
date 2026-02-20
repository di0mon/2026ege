def f(start, end, cnt):
    cnt+=1
    if start == end and cnt>52: return 1
    if start > end: return 0
    return f(start + 2, end, cnt) + f(start * 3, end, cnt) + f(start * 4, end, cnt)


print(f(2, 400,0))