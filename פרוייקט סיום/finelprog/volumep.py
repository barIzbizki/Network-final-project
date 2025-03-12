import pandas as pd
import matplotlib.pyplot as plt

def plot_flow_volumes(csv_files, labels):
    flow_volumes = {}

    for file, label in zip(csv_files, labels):
        df = pd.read_csv(file)  # reading from csv file
        df['Length'] = pd.to_numeric(df['Length'], errors='coerce')  # check that the length is number
        flow_volumes[label] = df['Length'].mean()  # calculate the mean

    #plot
    plt.bar(flow_volumes.keys(), flow_volumes.values(), color='lightseagreen')
    plt.title('Average Flow Volume (Bytes Transmitted) per Application', fontsize=14)
    plt.xlabel('Application', fontsize=12)
    plt.ylabel('Average Bytes per Packet', fontsize=12)
    plt.show()


csv_files = ['youtube.csv', 'zoom.csv', 'chrome.csv', 'edge.csv', 'spotify.csv']  # put the name of the csv file name
labels = ['YouTube', 'Zoom', 'Chrome', 'Edge', 'Spotify']  # the labels
plot_flow_volumes(csv_files, labels)
