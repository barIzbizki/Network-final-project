import pandas as pd
import matplotlib.pyplot as plt

def calculate_rtt(csv_file):
    try:
        # reading the data from the csv file
        df = pd.read_csv(csv_file)

        # filtering SYN and SYN-ACK packets
        syn_packets = df[df['Info'].str.contains(r'\[SYN\]', na=False)]
        syn_ack_packets = df[df['Info'].str.contains(r'\[SYN, ACK\]', na=False)]

        rtt_data = []

        # for each SYN packet, find the matching SYN-ACK packet
        for _, syn_row in syn_packets.iterrows():
            source = syn_row['Source']
            destination = syn_row['Destination']
            time_sent = syn_row['Time']

            matching_ack = syn_ack_packets[
                (syn_ack_packets['Source'] == destination) &
                (syn_ack_packets['Destination'] == source) &
                (syn_ack_packets['Time'] > time_sent)
            ].head(1)

            if not matching_ack.empty:
                time_received = matching_ack.iloc[0]['Time']
                rtt = time_received - time_sent
                rtt_data.append(rtt)

        return pd.DataFrame(rtt_data, columns=['RTT'])

    except Exception as e:
        print(f"Failed to open the file '{csv_file}'. Error: {e}")
        return pd.DataFrame(columns=['RTT'])
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return pd.DataFrame(columns=['RTT'])
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file}' is empty.")
        return pd.DataFrame(columns=['RTT'])


def plot_rtt_distribution(rtt_df):
    if rtt_df.empty:
        print("No RTT data available for plotting.")
        return

    plt.figure(figsize=(10, 5))
    plt.hist(rtt_df['RTT'], bins=30, color='skyblue', edgecolor='black')
    plt.xlabel("RTT (seconds)")
    plt.ylabel("Packet Count")
    plt.title("RTT Distribution")
    plt.show()


csv_file = "spotify.csv"  # put the CSV file name
rtt_df = calculate_rtt(csv_file)
plot_rtt_distribution(rtt_df)
