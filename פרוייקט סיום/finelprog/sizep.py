import pandas as pd
import matplotlib.pyplot as plt


def plot_avg_packet_size(filenames, labels):
    avg_sizes = []

    # calculating the mean size of packet per rec
    for file in filenames:
        try:
            df = pd.read_csv(file)  # reading from the csv file
        except FileNotFoundError:
            print(f"Error: The file '{file}' was not found.")
            continue
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{file}' is empty.")
            continue
        except Exception as e:
            print(f"Error: An unexpected error occurred while reading '{file}': {e}")
            continue

        sizes = df['Length'].tolist()  # taking the length of the packets
        if sizes:  # Ensure that there is data to process
            avg_packet_size = sum(sizes) / len(sizes)
            avg_sizes.append(avg_packet_size)  # adding to the mean list
        else:
            avg_sizes.append(0)  # in case of an empty 'Length' column

    # plot
    if avg_sizes:
        plt.figure(figsize=(10, 6))
        plt.bar(labels, avg_sizes, color='skyblue', edgecolor='black')
        plt.xlabel('File')
        plt.ylabel('Average Packet Size (bytes)')
        plt.title('Average Packet Size for Each File')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.subplots_adjust(bottom=0.30)  # space in the bottom
        plt.show()
    else:
        print("No data to plot due to errors in loading the files.")


csv_files = ['chrome.csv', 'zoom.csv', 'spotify.csv', 'edge.csv', 'youtube.csv']  # put the name of the csv file name
labels = ['Chrome', 'Zoom', 'Spotify', 'Edge', 'YouTube']  # the labels
plot_avg_packet_size(csv_files, labels)
