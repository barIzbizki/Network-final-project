import os
import random
import pandas as pd
from collections import Counter
from scapy.all import rdpcap
import hashlib


def create_flow_id(pkt):
    if 'IP' in pkt and ('TCP' in pkt or 'UDP' in pkt):
        src_ip = pkt['IP'].src
        dst_ip = pkt['IP'].dst
        src_port = pkt.sport
        dst_port = pkt.dport
        flow_tuple = f"{src_ip}-{dst_ip}-{src_port}-{dst_port}"
        return hashlib.md5(flow_tuple.encode()).hexdigest()
    return None


def process_pcap(file_path):
    packets = rdpcap(file_path)

    packet_sizes = []
    timestamps = []

    for pkt in packets:
        pkt_size = len(pkt)
        pkt_time = pkt.time

        packet_sizes.append(pkt_size)
        timestamps.append(pkt_time)

    mean_packet_size = sum(packet_sizes) / len(packet_sizes) if packet_sizes else 0
    interarrival_times = [t - s for s, t in zip(timestamps, timestamps[1:])] or [0]
    mean_interarrival_time = sum(interarrival_times) / len(interarrival_times) if interarrival_times else 0

    return {
        "MeanPacketSize": float(mean_packet_size),
        "MeanInterarrivalTime": float(mean_interarrival_time)
    }


summary_df = pd.read_csv("train2_table.csv")

min_size = summary_df['MeanPacketSize'].min()
max_size = summary_df['MeanPacketSize'].max()
min_interarrival = summary_df['MeanInterarrivalTime'].min()
max_interarrival = summary_df['MeanInterarrivalTime'].max()


def calculate_distance(record1, record2):
    size_diff = abs(float(record1['MeanPacketSize']) - float(record2['MeanPacketSize']))
    interarrival_diff = abs(float(record1['MeanInterarrivalTime']) - float(record2['MeanInterarrivalTime']))

    norm_size = (size_diff - min_size) / (max_size - min_size) if max_size != min_size else 0
    norm_interarrival = (interarrival_diff - min_interarrival) / (
                max_interarrival - min_interarrival) if max_interarrival != min_interarrival else 0

    return (norm_size + norm_interarrival) / 2


def knn_predict(new_record, k=5):
    distances = []

    for _, row in summary_df.iterrows():
        dist = calculate_distance(new_record, row)
        distances.append((dist, row['Label']))

    distances.sort(key=lambda x: x[0])
    nearest_neighbors = distances[:k]

    labels = [neighbor[1] for neighbor in nearest_neighbors]
    most_common_label = Counter(labels).most_common(1)[0][0]

    return most_common_label


def predict_from_pcap(pcap_file):
    new_record = process_pcap(pcap_file)
    predicted_label = knn_predict(new_record, k=3)
    return predicted_label


def predict_on_random_samples(directory_path, num_iterations=100):
    pcap_files = [f for f in os.listdir(directory_path) if f.endswith(".pcapng")]

    if not pcap_files:
        print("No pcapng files found in the directory.")
        return

    count_t = 0
    for _ in range(num_iterations):
        file_name = random.choice(pcap_files)
        file_path = os.path.join(directory_path, file_name)
        predicted_label = predict_from_pcap(file_path)
        print(f"File: {file_name} -> Predicted Label: {predicted_label}")

        if file_name[0].lower() == predicted_label[0].lower():
            count_t += 1

    print(f"Number of correct predictions: {count_t}%")


directory_path = /mnt/c/network1/finelprog/p4/rec
predict_on_random_samples(directory_path, num_iterations=100)

