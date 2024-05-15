from data_processing import *
import matplotlib.pyplot as plt
import statistics
import time

PATH = "tweets_cov19.tsv"
colors = ["red", "red", "red", "yellow", "yellow", "yellow", "green", "green", "green"]
sentiment_scores = list(range(-4, 5))


starttime = time.time()
print(f"Starting program. Time: {starttime}")

print("Filtering data")
data = filter_data(PATH)
print(f"We have {len(data)} tweets to work with.")

print("Segmenting data.")
data_seg = segment_data(data)
print("Segmenting finished.")

# Plot the histogram
plt.bar(sentiment_scores, data_seg, color=colors, alpha=0.7)
plt.xlabel('Sentiment Score')
plt.ylabel('Retweets')
plt.title('Histogram of Retweets by Sentiment Score')
plt.grid(True)
plt.show()

print(f"Retweets: {data_seg}")


print("Calculating means")
data_means = calculate_mean(data)
print("Means calculated")

# Plot the histogram
plt.bar(sentiment_scores, data_means, color=colors, alpha=0.7)
plt.xlabel('Sentiment Score')
plt.ylabel('Mean of Retweets')
plt.title('Histogram of Means of Retweets by Sentiment Score')
plt.grid(True)
plt.show()

print(f"Means: {data_means}")


completed_time = time.time() - starttime
print(f"Program completed sucecsfully. Time : {round(completed_time, 2)} seconds")
