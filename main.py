from collections import Counter
from struct import pack
import matplotlib.pyplot as plt


il = []


def plot(d):
    mc = d.most_common()
    plt.plot([i[1] for i in mc])
    # plt.axhline(mc[0][1], linestyle='--', color='red')
    plt.text(0, mc[0][1], (0, mc[0][1]))
    # plt.axhline(mc[-1][1], linestyle='--', color='red')
    plt.text(len(mc), mc[-1][1], (len(mc), mc[-1][1]))
    plt.show()


def print_most(d, th):
    c = 0
    for i, v in d.items():
        if v > th:
            print(i)
            c += 1
    print(c)


file = 'poll-29683-Sun_Nov__1_11-54-38_2020.log'
file = 'poll-29683-Thu_Oct__8_11-54-38_2020.log'

"""
poll example:
Sun Nov  1 11:54:38 2020 >>  device DOWN did=0x000312F295F77268
Sun Nov  1 11:54:38 2020 >>  device UP did=0x0003161ABDA73549
"""

def count(file):
    with open(file, 'r') as f:
        ls = f.readlines()
        for l in ls:
            i = int(l.split('=')[1].strip(), 0)
            did = pack('<Q', i).hex()
            il.append(did)
    return Counter(il)


def print_hi(name):
    d = count(name)
    plot(d)
    print_most(d, 1000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
