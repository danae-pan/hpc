import matplotlib.pyplot as plt
import numpy as np

## te_main runtime
## mf_main performance (total)
## memory footprint memory
## NPARTS="2000 3000 4000 5000 7500 10000 20000 40000 80000 200000 400000 800000 1200000 1600000 3000000"
## mf_dist distance
## mf_check reuse

with open('aos.gcc.dat') as f:
    array = np.genfromtxt(f)
    memory, mf_dist, mf_check, mf_main, te_main = array.T
    print(memory)


with open('soa.gcc.dat') as f:
    array = np.genfromtxt(f)
    memory_soa, mf_dist_soa, mf_check_soa, mf_main_soa, te_main_soa = array.T
    

##fig, ax = plt.subplots(1,figsize = (9, 6))


fig, ax = plt.subplots(2, figsize = (9, 6))
ax[0].scatter(memory, mf_main, s=100, alpha=0.7, edgecolors="c")
ax[0].scatter(memory, mf_main_soa, s=30, alpha=0.7, edgecolors="m")
ax[0].scatter(memory, mf_dist, s=50, alpha=0.7, edgecolors="k")
ax[0].scatter(memory, mf_check, s=80, alpha=0.7, edgecolors="r")
ax[0].scatter(memory, mf_dist_soa, s=10, alpha=0.7, edgecolors="w")
ax[0].scatter(memory, mf_check_soa, s=60, alpha=0.7, edgecolors="y")


ax[1].scatter(memory, te_main, s=100, alpha=0.7, edgecolors="b")
ax[1].scatter(memory, te_main_soa, s=100, alpha=0.7, edgecolors="c")


ax[0].legend(["aos performance", "soa performance", "aos distance", "aos reuse", "soa distance", "soa reuse"], loc="lower right")
ax[1].legend(["aos runtime", "soa runtime"], loc="lower right")

# Set logarithmic scale on the x variable
ax[0].set_xscale("log",base = 2)
ax[1].set_xscale("log",base = 2)
fig.savefig("plot1.png")





