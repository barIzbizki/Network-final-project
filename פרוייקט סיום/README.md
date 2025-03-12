# README - Final project network Project

## Table of Contents

1. [Project Description](#project-description)
2. [Project Structure](#project-structure)
   - [Part A: Visual Data Analysis](#part-a-visual-data-analysis)
   - [Part B: Attack Simulation and Machine Learning](#part-b-attack-simulation-and-machine-learning)
3. [System Requirements](#system-requirements)
4. [Execution Instructions](#execution-instructions)
5. [Data Files](#data-files)

## Project Description

This project focuses on analyzing application data by generating graphs, building a machine learning model, and ultimately predicting results based on the data.

In this project, we decrypted encryption using environment variables and recorded data for each application. The recorded data was exported to CSV files, from which graphs were generated for analysis.

The second part of the project simulates an attacker monitoring the user's network traffic and classifying the information into relevant categories. In this part, we implement two possible scenarios:

1. **The attacker knows the packet size, timestamp, and flow ID** - This information helps identify the application or website in use.

2. **The attacker knows only the packet size and timestamp** - This scenario examines whether the attacker can still identify the website or application even if the traffic is encrypted, and how to mitigate such an attack.

## Project Structure

The project is divided into two main parts:

### Part A: Visual Data Analysis

In this phase, the collected data is presented using visual graphs. These graphs enable:

- Identifying trends and differences between different data groups.
- Revealing patterns and deriving meaningful insights.

### Part B: Attack Simulation and Machine Learning

In this phase, we simulate an attacker monitoring the user's network traffic. We use the **KNN** machine learning algorithm to identify the application the user is accessing.

Process steps:

1. **Data Processing** - Processing the collected data to extract insights and prepare it for model training.
2. **Model Training and Prediction** - Training the model using a large dataset and then predicting which application the user is accessing based on captured network traffic.

## System Requirements

The code is written in Python, making it compatible with both **Windows** and **Ubuntu** operating systems.

- **Python 3.12**

### Required Libraries:

- `pandas` - For data processing and CSV file handling.
- `scapy` - For reading and analyzing PCAP files.
- `matplotlib` - For generating visual graphs.
- `numpy` - For time calculations, data processing, and distance computations.
- `hashlib` - For creating unique connection identifiers.
- `collections (Counter)` - For counting occurrences in data.
- `csv` - For reading and writing CSV files (built-in in Python).
- `os` - For managing files and directories (built-in in Python).

## Execution Instructions
Running the Codes in the Project
All the codes are located inside the finalprog directory. This directory contains:

Graph codes (9 codes)
Five CSV files extracted from Wireshark recordings
An attacker folder, which includes 4 codes related to the attacker (Part 1, Part 2) and dataset creation
The Wireshark recordings are available in a shared Google Drive link.

Generating CSV Files from Wireshark
The CSV files were generated from Wireshark recordings. In our recorded sessions, we decrypted encrypted traffic using an environment variable that stores the encryption keys in ssl.log. This allowed Wireshark to interpret the encrypted packets correctly. (use from https://youtu.be/5qecyZHL-GU)


To extract the data from Wireshark and convert it to CSV:

Open the .pcapng file in Wireshark.
Go to "File" → "Export Packet Dissections" → "As CSV".
Select the desired fields such as No., Time, Source, Destination, Protocol, Length, Info.
Save the file in CSV format.
These CSV files were then used for analysis and visualization in the project.

Running Each Code
Graph Codes (9 codes)
Protocol Distribution (count_protocol.py)
To generate this graph, you need to provide a single CSV file at a time. For example, to see the protocol distribution in zoom.csv, run the code with that file.

TCP Flags (tcpF.py)
Similar to the protocol distribution graph, this code requires a single CSV file at a time. For example, use zoom.csv to see its TCP flag distribution.

Number of New Connections (newcon.py)
This graph displays the distribution of new connections across all datasets. To run it, you must provide all CSV files together.

Number of Retransmitted Packets (ressend.py)
This graph shows the distribution of retransmitted packets across all datasets. To run it, provide all CSV files together.

RTT Calculation (rtt.py)
To generate this graph, you need to provide a single CSV file at a time. For example, use zoom.csv to analyze its RTT distribution.

Average Time Between Two Packets (time.py)
This graph displays the distribution of the average time between two packets across all datasets. To run it, provide all CSV files together.

Flow Size (sizeflow.py)
This graph shows the distribution of flow sizes across all datasets. To run it, provide all CSV files together.

Average Packet Size (sizep.py)
This graph displays the distribution of the average packet size across all datasets. To run it, provide all CSV files together.

Flow Volume (volumep.py)
This graph represents the flow volume across all datasets. To run it, provide all CSV files together.

attacker Directory
This directory contains four codes, two for each part:

Part4A / Part4B – Training CSV Creation

These codes generate the training CSV files.
To run them, you need to either download the Wireshark recordings from the shared Drive or create new recordings.
You must update the code with the correct directory path where the recordings are stored.
Part4t1 / Part4t2 – Testing Execution

Additionally, we have included the two CSV files used for our predictions and the dataset we worked on.  
If you use these files, there is no need to run **part4A** and **part4B**.  

- CSV file for the first part: **train_flowid**  
- CSV file for the second part: **train2_table**  

These codes run the test phase. There are two execution modes:
Batch Mode (100 Samples) – Ensure the code points to the directory containing all the test recordings.
Single Prediction Mode – Update the code with the path of the specific recording you want to analyze.

Important:
All recordings must be in PCAPNG format.

