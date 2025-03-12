import pandas as pd
import matplotlib.pyplot as plt


def plot_packet_counts(csv_files, labels):
    packet_counts = {}

    for file, label in zip(csv_files, labels):
        df = pd.read_csv(file)  # reading from csv file
        first_time = df['Time'].iloc[0]  # the time of the first packet
        time_limit = first_time + 10  # 10 seconds after the first packet
        packets_within_time_limit = df[df['Time'] <= time_limit]  # taking only the packets that in the rang of time
        packet_counts[label] = packets_within_time_limit.shape[0]  # count how many

    # plot
    plt.bar(packet_counts.keys(), packet_counts.values(), color='lightcoral')
    plt.title('Number of Packets per Application (within 10 seconds)', fontsize=14)
    plt.xlabel('Application', fontsize=12)
    plt.ylabel('Number of Packets (within 10s)', fontsize=12)
    plt.show()


csv_files = ['youtube.csv', 'zoom.csv', 'chrome.csv', 'edge.csv', 'spotify.csv']  # put the name of the csv file name
labels = ['YouTube', 'Zoom', 'Chrome', 'Edge', 'Spotify']  # the labels
plot_packet_counts(csv_files, labels)
