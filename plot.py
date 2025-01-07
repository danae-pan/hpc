import matplotlib.pyplot as plt
import numpy as numpy

## te_main runtime
## mf_main mflops/s
## memory footprint memory
## NPARTS="2000 3000 4000 5000 7500 10000 20000 40000 80000 200000 400000 800000 1200000 1600000 3000000"

with open('aos.gcc.dat') as f:
    memory, mf_dist, mf_check, mf_main, te_main = zip(*[line.split() for line in f])
    ## print(memory)

fig, ax = plt.subplots(figsize = (9, 6))
ax.scatter(memory, mf_main, s=60, alpha=0.7, edgecolors="k")

# Set logarithmic scale on the x variable
ax.set_xscale("log",base = 2)
fig.savefig("plot1.png")



