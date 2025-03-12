import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calculate_avg_inter_arrival_time(filenames):
    avg_times = []

    # calculating the mean time per rec
    for file in filenames:
        try:
            df = pd.read_csv(file)  # reading from csv file
        except FileNotFoundError:
            print(f"Error: The file '{file}' was not found.")
            avg_times.append(None)
            continue
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{file}' is empty.")
            avg_times.append(None)
            continue
        except Exception as e:
            print(f"Error: An unexpected error occurred while reading '{file}': {e}")
            avg_times.append(None)
            continue

        if 'Time' not in df.columns:
            print(f"Error: File '{file}' does not contain a 'Time' column.")
            avg_times.append(None)
            continue

        timestamps = df['Time'].values  # taking the time of the packets
        inter_arrival_times = np.diff(timestamps)  # calculating the difference
        avg_inter_arrival = np.mean(inter_arrival_times)  # mean time
        avg_times.append(avg_inter_arrival)  # adding the mean time to the list of mean times

    return avg_times


def plot_avg_inter_arrival_time(filenames, labels):
    avg_times = calculate_avg_inter_arrival_time(filenames)

    # plot
    plt.figure(figsize=(10, 6))
    plt.bar(labels, avg_times, color='skyblue', edgecolor='black')
    plt.xlabel('File')
    plt.ylabel('Average Inter-Arrival Time (seconds)')
    plt.title('Average Inter-Arrival Time for Each File')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(bottom=0.30)  # space in the bottom
    plt.show()


csv_files = ['chrome.csv', 'zoom.csv', 'spotify.csv', 'edge.csv', 'youtube.csv']  # put the name of the csv file name
labels = ['Chrome', 'Zoom', 'Spotify', 'Edge', 'YouTube']  # the labels
plot_avg_inter_arrival_time(csv_files, labels)
