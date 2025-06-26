import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import yfinance as yf

dataset_path = "/content/turkish_2ndhand_automobile_processed.csv"
df = pd.read_csv(dataset_path)

cat_imputer1 = SimpleImputer(strategy='most_frequent')
df['marka'] = cat_imputer1.fit_transform(df[['marka']]).ravel()

cat_imputer2 = SimpleImputer(strategy='most_frequent')
df['seri'] = cat_imputer2.fit_transform(df[['seri']]).ravel()

cat_imputer3 = SimpleImputer(strategy='most_frequent')
df['model'] = cat_imputer3.fit_transform(df[['model']]).ravel()

cat_imputer4 = SimpleImputer(strategy='most_frequent')
df['il_ilce'] = cat_imputer4.fit_transform(df[['il_ilce']]).ravel()

df['km'] = pd.to_numeric(df['km'], errors='coerce')
num_imputer = SimpleImputer(strategy='median')
df['km'] = num_imputer.fit_transform(df[['km']])


yil_bottom = df['yil'].quantile(0.10)

Q1fiyat = df['fiyat'].quantile(0.25)
Q3fiyat = df['fiyat'].quantile(0.75)
IQRfiyat = Q3fiyat - Q1fiyat

Q1km = df['km'].quantile(0.25)
Q3km = df['km'].quantile(0.75)
IQRkm = Q3km - Q1km

lower_bound = Q1fiyat - 1.5 * IQRfiyat
upper_bound = Q3fiyat + 1.5 * IQRfiyat


df = df[ (df['fiyat'] >= lower_bound) & (df['fiyat'] <= upper_bound) & (df['km'] >= Q1km) & (df['km'] <= Q3km) & (df['yil'] >= yil_bottom)]


selected_features = ['marka', 'seri', 'model', 'yil', 'km', 'il_ilce']


df_sampled = df.sample(frac=1, random_state=100)


price_factors = df_sampled[selected_features]


price_factors = pd.get_dummies(price_factors, columns=selected_features, drop_first=True).astype(float)


price_target = df_sampled['fiyat']


price_factors_train, price_factors_test, price_target_train, price_target_test = train_test_split(price_factors, price_target, test_size=.67)


model = LinearRegression()

model.fit(price_factors_train, price_target_train)

price_target_pred = model.predict(price_factors_test)
price_target_pred = np.maximum(price_target_pred, 0)


original_features = df[['marka', 'model', 'yil', 'km', 'il_ilce']]


original_features_test = original_features.loc[price_factors_test.index].reset_index(drop=True)


comparison_df = pd.DataFrame({
  "Brand": original_features_test["marka"],
  "Model": original_features_test["model"],
  "Year": original_features_test["yil"],
  "KM": original_features_test["km"].round().astype(int),
  "Location": original_features_test['il_ilce'],
  "Actual Price (TRY)": price_target_test.values.round(2).astype(float),
  "Predicted Price (TRY)": price_target_pred.round(2).astype(float)
})

lira2USD = yf.download("USDTRY=X", period="1d", interval="1m")["Close"].iloc[-1].round().astype(int)


def convertLira2USD(liras):
  price = liras / lira2USD
  return price


comparison_df["Actual Price ($)"] = (comparison_df["Actual Price (TRY)"].apply(lambda x: convertLira2USD(x))).round(2).astype(float)
comparison_df["Predicted Price ($)"] = (comparison_df["Predicted Price (TRY)"].apply(lambda x: convertLira2USD(x))).round(2).astype(float)

comparison_df = comparison_df.drop(columns=["Actual Price (TRY)", "Predicted Price (TRY)"])

comparison_df["  MoE (%)"] = ((abs(price_target_pred - price_target_test.values) / price_target_test.values) * 100).round(1).astype(float)


comparison_df["  MoE (%)"] = comparison_df["  MoE (%)"].apply(lambda x: f"{x}%")

average_moe = comparison_df["  MoE (%)"].str.rstrip('%').astype(float).mean()

print(f"\nAverage Margin of Error: {average_moe:.2f}%" + '\n')

output_file = "/content/comparison_output.txt"

with open(output_file, 'w') as file:
  file.write(comparison_df.to_string(index=False))

print(f"Full comparison data has been saved to {output_file}")


print('\n'+ "First 10 comparisons preview: " + '\n' + comparison_df.head(10).to_string(index=False))
