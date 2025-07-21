# Turkish Auto Price Predictor

This program reads the Kaggle dataset of secondhand car prices in Turkey and presents 2,000 price predictions with about an 87%+ accuracy.

```text
main.py                                    # Main file
turkish_2ndhand_automobile_processed.csv   # data CSV file
README.md                                  # README
```
# How to Run
In ordinary to run this program, the user must download the original CSV file and the ```main.py``` file. The user might not have the libraries installed on your computer / Google Colab, so to install them run these commands first:

```bash
pip install sklearn
```
```bash
pip install numpy
```
```bash
pip install pandas
```
Move the CSV file to Google Colab / your computer folder. Then, change _line 8_ in ```main.py ``` to match where your CSV file is located.
The user should also adjust line 110, ```output_file = "/content/comparison_output.txt"```, to adjust the location of where the results file is saved.

Then, run ```python main.py```

# Results
The first line of results will be the Average Margin of Error
The next line will confirm that the comparison data of the price predictions has been saved to ``comparison_output.txt``.
The following graph will show a preview of the first 10 comparisons, showing the car brand, model, year, KM, location, actual price (translated from Lira to USD), predicted price (translated from Lira to USD), and MoE.

<img width="1054" height="263" alt="Screenshot 2025-07-21 at 3 06 42 PM" src="https://github.com/user-attachments/assets/9d619e22-51fa-4ff5-aa91-7c42f1df2f6b" />


# Link to Original Kaggle Dataset
https://www.kaggle.com/code/selcukwashere/turkish-second-hand-automobile-market-analysis/

