# Hydro Analyzer

  &emsp;Hydro Analyser is a first ever Open-source tool designed for hydrogeologists, engineers, and other professionals in the water resources industry to accurately analyze and optimize groundwater pumping tests. This repository contains code to perform a single well pumping test, which is used to find the transmissivity and storativity of a well.This tool allows you to input data and calculate the transmissivity and storativity of the well. The code is written in PySide6 and can be run from the command line or in any python interpreter 

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
 

 
# Output 

 * `transmissivity`: The transmissivity of the well in square metre per day.
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
 
 <img width="1440" alt="Pumping test" src="https://user-images.githubusercontent.com/105580560/224953529-e79feef8-3da1-4ef1-95bf-ea2344e4d421.png">



 ## Pumping Data Tab  
 
 &emsp;Step 1: Fill in discharge details.  
 &emsp;Step 2: Enter field data in the table. Press Enter after entering last data.  
 &emsp;Step 3: Click "Plot Data" after entering drawdown data.  
 &emsp;Step 4: The graph will be plotted.  
 
<img width="1440" alt="pumping_data" src="https://user-images.githubusercontent.com/105580560/224953658-93d690a2-f3dd-48bb-a45e-492ad02b30b2.png">


 ## Analysis Tab.  
 
 &emsp;Step 1: Enter analyzer details.  
 &emsp;Step 2: Click "Fit" after entering required data.  
 &emsp;Step 3: The analysis curve for Theis method will be displayed.  
 &emsp;Step 4: Click "Generate Report" to save the report as a PDF.  
 
 <img width="1440" alt="Analysis" src="https://user-images.githubusercontent.com/105580560/224953801-0570bea5-eb41-40db-a1bb-89ccd01f9859.png">

# NOTE  
&emsp;This project is still in development and some features may not be fully functional.

