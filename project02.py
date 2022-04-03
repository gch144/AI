import numpy as np

A = b = c = r = p = d = cp = mp = mi = None


def F(x): return np.matmul(np.matmul(x, A), x) + np.matmul(b, x)+c


def gen_population(size, d):
    '''generate population with given size and dimension within range (-2^d,2^d)'''
    population = []
    for _ in range(size):
        rn = np.random.randint(0, 2**d)
        sign = np.random.randint(0, 2)
        chromosome = [int(b) for b in list(np.binary_repr(rn, d))]
        if(sign):
            chromosome = (np.array(chromosome)*-1).tolist()
        population.append(chromosome)

    return population


def roulette_selection(fitness):
    '''select a parent using roulette wheel selection with scaling'''
    f = np.divide(fitness, np.linalg.norm(fitness))
    f = np.add(f, np.abs(min(f)))
    s = sum(f)
    p = np.random.uniform(0, s)
    i = 0
    while (p+f[i]) < s:
        p += f[i]
        i += 1
    return i


def crossover(c1, c2, d, p):
    '''cross two parents based on given probability'''
    if(np.random.random() < p):
        p = np.random.randint(0, d)
        c1[p:], c2[p:] = c2[p:], c1[p:]


def mutate(c, p):
    '''mutate genes of a chromosome based on given probability'''
    for i in range(len(c)):
        if(np.random.random() < p):
            c[i] = int(not c[i])


def fifo(age, fitness):
    '''replace oldest chromosomes in the population, if more than two chromosome are the oldest,
    they are chosen based on their fitness value'''
    age = list(age)
    a = age.copy()
    a.sort()
    i1, i2 = age.index(a[-1]), age.index(a[-2])
    if(a.count(a[-1]) == 2):
        return i1, i2
    if(a.count(a[-1] == 1)):
        if(a.count(a[-2] == 1)):
            return i1, i2
        else:
            t = [i for i, x in enumerate(age) if x == a[-2]]
            z = fitness[t[0]]
            for x in t:
                if(fitness[t[x]] < z):
                    z = fitness[t[x]]
                    i2 = x
            return i1, i2
    t = [i for i, x in enumerate(age) if x == a[-1]]
    z = fitness[t[0]]
    for x in t:
        if(fitness[t[x]] < z):
            z = fitness[t[x]]
            i1 = x
    t.remove(i1)
    z = fitness[t[0]]
    for x in t:
        if(fitness[t[x]] < z):
            z = fitness[t[x]]
            i2 = x
    return i1, i2


def get(vals):
    '''get input from user with given args and conditions'''
    for val in vals:
        while(1):
            try:
                exec(val[0][0]+'='+input('\n'+val[0][0] +
                     ' ['+val[0][1]+'] : '), globals())
                for c in val[1]:
                    exec(c, globals())
                for c in val[2]:
                    exec('r='+c[0], globals())
                    if not r:
                        raise Exception(c[1])
                break

            except Exception as e:
                print('Error:', e)


get((
    (('d', 'dimension'), ('d=int(d)',),
     (('d>=1', 'dimension should be a greater than 0'),)),
    (('A', 'matrix'), (), (('np.matrix(A).shape==(d,d)', 'wrong dimensions for A'),)),
    (('b', 'vector'), (),
     (('np.matrix(b).shape==(1,d)', 'wrong dimensions for b'),)),
    (('c', 'scalar'), ('c=float(c)',), ()),
    (('p', 'population size'), ('p=int(p)',),
     (('p>1', 'population size should be a greater than 1'),)),
    (('cp', 'crossover probability'), ('cp=float(cp)',),
     (('cp>=0 and cp<=1', 'crossover probability must be within range [0,1]'),)),
    (('mp', 'mutation probability'), ('mp=float(mp)',),
     (('mp>=0 and mp<=1', 'mutation probability must be within range [0,1]'),)),
    (('mi', 'maximum iterations'), ('mi=int(mi)',),
     (('mi>1', 'maximum iterations should be a greater than 1'),)),
))

population = gen_population(p, d)
fitness = [F(chromosome) for chromosome in population]
age = np.zeros(p, int)
for g in range(mi):
    c1 = population[roulette_selection(fitness)].copy()
    c2 = population[roulette_selection(fitness)].copy()

    crossover(c1, c2, d, cp)
    mutate(c1, mp)
    mutate(c2, mp)
    i1, i2 = fifo(age, fitness)
    population[i1], population[i2] = c1, c2
    fitness = [F(chromosome) for chromosome in population]
    age += 1
    age[i1] = 0
    age[i2] = 0

print("Last population with fitness and age: ", population, '\n', fitness, age)
