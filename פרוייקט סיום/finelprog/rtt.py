import pandas as pd
import matplotlib.pyplot as plt


def calculate_rtt(csv_file):
    # reading the data from the csv file
    df = pd.read_csv(csv_file)

    # filtering SYN and SYN-ACK packets
    syn_packets = df[df['Info'].str.contains(r'\[SYN\]', na=False)]
    syn_ack_packets = df[df['Info'].str.contains(r'\[SYN, ACK\]', na=False)]

    rtt_data = []

    """""
    for each SYN packet, we check the destination, source, and timestamp,
    and search for the first matching packet where the destination matches the source of the SYN packet, 
    and the source matches its destination.
    """
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


def plot_rtt_distribution(rtt_df):
    plt.figure(figsize=(10, 5))
    plt.hist(rtt_df['RTT'], bins=30, color='skyblue', edgecolor='black')
    plt.xlabel("RTT (seconds)")
    plt.ylabel("Packet Count")
    plt.title("RTT Distribution")
    plt.show()


csv_file = "spotify.csv"  # put your csv file name
rtt_df = calculate_rtt(csv_file)
plot_rtt_distribution(rtt_df)

