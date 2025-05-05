# Final Project - Network Project

## Table of Contents
- [Project Description](#project-description)
- [Project Structure](#project-structure)
- [Part A: Visual Data Analysis](#part-a-visual-data-analysis)
- [Part B: Attack Simulation and Machine Learning](#part-b-attack-simulation-and-machine-learning)
- [System Requirements](#system-requirements)
- [Execution Instructions](#execution-instructions)


---

## Project Description

This project focuses on analyzing application data by generating graphs, building a machine learning model, and ultimately predicting results based on the data.

In this project, we decrypted encryption using environment variables and recorded data for each application. The recorded data was exported to CSV files, from which graphs were generated for analysis.

The second part of the project simulates an attacker monitoring the user's network traffic and classifying the information into relevant categories. In this part, we implement two possible scenarios:

1. **The attacker knows the packet size, timestamp, and flow ID** – This information helps identify the application or website in use.
2. **The attacker knows only the packet size and timestamp** – This scenario examines whether the attacker can still identify the website or application even if the traffic is encrypted, and how to mitigate such an attack.

---

## Project Structure

The project is divided into two main parts:

### Part A: Visual Data Analysis

In this phase, the collected data is presented using visual graphs. These graphs enable:

- Identifying trends and differences between different data groups.
- Revealing patterns and deriving meaningful insights.

### Part B: Attack Simulation and Machine Learning

In this phase, we simulate an attacker monitoring the user's network traffic. We use the **KNN machine learning algorithm** to identify the application the user is accessing.

Process steps:

1. **Data Processing** – Processing the collected data to extract insights and prepare it for model training.
2. **Model Training and Prediction** – Training the model using a large dataset and then predicting which application the user is accessing based on captured network traffic.

---

## System Requirements

The code is written in Python, making it compatible with both **Windows** and **Ubuntu** operating systems.

### Python Version

- Python 3.12

### Required Libraries

- `pandas` – For data processing and CSV file handling.
- `scapy` – For reading and analyzing PCAP files.
- `matplotlib` – For generating visual graphs.
- `numpy` – For time calculations, data processing, and distance computations.
- `hashlib` – For creating unique connection identifiers.
- `collections.Counter` – For counting occurrences in data.
- `csv` – For reading and writing CSV files (built-in in Python).
- `os` – For managing files and directories (built-in in Python).

---

## Execution Instructions

### Running the Codes in the Project

All the codes are located inside the **`finalprog`** directory. This directory contains:

- **Graph codes** (9 codes)
- **Five CSV files** extracted from Wireshark recordings
- An **`attacker`** folder, which includes 4 codes related to the attacker (Part 1, Part 2) and dataset creation

📝 **The Wireshark recordings are available in a shared Google Drive link.**

---

### Generating CSV Files from Wireshark

The CSV files were generated from Wireshark recordings. In our recorded sessions, we decrypted encrypted traffic using an environment variable that stores the encryption keys in `ssl.log`. This allowed Wireshark to interpret the encrypted packets correctly.

*(Tutorial reference: [YouTube Video](https://youtu.be/5qecyZHL-GU))*

Steps:

1. Open the `.pcapng` file in **Wireshark**.
2. Go to **File → Export Packet Dissections → As CSV**.
3. Select the desired fields: `No.`, `Time`, `Source`, `Destination`, `Protocol`, `Length`, `Info`.
4. Save the file in **CSV format**.

These CSV files were then used for analysis and visualization in the project.

---

## Running Each Code

### Graph Codes (9 codes)

#### 1. **Protocol Distribution** (`count_protocol.py`)
- Generates a protocol distribution graph.
- Requires a **single CSV file** at a time (e.g., `zoom.csv`).

#### 2. **TCP Flags** (`tcpF.py`)
- Generates a TCP flag distribution graph.
- Requires a **single CSV file** at a time.

#### 3. **Number of New Connections** (`newcon.py`)
- Displays distribution of new connections across all datasets.
- Requires **all CSV files together**.

#### 4. **Number of Retransmitted Packets** (`ressend.py`)
- Shows retransmitted packets distribution across all datasets.
- Requires **all CSV files together**.

#### 5. **RTT Calculation** (`rtt.py`)
- Analyzes RTT distribution.
- Requires a **single CSV file** at a time.

#### 6. **Average Time Between Two Packets** (`time.py`)
- Displays average time between packets distribution across datasets.
- Requires **all CSV files together**.

#### 7. **Flow Size** (`sizeflow.py`)
- Shows flow size distribution across datasets.
- Requires **all CSV files together**.

#### 8. **Average Packet Size** (`sizep.py`)
- Displays average packet size distribution across datasets.
- Requires **all CSV files together**.

#### 9. **Flow Volume** (`volumep.py`)
- Represents flow volume across datasets.
- Requires **all CSV files together**.

---

## `attacker` Directory

This directory contains **four codes**, two for each part:

### Training CSV Creation

- **`Part4A` / `Part4B`** – Generate training CSV files.
- To run:
  1. Download the Wireshark recordings from the shared Drive (or create your own recordings).
  2. Update the code with the correct directory path to the recordings.

---

### Testing Execution

- **`Part4t1` / `Part4t2`** – Run the test phase.
- Included:
  - Two CSV files used for predictions.
  - The dataset used in our work.

👉 If you use the included CSV files, **you do not need to run Part4A and Part4B.**

Files:

- `train_flowid` – CSV file for the first part.
- `train2_table` – CSV file for the second part.

---

## Execution Modes

✅ **Batch Mode (100 Samples)**

- Ensure the code points to the directory containing all the test recordings.

✅ **Single Prediction Mode**

- Update the code with the path of the specific recording you want to analyze.

⚠️ **Important: All recordings must be in PCAPNG format.**

---
