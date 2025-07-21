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
The first 10 results will appear in the terminal box, but to see the full results, check the ``comparison_output.txt`` file.

# Link to Original Kaggle Dataset
https://www.kaggle.com/code/selcukwashere/turkish-second-hand-automobile-market-analysis/

