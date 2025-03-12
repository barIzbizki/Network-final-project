import pandas as pd
import matplotlib.pyplot as plt

def plot_new_connections_for_files(file_list):

    new_connections_counts = []

    for csv_file in file_list:
        try:
            # read the CSV file
            df = pd.read_csv(csv_file, encoding='ISO-8859-1')

            # filter packets to take only TCP packets
            df_tcp_syn = df[df['Protocol'] == 'TCP'].copy()

            # filter and take only SYN packets
            df_tcp_syn.loc[:, 'New_Connection'] = df_tcp_syn['Info'].apply(lambda x: 'SYN' in str(x))

            # count the number of packets
            new_connections_count = df_tcp_syn['New_Connection'].sum()
            new_connections_counts.append(new_connections_count)

        except Exception as e:
            print(f"Failed to process the file {csv_file}. Error: {e}")
            new_connections_counts.append(0)
        except FileNotFoundError:
            print(f"Error: The file '{csv_file}' was not found.")
            new_connections_counts.append(0)
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{csv_file}' is empty.")
            new_connections_counts.append(0)


    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(file_list, new_connections_counts, color='lightcoral')
    plt.title('Count of New Connections')
    plt.xlabel('File')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(bottom=0.30)  # space at the bottom
    plt.show()

files = ['chrome.csv', 'edge.csv', 'spotify.csv', 'youtube.csv', 'zoom.csv']  # put the name of the CSV file
plot_new_connections_for_files(files)
