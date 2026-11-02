"""
Phase 1: Dataset Preprocessing and Feature Engineering
Course: Bio-Inspired Algorithms (23DS7BSBIO)
Project: Solar PV Power Generation Forecasting using CatBoost & Grey Wolf Optimizer (GWO)
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(gen_path='Plant_1_Generation_Data.csv',
                             weather_path='Plant_1_Weather_Sensor_Data.csv'):
    print("[1/5] Loading datasets...")
    df_gen = pd.read_csv(gen_path)
    df_weather = pd.read_csv(weather_path)
    
    # 1. Parse timestamps to standard datetime format
    df_gen['DATE_TIME'] = pd.to_datetime(df_gen['DATE_TIME'], format='%d-%m-%Y %H:%M')
    df_weather['DATE_TIME'] = pd.to_datetime(df_weather['DATE_TIME'], format='%Y-%m-%d %H:%M:%S')
    
    # 2. Aggregate generation at plant level (sum across inverters per 15-minute interval)
    plant_gen = df_gen.groupby('DATE_TIME').agg({
        'DC_POWER': 'sum',
        'AC_POWER': 'sum',
        'DAILY_YIELD': 'sum'
    }).reset_index()
    
    # 3. Merge plant generation with weather station sensors
    weather_cols = ['DATE_TIME', 'AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']
    df = pd.merge(plant_gen, df_weather[weather_cols], on='DATE_TIME', how='inner')
    df = df.sort_values('DATE_TIME').reset_index(drop=True)
    
    # Check and handle missing values
    null_counts = df.isnull().sum().sum()
    if null_counts > 0:
        print(f"Handling {null_counts} missing values using forward/backward fill...")
        df = df.bfill().ffill()
    else:
        print("Dataset clean: 0 missing values detected.")
        
    # 4. Feature Engineering (Domain-specific solar physics & cyclical time)
    df['HOUR'] = df['DATE_TIME'].dt.hour
    df['MINUTE'] = df['DATE_TIME'].dt.minute
    df['DAY_OF_WEEK'] = df['DATE_TIME'].dt.dayofweek
    
    # Thermal gradient between module and ambient air
    df['TEMP_DIFF'] = df['MODULE_TEMPERATURE'] - df['AMBIENT_TEMPERATURE']
    
    # Cyclical solar diurnal angle encoding
    time_float = df['HOUR'] + df['MINUTE'] / 60.0
    df['HOUR_SIN'] = np.sin(2 * np.pi * time_float / 24.0)
    df['HOUR_COS'] = np.cos(2 * np.pi * time_float / 24.0)
    
    # Interaction: Effective Solar Irradiance Thermal Index
    df['IRRAD_TEMP_INTERACTION'] = df['IRRADIATION'] * df['MODULE_TEMPERATURE']
    
    # 5. Define Feature Matrix X and Target y
    feature_cols = [
        'AMBIENT_TEMPERATURE',
        'MODULE_TEMPERATURE',
        'IRRADIATION',
        'TEMP_DIFF',
        'HOUR',
        'MINUTE',
        'HOUR_SIN',
        'HOUR_COS',
        'IRRAD_TEMP_INTERACTION'
    ]
    target_col = 'AC_POWER'
    
    # 6. Chronological Train / Validation / Test split (No future data leakage)
    # 70% Train, 15% Validation (for GWO Fitness), 15% Test (Final Unseen Evaluation)
    n = len(df)
    train_end = int(0.70 * n)
    val_end = int(0.85 * n)
    
    train_df = df.iloc[:train_end].copy()
    val_df = df.iloc[train_end:val_end].copy()
    test_df = df.iloc[val_end:].copy()
    
    X_train, y_train = train_df[feature_cols].copy(), train_df[target_col].copy()
    X_val, y_val = val_df[feature_cols].copy(), val_df[target_col].copy()
    X_test, y_test = test_df[feature_cols].copy(), test_df[target_col].copy()
    
    # 7. Standard Scaler Normalization (Rubric Phase 1 requirement)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
    
    # Wrap into DataFrames for clean column preservation
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=feature_cols, index=X_train.index)
    X_val_scaled = pd.DataFrame(X_val_scaled, columns=feature_cols, index=X_val.index)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=feature_cols, index=X_test.index)
    
    print(f"Data Splitting Complete:")
    print(f" - Total Samples: {n}")
    print(f" - Train Set:      {len(X_train)} samples ({train_df['DATE_TIME'].min().date()} to {train_df['DATE_TIME'].max().date()})")
    print(f" - Validation Set: {len(X_val)} samples ({val_df['DATE_TIME'].min().date()} to {val_df['DATE_TIME'].max().date()})")
    print(f" - Test Set:       {len(X_test)} samples ({test_df['DATE_TIME'].min().date()} to {test_df['DATE_TIME'].max().date()})")
    print(f" - Feature Dimensions: {len(feature_cols)} features")
    
    return {
        'df': df,
        'feature_cols': feature_cols,
        'target_col': target_col,
        'train_df': train_df,
        'val_df': val_df,
        'test_df': test_df,
        'X_train': X_train,
        'y_train': y_train,
        'X_val': X_val,
        'y_val': y_val,
        'X_test': X_test,
        'y_test': y_test,
        'X_train_scaled': X_train_scaled,
        'X_val_scaled': X_val_scaled,
        'X_test_scaled': X_test_scaled,
        'scaler': scaler
    }

if __name__ == '__main__':
    data_dict = load_and_preprocess_data()
    print("Preprocessing verification successful!")

