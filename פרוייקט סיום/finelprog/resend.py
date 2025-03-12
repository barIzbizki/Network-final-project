import pandas as pd
import matplotlib.pyplot as plt

def count_retransmissions(csv_file):

    df = pd.read_csv(csv_file, encoding='ISO-8859-1')  # reading from csv file
    retransmissions_count = df['Info'].str.contains('Retransmission', na=False).sum()  # count the packets that sent again by searching the word "Retransmission" in the info

    return retransmissions_count


def plot_retransmissions(csv_files):
    retransmission_counts = []
    labels = [file.replace('.csv', '') for file in csv_files]  # taking of the .csv

    for file in csv_files:  # for each file calculating the number of retransmission packets and adding it to the list
        retransmission_count = count_retransmissions(file)
        retransmission_counts.append(retransmission_count)

    #plot
    plt.figure(figsize=(10, 6))
    plt.bar(labels, retransmission_counts, color='skyblue', edgecolor='black')  # שימוש ב-labels בלי .csv
    plt.xlabel('Type')
    plt.ylabel('Retransmissions Count')
    plt.title('Resend')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(bottom=0.30)  # space in the bottom
    plt.show()


csv_files = ['chrome.csv', 'zoom.csv', 'spotify.csv', 'edge.csv', 'youtube.csv']  # put the name of the csv file name
plot_retransmissions(csv_files)
