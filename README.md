#  AI Greenhouse Automation

An AI-based Smart Greenhouse Robot project developed using Python. This project analyzes greenhouse data, monitors soil moisture, and simulates intelligent robots that help automate plant watering.

## Project Overview

The main goal of this project is to make plant watering smarter and more efficient.

The system uses greenhouse sensor data to identify plants that need water and simulates intelligent agents to perform watering tasks.

## Project Objectives

- Analyze greenhouse data using Pandas and NumPy.
- Handle missing values in the dataset.
- Visualize plant and soil moisture data.
- Calculate water requirements for plants.
- Simulate a watering robot.
- Compare Simple Reflex and Model-Based Agents.

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
AI-Greenhouse-Automation/
│
├── Q1.py
├── Q2.py
├── greenhouse.csv
├── greenhouse_clean.csv
└── README.md
```

##  Project Tasks

### Q1: Data Analysis and Visualization

- Load and explore greenhouse dataset.
- Identify and handle missing values.
- Use Pandas for data manipulation.
- Use NumPy for numerical operations.
- Generate graphs and visualizations.
- Save cleaned dataset.

### Q2: AI Robot Simulation

- Calculate plant water requirements.
- Simulate water tank management.
- Create Plant and WateringRobot classes.
- Implement a Simple Reflex Agent.
- Implement a Model-Based Agent.
- Calculate robot performance scores.

##  How to Run

### 1. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 2. Run Q1

```bash
python Q1.py
```

### 3. Run Q2

```bash
python Q2.py
```

**Note:** Keep `greenhouse.csv` in the same folder as `Q1.py`. Run Q1 first because it generates `greenhouse_clean.csv`, which is used by Q2.

##  AI Concepts

- Intelligent Agents
- Simple Reflex Agent
- Model-Based Agent
- Environment Perception
- Decision Making
- State and Memory

##  Author

Developed as an Artificial Intelligence Lab Mid-Term Project.

**Language:** Python

---

⭐ If you find this project useful, feel free to explore the code!
