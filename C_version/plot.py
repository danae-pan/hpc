import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the file
file_path = "runtime_results.txt"  # Update with your file path
data = pd.read_csv(file_path)

# Extract threads and runtime columns
threads = data["Threads"]
runtimes = data["Runtime"]

# Calculate speedup
speedup = runtimes.iloc[0] / runtimes

# Plot runtime vs. threads
plt.figure(figsize=(10, 6))
plt.plot(threads, runtimes, marker='o', label="Runtime (s)")
plt.xlabel("Number of Threads")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime vs. Number of Threads")
plt.grid(True)
plt.legend()
plt.savefig("runtime_plot.png")  # Save the runtime plot
plt.show()

# Plot speedup vs. threads
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup, marker='o', color='green', label="Speedup")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs. Number of Threads")
plt.grid(True)
plt.legend()
plt.savefig("speedup_plot.png")  # Save the speedup plot
plt.show()
