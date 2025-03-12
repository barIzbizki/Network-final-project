import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def count_by_protocol(file):
    # Load the csv file into a dataframe
    df = pd.read_csv(file, encoding='ISO-8859-1')
    df['Protocol'] = df['Protocol'].fillna('Unknown')  # Replace NaN with 'Unknown'

    protocol_packet_count = defaultdict(int)

    # Count occurrences of each protocol
    for protocol in df['Protocol']:
        protocol_packet_count[protocol] += 1

    # Extract protocol names and counts
    protocols = list(protocol_packet_count.keys())
    packet_counts = list(protocol_packet_count.values())

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(protocols, packet_counts, color='lightcoral', edgecolor='black')
    plt.xlabel("Protocol")
    plt.ylabel("Number of Packets")
    plt.title(f"Protocols in {file}")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(bottom=0.30)  # Space in the bottom
    plt.show()


csv_file = 'zoom.csv'  # Specify the CSV file name
count_by_protocol(csv_file)
