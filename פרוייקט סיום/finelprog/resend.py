import pandas as pd
import matplotlib.pyplot as plt

def count_retransmissions(csv_file):
    try:
        df = pd.read_csv(csv_file, encoding='ISO-8859-1')  # reading from csv file

        # Ensure required column exists
        if 'Info' not in df.columns:
            raise KeyError("Missing required column: 'Info'.")

        # Count the packets that were retransmitted by searching for "Retransmission" in the 'Info' column
        retransmissions_count = df['Info'].str.contains('Retransmission', na=False).sum()

        return retransmissions_count

    except Exception as e:
        print(f"error with file '{csv_file}': {e}")
        return 0
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return 0
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file}' is empty.")
        return 0


def plot_retransmissions(csv_files):
    retransmission_counts = []
    labels = [file.replace('.csv', '') for file in csv_files]  # removing ".csv" from labels

    for file in csv_files:  # for each file, calculate the number of retransmissions and add it to the list
        retransmission_count = count_retransmissions(file)
        retransmission_counts.append(retransmission_count)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(labels, retransmission_counts, color='skyblue', edgecolor='black')
    plt.xlabel('Type')
    plt.ylabel('Retransmissions Count')
    plt.title('Resend')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(bottom=0.30)  # space in the bottom
    plt.show()


csv_files = ['chrome.csv', 'zoom.csv', 'spotify.csv', 'edge.csv', 'youtube.csv']  # list of csv files
plot_retransmissions(csv_files)
