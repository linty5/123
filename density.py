# Lin Tingyu. 56111512
from scipy import stats
import numpy as np
import argparse
import matplotlib.pyplot as plt
import time

def Binomial_Density(opt):
    size = opt.size
    n = opt.n
    p = opt.p
    binomial = stats.binom.rvs(n = n, p = p, size = size)
    print(np.mean(binomial))
    print(np.std(binomial, ddof = 1))
    return binomial

def Poisson_Density(opt):
    size = opt.size
    mu = opt.mu
    poisson = stats.poisson.rvs(mu = mu, size = size)
    return poisson

def Normal_Density(opt):
    size = opt.size
    m = opt.m
    s = opt.s
    normal = stats.norm.rvs(size = size)
    return normal

def Exponential_Density(opt):
    size = opt.size
    exponential = stats.expon.rvs(scale = 2, size = size)
    return exponential

def Plot(Density, opt):
    plt.hist(Density, bins = 10, normed = True)
    plt.title('%s Density'%opt.type)
    plt.show()


if __name__ == '__main__':
    # Options can be adjusted listing here
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, default='Exponential',
                        help='choose the type of distribution')
    parser.add_argument('--p', type=float, default=0.5, help='probability')
    parser.add_argument('--n', type=int, default=10, help='sample points')
    parser.add_argument('--k', type=int, default=50, help='range')
    parser.add_argument('--r', type=int, default=5, help='rate')
    parser.add_argument('--m', type=float, default=0, help='mean')
    parser.add_argument('--mu', type=float, default=3, help='mean')
    parser.add_argument('--s', type=float, default=10, help='standard deviation')
    parser.add_argument('--l', type=float, default=0.5, help='lamda')
    parser.add_argument('--size', type=float, default=50000, help='lamda')
    opt = parser.parse_args()
    # Lin Tingyu. 56111512
    time_start = time.time()
    if opt.type == 'Poisson':
        Density = Poisson_Density(opt)
    elif opt.type == 'Normal':
        Density = Normal_Density(opt)
    elif opt.type == 'Exponential':
        Density = Exponential_Density(opt)
    elif opt.type == 'Binomial':
        Density = Binomial_Density(opt)
        print("b")
    else:
        print("you forget to inout type")
        Density = Binomial_Density(opt)
    Plot(Density, opt)
    time_end = time.time()
    print('totally cost', time_end - time_start)


