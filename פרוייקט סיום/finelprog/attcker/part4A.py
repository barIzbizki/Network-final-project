import os
import pandas as pd
from scapy.all import rdpcap
import hashlib
from collections import Counter


def create_flowid(pkt):
    if 'IP' in pkt and ('TCP' in pkt or 'UDP' in pkt):
        src_ip = pkt['IP'].src
        dst_ip = pkt['IP'].dst
        src_port = pkt.sport
        dst_port = pkt.dport
        flow_tuple = f"{src_ip}-{dst_ip}-{src_port}-{dst_port}"
        return hashlib.md5(flow_tuple.encode()).hexdigest()
    return None


def process_pcapng(file_path):
    packets = rdpcap(file_path)

    # lists for the values per packet
    packet_sizes = []
    timestamps = []
    flow_ids = []

    for p in packets:
        pkt_size = len(p)  # the size of the packet
        pkt_time = p.time  # the interarrival time of the packet
        flowid = create_flowid(p)  # the flowid of the packet
        # add the values to the lists:
        packet_sizes.append(pkt_size)
        timestamps.append(pkt_time)
        if flowid:
            flow_ids.append(flowid)

    # calculating the mean of all the packets int the rec:
    mean_packet_size = sum(packet_sizes) / len(packet_sizes) if len(packet_sizes) > 0 else 0
    interarrival_times = [t - s for s, t in zip(timestamps, timestamps[1:])] or [0]
    mean_interarrival_time = sum(interarrival_times) / len(interarrival_times) if len(interarrival_times) > 0 else 0
    if flow_ids:
        most_common_flow_id, _ = Counter(flow_ids).most_common(1)[0]
    else:
        most_common_flow_id = None

    return {
        "MeanPacketSize": mean_packet_size,
        "MeanInterarrivalTime": mean_interarrival_time,
        "MostCommonFlowID": most_common_flow_id
    }


def process_directory(directory_path):
    summary_data = []

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".pcapng"):  # if the file is from typ pcapng
            file_path = os.path.join(directory_path, file_name)

            # choose the label of the rec
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

            record = process_pcapng(file_path)
            summary_data.append({
                "MeanPacketSize": record["MeanPacketSize"],
                "MeanInterarrivalTime": record["MeanInterarrivalTime"],
                "MostCommonFlowID": record["MostCommonFlowID"],
                "Label": label
            })

    summary_df = pd.DataFrame(summary_data)

    # save in csv
    output_path = os.path.join(directory_path, "train_flowid.csv")
    summary_df.to_csv(output_path, index=False)

    print(f"Summary table with FlowID created and saved successfully at {output_path}")


directory_path = /mnt/c/network1/finelprog/p4 # put your path
process_directory(directory_path)
