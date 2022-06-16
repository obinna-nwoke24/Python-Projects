import scipy.stats as stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
print(dir(stats))

choices = np.random.choice(['Win', 'Lose'], 10, p=(.10, .90))
print(choices)
print((choices == 'Win').sum())

coin = np.random.choice(['Head', 'Tail'], 10, p=(.5, .5))
print(coin)
print((coin == 'Head').sum())

heads_per_100_tosses = []


def flip(size=10, n=1000):
    for i in range(size):
        tosses = np.random.choice(['Head', 'Tail'], n, p=(.5, .5))
        heads = (tosses == 'Head').sum()
        heads_per_100_tosses.append(heads)
    heads_per = np.array(heads_per_100_tosses)
    return heads_per


trials = flip(100, 10000)

print(trials)

plt.hist(trials)
plt.show()
