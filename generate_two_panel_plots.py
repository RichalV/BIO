"""
Generate 2-panel Figures exactly matching Page 34 of BMSCE Reference PDF:
- Figure 1: Baseline Model Predictions (Time-series top, Scatter plot bottom)
- Figure 2: GWO-Optimized Model Predictions (Time-series top, Scatter plot bottom)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_preds = pd.read_csv('results/test_predictions.csv')
sample_slice = df_preds.iloc[:200]
time_steps = range(len(sample_slice))

# -------------------------------------------------------------------------
# FIGURE 1: Baseline Model Predictions (Before Optimization)
# -------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), dpi=300)

# Top: Time Series
ax1.plot(time_steps, sample_slice['ACTUAL_AC_POWER'], label='Actual', color='#1f77b4', linewidth=1.5)
ax1.plot(time_steps, sample_slice['BASELINE_PREDICTED'], label='Predicted', color='#d62728', linestyle='--', linewidth=1.4)
ax1.set_title('Baseline Model Predictions (Before Optimization)', fontsize=12, fontweight='bold', pad=10)
ax1.set_xlabel('Time Steps', fontsize=10)
ax1.set_ylabel('Power (kW)', fontsize=10)
ax1.legend(loc='upper right', frameon=True)
ax1.grid(True, linestyle=':', alpha=0.6)

# Bottom: Scatter Plot
max_val = max(df_preds['ACTUAL_AC_POWER'].max(), df_preds['BASELINE_PREDICTED'].max())
ax2.scatter(df_preds['ACTUAL_AC_POWER'], df_preds['BASELINE_PREDICTED'], color='#e377c2', alpha=0.5, s=15, edgecolors='none')
ax2.plot([0, max_val], [0, max_val], color='#d62728', linestyle='--', linewidth=1.5, label='Perfect Prediction')
ax2.set_title('Scatter Plot: Predicted vs Actual', fontsize=12, fontweight='bold', pad=10)
ax2.set_xlabel('Actual Values (kW)', fontsize=10)
ax2.set_ylabel('Predicted Values (kW)', fontsize=10)
ax2.legend(loc='upper left', frameon=True)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('plots/figure1_baseline_performance.png', bbox_inches='tight')
plt.close()
print("Saved plots/figure1_baseline_performance.png successfully!")

# -------------------------------------------------------------------------
# FIGURE 2: GWO-Optimized Model Predictions (After Optimization)
# -------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), dpi=300)

# Top: Time Series
ax1.plot(time_steps, sample_slice['ACTUAL_AC_POWER'], label='Actual', color='#1f77b4', linewidth=1.5)
ax1.plot(time_steps, sample_slice['GWO_PREDICTED'], label='Predicted', color='#2ca02c', linestyle='-', linewidth=1.6)
ax1.set_title('Optimized Model - Test Set Predictions - Time Series', fontsize=12, fontweight='bold', pad=10)
ax1.set_xlabel('Time Steps', fontsize=10)
ax1.set_ylabel('Power (kW)', fontsize=10)
ax1.legend(loc='upper right', frameon=True)
ax1.grid(True, linestyle=':', alpha=0.6)

# Bottom: Scatter Plot
ax2.scatter(df_preds['ACTUAL_AC_POWER'], df_preds['GWO_PREDICTED'], color='#9467bd', alpha=0.5, s=15, edgecolors='none')
ax2.plot([0, max_val], [0, max_val], color='#d62728', linestyle='--', linewidth=1.5, label='Perfect Prediction')
ax2.set_title('Optimized Model - Test Set Predictions - Scatter Plot', fontsize=12, fontweight='bold', pad=10)
ax2.set_xlabel('Actual Price / Power (kW)', fontsize=10)
ax2.set_ylabel('Predicted Values (kW)', fontsize=10)
ax2.legend(loc='upper left', frameon=True)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('plots/figure2_gwo_performance.png', bbox_inches='tight')
plt.close()
print("Saved plots/figure2_gwo_performance.png successfully!")

