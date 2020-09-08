def user():
    global n
    global a
    global b
    n = int(input('Enter The Number: '))
    a = int(input('Enter The Local Base: '))
    b = int(input('Enter The Secend Base: '))

def to_base_ten(a,n):
    p = 0
    n = str(n)
    n = n[::-1]
    s = 0
    for  v in n:
        v = int(v)
        s = s + ((a**p)*v)
        p = p + 1
    return s

def larger_than_ten(n):
    s = ''
    if n == 10:
        s = 'A'
    elif n == 11:
        s = 'B'
    elif n == 12:
        s = 'C'
    elif n == 13:
        s = 'D'
    elif n == 14:
        s = 'E'
    elif n == 15:
        s = 'F'
    return s

def to_base_b(b,n):
    st = ''
    while n >= b:
        r = n//b
        m = n%b
        n = r
        if m >= 10:
            m = larger_than_ten(m)
        m = str(m)
        st = m + st
    if n >= 10:
        n = larger_than_ten(n)
    n = str(n)
    st = n + st
    return st


if __name__ == '__main__':
    user()
    if a != 10:
        mid = to_base_ten(a,n)
        end = to_base_b(b,mid)
        print(end)
    if a == 10:
        end = to_base_b(b,n)
        print(end)