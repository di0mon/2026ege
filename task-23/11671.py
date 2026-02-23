def f(start,end):
    if end==15:return{start}
    return f(start+10,end+1)| f(start-5,end+1)
print(len(f(1,0)))