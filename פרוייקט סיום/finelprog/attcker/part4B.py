import os
import pandas as pd
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
    try:
        packets = rdpcap(file_path)  # Try reading the pcap file
    except Exception as e:
        print(f"Error: Unable to open or process the file '{file_path}': {e}")
        return None

    packet_sizes = []
    timestamps = []

    for pkt in packets:
        pkt_size = len(pkt)
        pkt_time = pkt.time

        packet_sizes.append(pkt_size)
        timestamps.append(pkt_time)

    mean_packet_size = sum(packet_sizes) / len(packet_sizes) if len(packet_sizes) > 0 else 0
    interarrival_times = [t - s for s, t in zip(timestamps, timestamps[1:])] or [0]
    mean_interarrival_time = sum(interarrival_times) / len(interarrival_times) if len(interarrival_times) > 0 else 0

    return {
        "MeanPacketSize": mean_packet_size,
        "MeanInterarrivalTime": mean_interarrival_time
    }


def process_directory(directory_path):
    summary_data = []

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".pcapng"):
            file_path = os.path.join(directory_path, file_name)

            # Assign label based on the file name
            if file_name.lower().startswith('ch'):
                label = 'Chrome'
            elif file_name.lower().startswith('ed'):
                label = 'Edge'
            elif file_name.lower().startswith('s'):
                label = 'Spotify'
            elif file_name.lower().startswith('yo'):
                label = 'YouTube'
            elif file_name.lower().startswith('zo'):
                label = 'Zoom'
            else:
                label = 'Unknown'

            record = process_pcap(file_path)
            if record:  # Only add the record if processing was successful
                summary_data.append({
                    "MeanPacketSize": record["MeanPacketSize"],
                    "MeanInterarrivalTime": record["MeanInterarrivalTime"],
                    "Label": label
                })

    if summary_data:
        summary_df = pd.DataFrame(summary_data)

        # Save the summary as a CSV file
        summary_df.to_csv(os.path.join(directory_path, "train2_table.csv"), index=False)

        print("Summary table created and saved successfully.")
    else:
        print("No valid data to process. No summary file was created.")


directory_path = "/mnt/c/network1/finelprog/p4"  # Specify your path here
process_directory(directory_path)
