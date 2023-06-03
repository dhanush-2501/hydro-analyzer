[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Development Status](https://img.shields.io/badge/status-development-blue) [![Auto-format with Black](https://github.com/HydroAnalyser/hydro-analyzer/actions/workflows/black.yml/badge.svg)](https://github.com/HydroAnalyser/hydro-analyzer/actions/workflows/black.yml)

# Hydro Analyzer

  &emsp;Hydro Analyser is the first-ever open-source tool designed for hydrogeologists, engineers, and other professionals in the water resources industry to accurately analyze and optimize groundwater pumping tests . This repository contains code that performs a single well pumping test, used to determine the transmissivity and storativity of a well 🔍. This tool enables you to input data and calculate the well's transmissivity and storativity 📊. The code is written in PySide6 and can be executed from the command line or any Python interpreter.  
  

# 🚀Getting Started

 To use the hydro analyzer pumping test code, follow these steps:
 * Clone this repository to your local machine 🖥️. 
 * Navigate to the cloned directory 📂.
 * Install the required packages in the project directory by running the code below.
 ```
 pip install . -e
 ```
 
 * Run `run.py` file.
 ```
 python3 run.py
 ```
 
# Pumping Test Tutorial  
 This tutorial provides step-by-step instructions for entering data and analyzing results using the Hydro-Analyzer. 
 
 
 ## Pumping Test Tab 
 
1. Enter project information in the first box📝.
2. Enter the pumping test details.
3. Select units of measurement.
4. Enter aquifer thickness.
5. Enter well details in the table🗂️.
6. Click "submit"
 
<img width="1440" alt="pumping_test" src="https://user-images.githubusercontent.com/105580560/226807426-757bef2f-31d3-4b2a-a0f4-b052fef0f307.png">



 ## Pumping Data Tab  
 
1. Fill in discharge details.  
2. Enter field data in the table. Press Enter after entering last data.  
3. Click "Plot Data" after entering drawdown data.  
4. The graph will be plotted📈.  

<img width="1440" alt="pumping_data" src="https://user-images.githubusercontent.com/105580560/224953658-93d690a2-f3dd-48bb-a45e-492ad02b30b2.png">


 ## Analysis Tab.  
 
1. Enter analyzer details.  
2. Click "Fit" after entering required data.  
3. The analysis curve for Theis method will be displayed.  
4. Click "Generate Report"💾 to save the report as a PDF.  
 
 <img width="1440" alt="Analysis" src="https://user-images.githubusercontent.com/105580560/224953801-0570bea5-eb41-40db-a1bb-89ccd01f9859.png">
 
https://user-images.githubusercontent.com/79148926/227170614-2729ff08-2b02-4003-9e6e-325f8a312bce.mp4
 
## How to Contribute🤝 
🙌 We welcome contributions from anyone who is interested in improving this project. Whether you want to submit a pull request with code changes or just help with documentation or issue triage, we appreciate your help in making this project better💻👩‍💻👨‍💻.

# Guidelines for Contributing  
If you would like to submit a pull request with code changes, please follow these steps:
1. 🍴Fork the repository to your own GitHub account.
2. Clone the repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes to the code according to code and documentation standards. Like files related to UI must be inside the UI folder, Widgets must be in Widgets folder.            
5. Test your changes thoroughly.
6. Commit your changes with a clear and concise commit message💬.
7. Push your changes to your forked repository.
8. Submit a pull request to the forked repository, including a clear and concise description of the changes you made.  

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

# NOTE📌  
This project is still in development and some features may not be fully functional.
