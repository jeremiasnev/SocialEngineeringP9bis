import matplotlib.pyplot as plt
from data_processing import *

def analyse_social(_data, idx):

    _data = _data.copy()
    _data = sorted(_data, key=lambda x: int(x[idx]), reverse=False)

    borders = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, int(_data[-1][idx])]
    retweets_list = [[] for _ in range(len(borders))]
    i = 0
    for d in _data:
        f = d[idx]
        retweets = d[2]
        if int(f) > borders[i]:
            i += 1
        retweets_list[i].append(int(retweets))
    
    return retweets_list

def analyse_counts(_data, idx):

    _data = _data.copy()
    retweets_list = [[] for _ in range(3)]

    for d in _data:
        f = d[idx]
        retweets = d[2]
        f = f.split(";")
        f = [item for item in f if item.strip()]
        if len(f) == 0 or f[0] == "null":
            retweets_list[0].append(int(retweets))
        elif len(f) == 1:
            retweets_list[1].append(int(retweets))
        elif len(f) >= 2:
            retweets_list[2].append(int(retweets))
        else:
            print("Error in count analysis")
    return retweets_list





PATH = "tweets_cov19.tsv"

items = None

# Filter data using function from data_processing
data = filter_data(PATH, features=["#Followers", "#Friends", "#Retweets", "#Favorites", "Entities", "Sentiment", "Mentions", "Hashtags", "URLs"], show_progress=True, items=items)

print("\n")

# Get arrays for each feature
followers, friends, retweets, favourites, entities, sentiment, mentions, hashtags, urls = zip(*data)

# Socials analysis
labels_social = ["0-10", "11-100", "101-1000", "1001-5000", "5001-10000", "10001-50000", "50001-100000", "100001-500000", "500000->"]
retw_follow = analyse_social(data, 0)
retw_friend = analyse_social(data, 1)
retw_fav = analyse_social(data, 3)

mean_retweets_follow = [sum(retw) / len(retw) if len(retw) > 0 else 0 for retw in retw_follow]
mean_retweets_friend = [sum(retw) / len(retw) if len(retw) > 0 else 0 for retw in retw_friend]
mean_retweets_fav = [sum(retw) / len(retw) if len(retw) > 0 else 0 for retw in retw_fav]

# String analysis
labels_count = ["0", "1", "2+"]
colors = ["red", "yellow", "green"]

retw_entities = analyse_counts(data, 4)
retw_mentions = analyse_counts(data, 6)
retw_hashtags = analyse_counts(data, 7)
retw_urls = analyse_counts(data, 8)

mean_retweets_entities = [sum(retw) / len(retw) if len(retw) > 0 else 0 for retw in retw_entities]
mean_retweets_mentions = [sum(retw) / len(retw) if len(retw) > 0 else 0 for retw in retw_mentions]
mean_retweets_hashtags = [sum(retw) / len(retw) if len(retw) > 0 else 0 for retw in retw_hashtags]
mean_retweets_urls = [sum(retw) / len(retw) if len(retw) > 0 else 0 for retw in retw_urls]



plt.bar(labels_social, mean_retweets_follow)
plt.xlabel('Follow Counts')
plt.ylabel('Mean Retweets')
plt.title('Mean Retweets vs Follow')
plt.grid(True)
plt.show()

plt.bar(labels_social, mean_retweets_friend)
plt.xlabel('Friend Counts')
plt.ylabel('Mean Retweets')
plt.title('Mean Retweets vs Friends')
plt.grid(True)
plt.show()

plt.bar(labels_social, mean_retweets_fav)
plt.xlabel('Favourites Counts')
plt.ylabel('Mean Retweets')
plt.title('Mean Retweets vs Favourites')
plt.grid(True)
plt.show()

plt.bar(labels_count, mean_retweets_entities, color = colors)
plt.xlabel('Entities Counts')
plt.ylabel('Mean Retweets')
plt.title('Mean Retweets vs Entities')
plt.grid(True)
plt.show()

plt.bar(labels_count, mean_retweets_mentions, color = colors)
plt.xlabel('Mentions Counts')
plt.ylabel('Mean Retweets')
plt.title('Mean Retweets vs Mentionss')
plt.grid(True)
plt.show()

plt.bar(labels_count, mean_retweets_hashtags, color = colors)
plt.xlabel('Hashtags Counts')
plt.ylabel('Mean Retweets')
plt.title('Mean Retweets vs Hashtags')
plt.grid(True)
plt.show()

plt.bar(labels_count, mean_retweets_urls, color = colors)
plt.xlabel('URLs Counts')
plt.ylabel('Mean Retweets')
plt.title('Mean Retweets vs URLs')
plt.grid(True)
plt.show()


