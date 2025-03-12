import pandas as pd
import matplotlib.pyplot as plt


def plot_avg_packet_size(filenames, labels):

    avg_sizes = []

    # calculating the mean size of packet per rec
    for file in filenames:
        df = pd.read_csv(file)  #readin from the csv file
        sizes = df['Length'].tolist()  # taking the length of the packets
        avg_packet_size = sum(sizes) / len(sizes)
        avg_sizes.append(avg_packet_size)  # adding to the mean list

    # plot
    plt.figure(figsize=(10, 6))
    plt.bar(labels, avg_sizes, color='skyblue', edgecolor='black')
    plt.xlabel('File')
    plt.ylabel('Average Packet Size (bytes)')
    plt.title('Average Packet Size for Each File')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(bottom=0.30)  # space in the bottom
    plt.show()


csv_files = ['chrome.csv', 'zoom.csv', 'spotify.csv', 'edge.csv', 'youtube.csv']  # put the name of the csv file name
labels = ['Chrome', 'Zoom', 'Spotify', 'Edge', 'YouTube']  # the labels
plot_avg_packet_size(csv_files, labels)
