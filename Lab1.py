import numpy as np
from time import time

A = a = b = c = d = x = r = n = mi = mt = dv = l = h = None


def F(x): return a*x**3 + b*x**2 + c*x + d


def dF(x): return 3*a*x**2 + 2*b*x + c


def dF2(x): return 6*a*x + 2*b


def G(x): return c + np.matmul(b, x) + np.matmul(np.matmul(x, A), x)


def dG(x): return b + np.matmul(A, x)+np.matmul(np.matrix(A).transpose(), x)


def dG2(x): return A+np.matrix(A).transpose()


def gradf(x, mi, mt, dv):
    s = time()
    i = 0
    while (i < mi) and ((time()-s) <= mt) and (F(x) >= dv):
        x -= 0.1*dF(x)
        i += 1
    return x, i


def newtf(x, mi, mt, dv):
    s = time()
    i = 0
    while (i < mi) and ((time()-s) <= mt) and (F(x) >= dv):
        x -= dF(x)/dF2(x)
        i += 1
    return x, i


def gradg(x,  mi, mt, dv):
    s = time()
    i = 0
    while (i < mi) and ((time()-s) <= mt) and (G(x) >= dv):
        x = np.subtract(x, np.multiply(dG(x), 0.1)).tolist()[0]
        i += 1
    return x, i


def newtg(x, mi, mt, dv):
    s = time()
    i = 0
    while (i < mi) and ((time()-s) <= mt) and (G(x) >= dv):
        x = np.subtract(x, np.matmul(dG(x), np.linalg.inv(dG2(x)))).tolist()[0]
        i += 1
    return x, i


def ask(prompt, ev):
    while(1):
        inp = input(prompt)
        if(inp in ev):
            return inp
        print('Invalid Input!')
    print()


def get(vals):
    for val in vals:
        while(1):
            try:
                exec(val[0][0]+'='+input(val[0][0] +
                     ' ['+val[0][1]+']: '), globals())
                for c in val[1]:
                    exec(c, globals())
                for c in val[2]:
                    exec('r='+c[0], globals())
                    if not r:
                        raise Exception(c[1])
                break

            except Exception as e:
                print('Error: ', e)


f = ask('F(x) or G(x)?  [f/g]: ', ('f', 'g'))
m = ask('Newtons Method or Gradient Descent Method?  [n/g]: ', ('n', 'g'))

get((
    (('mi', 'maximum iterations'), ('mi=int(mi)',),
     (('mi>=0', 'maximum iterations must not be less than 0'),)),
    (('mt', 'maximum computaional time(seconds)'), ('mt=float(mi)',),
     (('mt>=0', 'maximum time must not be less than 0'),)),
    (('dv', 'desired value'), ('dv=float(dv)',), ())
))

b = ask('Do you want to run in batch mode? [y/n]: ', ('y', 'n'))
if(b == 'y'):
    get((
        (('n', 'batch count'), ('n=int(n)',),
         (('n>=0', 'batch count cannot be less than 0'),)),
    ))

z = ask(
    'Do you want to enter x manually or randomly generate? [m/r]: ', ('m', 'r'))
if(z == 'r'):
    get((
        (('l', 'lower limit'), ('l=float(l)',), ()),
        (('h', 'upper limit'), ('h=float(h)',),
         (('h>l'), 'higher limit must the greater than lower limit')),
    ))

if(f == 'f'):
    get((
        (('a', 'scalar'), ('a=float(a)',), ()),
        (('b', 'scalar'), ('b=float(b)',), ()),
        (('c', 'scalar'), ('c=float(c)',), ()),
        (('d', 'scalar'), ('d=float(d)',), ())
    ))
    if(z == 'm'):
        get((
            (('x', 'scalar'), ('n=float(x)',), ())
        ))
    else:
        x = np.random.randint(l, h)
    if(m == 'n'):
        _z = newtf
    else:
        _z = gradf
    if n:
        _x = [x]
        _f = [F(x)]
        for i in range(n):
            x, _i = _z(x, mi, mt, dv)
            _x.append(x)
            _f.append(F(x))
            if(z == 'm'):
                get((
                    (('x', 'scalar'), ('n=float(x)',), ())
                ))
            else:
                x = np.random.randint(l, h)

        print('x* standard deviation: {}'.format(np.std(_x)))
        print('x* mean: {}'.format(np.mean(_x)))
        print('F(x*) standard deviation: {}'.format(np.std(_f)))
        print('F(x*) mean: {}'.format(np.mean(_f)))
    else:
        x, i = _z(x, mi, mt, dv)
        print('x* = {} after {} iterations'.format(x, i))
        print('F(x*) = {}'.format(F(x)))


else:
    get((
        (('d', 'dimension'), ('d=int(d)',),
         (('d>1', 'dimension should be greater than 1'),)),
        (('A', 'matrix'), (), (('np.matrix(A).shape==(d,d)', 'wrong dimensions for A'),
                               ('np.all(np.linalg.eigvals(A) > 0)', 'matrix is not positive definite'))),
        (('b', 'vector'), (),
         (('np.matrix(b).shape==(1,d)', 'wrong dimensions for b'),)),
        (('c', 'scalar'), ('c=float(c)',), ())
    ))
    if(z == 'm'):
        get((
            (('x', 'vector'), (),
             (('np.matrix(x).shape==(1,d)', 'wrong dimensions for x'),)),
        ))
    else:
        x = np.random.uniform(low=l, high=h, size=(1, d)).tolist()[0]
    if(m == 'n'):
        _z = newtg
    else:
        _z = gradg
    if n:
        _x = [x]
        _g = [G(x)]
        for i in range(n):
            x, _i = _z(x, mi, mt, dv)
            _x.append(x)
            _g.append(G(x))
            if(z == 'm'):
                get((
                    (('x', 'vector'), (),
                     (('np.matrix(x).shape==(1,d)', 'wrong dimensions for x'),)),
                ))
            else:
                x = np.random.uniform(low=l, high=h, size=(1, d)).tolist()[0]

        print('x* standard deviation: {}'.format(np.std(_x)))
        print('x* mean: {}'.format(np.mean(_x)))
        print('G(x*) standard deviation: {}'.format(np.std(_g)))
        print('G(x*) mean: {}'.format(np.mean(_g)))
    else:
        x, i = _z(x, mi, mt, dv)
        print('G* = {} after {} iterations'.format(x, i))
        print('G(x*) = {}'.format(G(x)))
