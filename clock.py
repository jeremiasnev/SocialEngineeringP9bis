import time
import matplotlib.pyplot as plt
from data_processing import filter_data, segment_data

PATH = "tweets_cov19.tsv"

times = []
labels = []
data = []
segm = []
runs = [10, 100, 2500, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000, 2500000, 5000000, None]

iteration = 1
for run in runs:
    print(f"Starting iteration {iteration}")
    
    if run == None:
        labels.append(8000000)
    else:
        labels.append(run)
    
    starttime = time.time()
    data = filter_data(PATH, items = run)
    segm = segment_data(data)
    endtime = time.time() - starttime
    times.append(round(endtime, 2))
    print(f"Iteration {iteration} finished in time {round(endtime, 2)}")
    iteration += 1

# Plot the runtime by processed tweets
plt.plot(labels, times, alpha=0.7)  # Switched labels and times
plt.xlabel('Number of Tweets Processed')
plt.ylabel('Time Used (s)')
plt.title('Runtime by Processed Tweets')
plt.grid(True)
plt.show()
