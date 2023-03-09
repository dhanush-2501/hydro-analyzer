# Hydro Analyzer

  Hydro Analyser is  is a powerful tool designed for hydrogeologists, engineers, and other professionals in the water resources industry to accurately analyze and optimize groundwater pumping tests. This repository contains code to perform a hydro analyzer pumping test, which is used to find the transmissivity and storativity of a well.This code allows you to input data and calculate the transmissivity and storativity of the well. The code is written in PySide6 and can be run from the command line or in any python interpreter 

# Getting Started

 * To use the hydro analyzer pumping test code, follow these steps:
 * Clone this repository to your local machine. 
 * Navigate to the clone directory.
 * Install the following packages in the project directory by running the code below.
 ```
 pip install -e .
 ```
 
 * Run `main.py` file.
 ```
 python main.py
 ```
 
# Input Data Format

 * `time`: The time since pumping began.
 * `pumping_well`: The water level in the pumped well.
 * `well_dimension`s: Radius, Width and other required dimensions of the well.
 * `discharge`: The discharge data.
 * `drawdown`: The drawdown data.
 
# Output 

 * `transmissivity`: The transmissivity of the well in square feet per day.
 * `storativity`: The storativity of the well, a dimensionless value.
 
 
