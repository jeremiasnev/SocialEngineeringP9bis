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
data = filter_data_sentiment_retweets(PATH, items=100000)
print(f"We have {len(data)} tweets to work with.")
sentiments, retweets = zip(*data)
counts = [0] * 9
for sen in sentiments:
    counts[sen + 4] += 1

c = 0
for tweet in retweets:
    if tweet > 0:
        c += 1

print(f"Tweets: {len(retweets)}, Tweets with Retweets: {c}")

    
# Plot the histogram
plt.plot(sentiment_scores, counts, alpha=0.7)
plt.xlabel('Sentiment Scores')
plt.ylabel('Counts')
plt.title('Distribution of Sentiment Scores')
plt.grid(True)
plt.show()
l = len(sentiments)
print(f"Percentage per tweet by sentiment score:\n -4: {counts[0]}\n -3: {counts[1]}\n -2: {counts[2]}\n -1: {counts[3]}\n 0: {counts[4]}\n 1: {counts[5]}\n 2: {counts[6]}\n 3: {counts[7]}\n 4: {counts[8]}")

# Calculate cumulative distribution
cumulative_counts = [sum(counts[:i+1]) for i in range(len(counts))]
total_tweets = sum(counts)
cumulative_distribution = [count / total_tweets for count in cumulative_counts]

# Plot the cumulative distribution
plt.plot(sentiment_scores, cumulative_distribution, alpha=0.7)
plt.xlabel('Sentiment Scores')
plt.ylabel('Cumulative Distribution')
plt.title('Cumulative Distribution of Sentiment Scores')
plt.grid(True)
plt.show()




completed_time = time.time() - starttime
print(f"Program completed sucecsfully. Time : {round(completed_time, 2)} seconds")