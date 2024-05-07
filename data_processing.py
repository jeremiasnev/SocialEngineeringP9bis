

def calculate_length(path):
    with open(path, 'r', encoding='utf-8') as file:
        total_lines = sum(1 for line in file)
    return total_lines

def calculate_mean(data, depth = 9):
    sums = [0 for _ in range(depth)]
    counts = [0 for _ in range(depth)]
    for d in data:
        idx = d[0] + 4
        sums[idx] += d[1]
        counts[idx] += 1
    for n, s in enumerate(sums):
        print(f"Mean for enum {n} is {s / counts[n]}, where sum is {s} and len is {counts[n]}")
        sums[n] = round(s / counts[n], 1)
    return sums

def segment_data(data):
    data_segmented = [0 for _ in range(9)]
    for d in data:
        idx = d[0] + 4
        data_segmented[idx] += d[1]

    return data_segmented

def filter_data(dataset_path, show_progress = True, items = None):
    _data = []
    if items == None:
        total_lines = calculate_length(dataset_path)

    columns = ["Tweet Id", "Username", "Timestamp", "#Followers", "#Friends", "#Retweets", "#Favorites", "Entities", "Sentiment", "Mentions", "Hashtags", "URLs"]

    lines_read = 0
    # Load the dataset into a DataFrame
    with open(dataset_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                data = line.strip().split('\t')
                if len(data) == len(columns):
                    # Convert timestamp to a timezone-aware datetime object
                    sentiment = data[columns.index("Sentiment")].split(" ")
                    sent = int(sentiment[0]) + int(sentiment[1])
                    retweets = data[columns.index("#Retweets")]
                    _data.append((sent, int(retweets)))
                else:
                    print(f"Skipping line {line_number}: Incorrect number of fields")
            except Exception as e:
                print(f"Error parsing line {line_number}: {e}")
            
            # Increment the lines_read counter
            lines_read += 1

            if items != None and lines_read >= items:
                break

            if show_progress:
                if items == None:
                    items = total_lines
                # Calculate the percentage completed
                progress = (lines_read / items) * 100
                print(f"Progress: {progress:.2f}% ({lines_read}/{items} lines processed)", end='\r')
            
    return _data