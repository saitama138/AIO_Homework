from math import *

def md_nre_single_samples(y, y_hat, n, p) :
    md_nre = 0.0
    m = 1
    for i in range(1, m + 1) :
        md_nre+= (y ** (1/n) - y_hat ** (1/n)) ** p

    print(md_nre)
