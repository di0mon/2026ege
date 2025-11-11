for N in range(1,100000):
    from string import printable as alph
    def convert2(N, 3):
        res = " "
        while N != 0:
            res += alph[N % 3]
            N //= 3
        return res[::-1]