# Hydro Analyzer

  &emsp;Hydro Analyser is a powerful tool designed for hydrogeologists, engineers, and other professionals in the water resources industry to accurately analyze and optimize groundwater pumping tests. This repository contains code to perform a hydro analyzer pumping test, which is used to find the transmissivity and storativity of a well.This code allows you to input data and calculate the transmissivity and storativity of the well. The code is written in PySide6 and can be run from the command line or in any python interpreter 

# Getting Started

 * To use the hydro analyzer pumping test code, follow these steps:
 * Clone this repository to your local machine. 
 * Navigate to the cloned directory.
 * Install the required packages in the project directory by running the code below.
 ```
 pip install -e .
 ```
 
 * Run `run.py` file.
 ```
 python run.py
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
 
# Pumping Test Tutorial  
 &emsp;This tutorial provides step-by-step instructions for entering data and analyzing results using the Hydro-Analyzer.  
 
 
 ## Pumping Test Tab 
 
 &emsp;Step 1: Enter project information in the first box.  
 &emsp;Step 2: Enter the pumping test details.  
 &emsp;Step 3: Select units of measurement.  
 &emsp;Step 4: Enter aquifer thickness.  
 &emsp;Step 5: Enter well details in the table.  
 &emsp;Step 6: Click "submit".  
 
 <img width="1440" alt="well data" src="https://user-images.githubusercontent.com/105580560/224926814-95cc2c46-9c51-43a2-aecc-f2d7aa4fd19e.png">


 ## Pumping Data Tab  
 
 &emsp;Step 1: Fill in discharge details.  
 &emsp;Step 2: Enter field data in the table.  
 &emsp;Step 3: Click "Plot Data" after entering drawdown data. Click Enter after entering last data.  
 &emsp;Step 4: The graph will be plotted.  
 
 <img width="1440" alt="Plotted data" src="https://user-images.githubusercontent.com/105580560/224926435-b3a12b6d-64d5-43d2-b00a-66cb1aec1344.png">


 ## Analysis Tab.  
 
 &emsp;Step 1: Enter analyzer details.  
 &emsp;Step 2: Click "Fit" after entering required data.  
 &emsp;Step 3: The analysis curve for Theis method will be displayed.  
 &emsp;Step 4: Click "Generate Report" to download the report as a PDF.  
 
 <img width="1440" alt="Fitted data" src="https://user-images.githubusercontent.com/105580560/224922541-97d8ce6b-6655-4f22-af48-4eaad7d63128.png">

