# Lin Tingyu. 56111512
from scipy import stats
import numpy as np
import argparse
import matplotlib.pyplot as plt
import time

def Binomial_Distribution(opt):
    k = np.arange(0,opt.k)
    n = opt.n
    p = opt.p
    binomial = stats.binom.pmf(k, n, p)
    return binomial

def Poisson_Distribution(opt):
    k = np.arange(0,opt.k)
    r = opt.r
    poisson = stats.poisson.pmf(k, r)
    return poisson

def Normal_Distribution(opt):
    k = np.arange(-1*(opt.k), opt.k, 0.1)
    m = opt.m
    s = opt.s
    normal = stats.norm.pdf(k, m, s)
    return normal

def Exponential_Distribution(opt):
    l = opt.l
    k = np.arange(0, opt.k, 1)
    Exponential = l * np.exp(-l * k)
    return Exponential

def Plot(Distribution, opt):
    k = np.arange(0, opt.k)
    if opt.type == 'Normal':
        k = np.arange(-1 * (opt.k), opt.k, 0.1)
    plt.plot(k, Distribution)
    plt.title('%s Distribution'%opt.type)
    plt.show()

if __name__ == '__main__':
    # Options can be adjusted listing here
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, default='Exponential',
                        help='choose the type of distribution')
    parser.add_argument('--p', type=float, default=0.3, help='probability')
    parser.add_argument('--n', type=int, default=40, help='sample points')
    parser.add_argument('--k', type=int, default=50, help='range')
    parser.add_argument('--r', type=int, default=5, help='rate')
    parser.add_argument('--m', type=float, default=0, help='mean')
    parser.add_argument('--s', type=float, default=10, help='standard deviation')
    parser.add_argument('--l', type=float, default=0.5, help='lamda')
    opt = parser.parse_args()
    # Lin Tingyu. 56111512
    time_start = time.time()
    if opt.type == 'Poisson':
        Distribution = Poisson_Distribution(opt)
    elif opt.type == 'Normal':
        Distribution = Normal_Distribution(opt)
    elif opt.type == 'Exponential':
        Distribution = Exponential_Distribution(opt)
    elif opt.type == 'Binomial':
        Distribution = Exponential_Distribution(opt)
    elif opt.type == 'LinTingyu':
        Distribution = Binomial_Distribution(opt)
        print("homework")
    else:
        print("you forget to inout type")
        Distribution = Binomial_Distribution(opt)
    Plot(Distribution, opt)
    time_end = time.time()
    print('totally cost', time_end - time_start)


