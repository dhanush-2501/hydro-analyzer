[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Development Status](https://img.shields.io/badge/status-development-blue)

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
 python3 run.py
 ```
 
# Pumping Test Tutorial  
 &emsp;This tutorial provides step-by-step instructions for entering data and analyzing results using the Hydro-Analyzer.  
 
 
 ## Pumping Test Tab 
 
 &emsp;Step 1: Enter project information in the first box.  
 &emsp;Step 2: Enter the pumping test details.  
 &emsp;Step 3: Select units of measurement.  
 &emsp;Step 4: Enter aquifer thickness.  
 &emsp;Step 5: Enter well details in the table.  
 &emsp;Step 6: Click "submit".  
 
<img width="1440" alt="pumping_test" src="https://user-images.githubusercontent.com/105580560/225810486-3fa795a2-ba86-470a-ac39-203f642333db.png">


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
 
 


https://user-images.githubusercontent.com/79148926/226101677-c95751d6-564e-4f5e-a80d-2834e689368b.mov


 
# How to Contribute 
&emsp;We welcome contributions from anyone who is interested in improving this project. Whether you want to submit a pull request with code changes, we appreciate your help in making this project better.

# Guidelines for Contributing  
&emsp;If you would like to submit a pull request with code changes, please follow these steps:
1. Fork the repository to your own GitHub account.
2. Clone the repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes to the code according to code and documentation standards. Like files related to UI must be inside the UI folder, Widgets must be in Widgets folder.

```
Hydro analyzer  
├── docs    
    ├── README.md 
├── HyAn  
    ├── img    
        ├── analysis_curve  
    ├── report    
        ├── report            # report format must be modified and upadate here.  
    ├── solution              # folder for modifying and adding solutions
        ├── pytheis  
    ├── ui 
        ├── ...               # ui files must be placed in this ui folder             
    ├── widget           
        ├── ...               # widget must be placed in this widget folder            
                   
```
          
5. Test your changes thoroughly.
6. Commit your changes with a clear and concise commit message.
7. Push your changes to your forked repository.
8. Submit a pull request to the forked repository, including a clear and concise description of the changes you made.


# NOTE  
&emsp;This project is still in development and some features may not be fully functional.
