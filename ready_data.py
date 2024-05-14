import matplotlib.pyplot as plt
import statistics
import time
import data_processing

# Path to the unzipped dataset file
dataset_path = "tweets_cov19.tsv"
dest_file = "dest.txt"
starttime = time.time()
# Define column names
columns = ["Tweet Id", "Username", "Timestamp", "#Followers", "#Friends", "#Retweets", "#Favorites", "Entities", "Sentiment", "Mentions", "Hashtags", "URLs"]

# Get the total number of lines in the dataset file
with open(dataset_path, 'r', encoding='utf-8') as file:
    total_lines = sum(1 for line in file)

# Initialize a counter for the lines read
negatives = []
positives = []
neutrals = []
_data = []
lines_read = 0
items = 100000

# Load the dataset into a DataFrame
with open(dest_file, 'a', encoding='utf-8') as dest:
    with open(dataset_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                data = line.strip().split('\t')
                if len(data) == len(columns):
                    # Convert timestamp to a timezone-aware datetime object
                    sentiment = data[columns.index("Sentiment")].split(" ")
                    sent = int(sentiment[0]) + int(sentiment[1])
                    retweets = data[columns.index("#Retweets")]
                    """ if sent > 0:
                        positives.append(int(retweets))
                    elif sent == 0:
                        neutrals.append(int(retweets))
                    else:
                        negatives.append(int(retweets)) """
                    _data.append((sent, int(retweets)))
                else:
                    print(f"Skipping line {line_number}: Incorrect number of fields")
            except Exception as e:
                print(f"Error parsing line {line_number}: {e}")
            
            # Increment the lines_read counter
            lines_read += 1

            if lines_read >= items:
                break

            # Calculate the percentage completed
            progress = (lines_read / total_lines) * 100
            print(f"Progress: {progress:.2f}% ({lines_read}/{total_lines} lines processed)", end='\r')


print(f"Info: Length {len(_data)}, Mean {statistics.mean(_data[1])}")
data_segmented = [0 for _ in range(9)]
for d in _data:
    idx = d[0] + 4
    data_segmented[idx] += d[1]
data_mean = data_processing.calculate_mean(_data)
print(f"Data: {data_mean}")

# Sentiment scores
sentiment_scores = list(range(-4, 5))
colors = ["red", "red", "red", "yellow", "yellow", "yellow", "green", "green", "green"]
sentiments, retweets = zip(*_data)

endttime = time.time() - starttime
print(f"Time to complete: {round(endttime, 2)}s, when using {items} tweets")

# Plot the histogram
plt.bar(sentiment_scores, data_mean, color=colors, alpha=0.7)
plt.xlabel('Sentiment Score')
plt.ylabel('Mean of Retweets')
plt.title('Histogram of Retweets by Sentiment Score')
plt.grid(True)
plt.show()

