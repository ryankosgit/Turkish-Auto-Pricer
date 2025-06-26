# Turkish Auto Price Predictor

This program reads the Kaggle dataset of secondhand car prices in Turkey and presents 2,000 price predictions with about an 87%+ accuracy.

```text
main.py                                    # Main file
turkish_2ndhand_automobile_processed.csv   # data CSV file
README.md                                  # README
```
# How to Run
In ordinary to run this program, the user must download the original CSV file with the data and the code file. The user might not have the libraries installed, so to install them run these commands first:

```bash
!pip install sklearn
```
```bash
!pip install numpy
```
```bash
!pip install pandas
```
Move the CSV file to Google Colab / your computer folder. Then, adjust _line 8_ in ```main.py ``` to match where your CSV file is located.

Once that is completed, simply run the program and watch the price predictions print in the terminal.

# Link to Original Kaggle Dataset
https://www.kaggle.com/code/selcukwashere/turkish-second-hand-automobile-market-analysis/

