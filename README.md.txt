# Worker Payment System

## Overview
This project contains Python and R scripts that generate a list of 400 workers dynamically, assign employee levels based on salary and gender, and print payment slips.

## Files Included
- `workerPayment.py` - Python script to generate workers and payment slips.
- `worker_payment.R` - R script equivalent to the Python version.
- `README.md` - Instructions on running the scripts.

## How to Run the Python Script
### Prerequisites
- Install **Python 3.7+**.

### Steps to Run
1. Open a terminal or command prompt.
2. Navigate to the directory containing `workerPayment.py`.
3. Run the script using:
   ```bash
   python workerPayment.py
   ```
4. The script will generate and print payment slips.

---

## How to Run the R Script
### Prerequisites
- Install **R 4.0+**.

### Steps to Run
1. Open R or RStudio.
2. Set the working directory to the script's location.
3. Run the script using:
   ```r
   source("worker_payment.R")
   ```
4. The script will generate and print payment slips.


## Error Handling
- The scripts handle missing data and file-writing errors.
- If any issues arise, an appropriate message is displayed in the console.

## Notes
- Both scripts dynamically generate worker details and assign employee levels based on salary and gender.
- The output is displayed directly in the console.

## Author
Yetunde Salami

## License
This project is for educational purposes only.

