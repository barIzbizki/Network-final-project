# README - Data Analysis Project

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

To generate the graphs, the recordings must first be converted to a CSV file using **Wireshark**. This can be done by following these steps:
1. Open the recording in **Wireshark**.
2. Go to **File → Export Packet Dissections → As CSV**.
3. Save the file in the project directory.

Once the CSV file is ready, execute the following scripts to run the project:


### Part 4: Execution Instructions

To run the project, execute the following scripts:

```sh
python part4A.py
python part4B.py
python part4t1.py
python part4t2.py
```

## Data Files

- **For graph generation**, we used **one recording per application**.
- **For the attacker's prediction phase**, we recorded **approximately 15 sessions per application** to ensure a sufficient dataset for accurate predictions.

