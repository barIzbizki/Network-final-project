import pandas as pd
import matplotlib.pyplot as plt

def plot_flow_volumes(csv_files, labels):
    flow_volumes = {}

    for file, label in zip(csv_files, labels):
        try:
            df = pd.read_csv(file)  # reading from csv file
        except FileNotFoundError:
            print(f"Error: The file '{file}' was not found.")
            flow_volumes[label] = None
            continue
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{file}' is empty.")
            flow_volumes[label] = None
            continue
        except Exception as e:
            print(f"Error: An unexpected error occurred while reading '{file}': {e}")
            flow_volumes[label] = None
            continue

        if 'Length' not in df.columns:
            print(f"Error: File '{file}' does not contain a 'Length' column.")
            flow_volumes[label] = None
            continue

        df['Length'] = pd.to_numeric(df['Length'], errors='coerce')  # check that the length is a number
        flow_volumes[label] = df['Length'].mean()  # calculate the mean

    # Filter out None values to avoid plotting empty bars
    flow_volumes = {k: v for k, v in flow_volumes.items() if v is not None}

    if not flow_volumes:
        print("No valid flow volumes to plot.")
        return

    # plot
    plt.bar(flow_volumes.keys(), flow_volumes.values(), color='lightseagreen')
    plt.title('Average Flow Volume (Bytes Transmitted) per Application', fontsize=14)
    plt.xlabel('Application', fontsize=12)
    plt.ylabel('Average Bytes per Packet', fontsize=12)
    plt.show()


csv_files = ['youtube.csv', 'zoom.csv', 'chrome.csv', 'edge.csv', 'spotify.csv']  # put the name of the csv file name
labels = ['YouTube', 'Zoom', 'Chrome', 'Edge', 'Spotify']  # the labels
plot_flow_volumes(csv_files, labels)
