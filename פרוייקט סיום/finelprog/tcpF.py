import pandas as pd
import matplotlib.pyplot as plt


def extract_tcp_flags(info):
    # the optional flags
    tcp_flags = ['SYN', 'ACK', 'PSH', 'RST', 'FIN', 'URG']

    # checking witch flag do we have
    flags_found = [flag for flag in tcp_flags if flag in info]

    return flags_found



def plot_tcp_flags(csv_file):
    df = pd.read_csv(csv_file, encoding='ISO-8859-1') #reading from csv

    all_flags = []

    for _, row in df.iterrows():
        info = row.get('Info', '')
        if pd.notna(info):  # if is nit nun
            flags = extract_tcp_flags(info)
            all_flags.extend(flags)  # adding to the list

    if not all_flags:
        print("no flags.")
        return

    """
     Counting the occurrences of each unique flag
     all_flags – A variable containing a list of flags from network packets.
     pd.Series(all_flags) – Converts the all_flags list into a Pandas Series.
     .value_counts() – Counts the occurrences of each unique value in the Series
     and returns a new Series where:
     - The keys are the unique flag values.
     - The values represent the number of occurrences of each flag.
    """
    flag_counts = pd.Series(all_flags).value_counts()

    #plot
    plt.figure(figsize=(10, 6))
    flag_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel('TCP Flags')
    plt.ylabel('Count')
    plt.title('TCP Flags')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()


csv_file = 'zoom.csv'  # put your csv file name
plot_tcp_flags(csv_file)
