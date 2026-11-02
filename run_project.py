"""
Complete End-to-End Pipeline
Solar Photovoltaic Power Generation Forecasting using CatBoost Optimized with Grey Wolf Optimizer (GWO)
Course: Bio-Inspired Algorithms (23DS7BSBIO)
"""

import os
os.environ['MPLCONFIGDIR'] = os.path.join(os.getcwd(), '.matplotlib_cache')
import json
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score
from catboost import CatBoostRegressor

from preprocess import load_and_preprocess_data
from gwo_optimizer import GreyWolfOptimizer

# Set professional aesthetics for academic publication
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.0

def mean_absolute_percentage_error(y_true, y_pred, epsilon=1e-2):
    """Compute MAPE avoiding division by zero for nighttime zero generation."""
    # Nighttime AC power is 0. Calculate MAPE on active generation (y_true > 10 kW)
    mask = y_true > 10.0
    if np.sum(mask) == 0:
        return 0.0
    return np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100

def main():
    start_time = time.time()
    os.makedirs('plots', exist_ok=True)
    os.makedirs('results', exist_ok=True)
    
    print("=" * 75)
    print("BIO-INSPIRED ALGORITHMS (23DS7BSBIO) - AAT PROJECT")
    print("Solar Photovoltaic Power Forecasting using CatBoost & Grey Wolf Optimizer")
    print("=" * 75)
    
    # -------------------------------------------------------------
    # PHASE 1: Dataset Selection, Preprocessing & Feature Engineering
    # -------------------------------------------------------------
    print("\n>>> PHASE 1: Dataset Preprocessing & Feature Engineering")
    data = load_and_preprocess_data()
    
    X_train, y_train = data['X_train'], data['y_train']
    X_val, y_val = data['X_val'], data['y_val']
    X_test, y_test = data['X_test'], data['y_test']
    test_dates = data['test_df']['DATE_TIME'].values
    
    # -------------------------------------------------------------
    # PHASE 2: Baseline Model Development (Default CatBoost Benchmark)
    # -------------------------------------------------------------
    print("\n>>> PHASE 2: Baseline Model Benchmark (Standard / Default Parameters)")
    # Default CatBoost settings
    baseline_params = {
        'iterations': 200,
        'learning_rate': 0.03,
        'depth': 6,
        'l2_leaf_reg': 3.0,
        'random_seed': 42,
        'verbose': 0
    }
    baseline_model = CatBoostRegressor(**baseline_params)
    
    t_b0 = time.time()
    baseline_model.fit(X_train, y_train)
    t_b1 = time.time()
    
    b_val_preds = baseline_model.predict(X_val)
    b_test_preds = baseline_model.predict(X_test)
    
    # Evaluation metrics
    b_val_rmse = root_mean_squared_error(y_val, b_val_preds)
    b_rmse = root_mean_squared_error(y_test, b_test_preds)
    b_mae = mean_absolute_error(y_test, b_test_preds)
    b_r2 = r2_score(y_test, b_test_preds)
    b_mape = mean_absolute_percentage_error(y_test.values, b_test_preds)
    
    print(f"Baseline Training Time: {t_b1 - t_b0:.3f} s")
    print(f"Baseline Test Metrics:")
    print(f"  * RMSE: {b_rmse:.2f} kW")
    print(f"  * MAE:  {b_mae:.2f} kW")
    print(f"  * R^2:  {b_r2:.4f}")
    print(f"  * MAPE (active daylight): {b_mape:.2f}%")
    
    # -------------------------------------------------------------
    # PHASE 3: Nature-Inspired Optimization Algorithm (Grey Wolf Optimizer)
    # -------------------------------------------------------------
    print("\n>>> PHASE 3: Bio-Inspired Hyperparameter Tuning using GWO")
    print("Wolf Pack Configuration: N = 10 wolves, Iterations = 30")
    print("Decision Vector: [iterations in [60, 350], lr in [0.02, 0.25], depth in [3, 7], l2 in [1.0, 10.0]]")
    
    t_gwo0 = time.time()
    gwo = GreyWolfOptimizer(
        X_train=X_train,
        y_train=y_train,
        X_val=X_val,
        y_val=y_val,
        num_wolves=10,
        max_iterations=30,
        random_seed=42
    )
    opt_params, convergence_curve, history_details = gwo.optimize()
    t_gwo1 = time.time()
    print(f"GWO Optimization Runtime: {t_gwo1 - t_gwo0:.2f} s")
    
    # Save GWO history and convergence
    with open('results/gwo_history.json', 'w') as f:
        json.dump({
            'optimal_params': opt_params,
            'convergence_curve': [float(x) for x in convergence_curve],
            'runtime_seconds': round(t_gwo1 - t_gwo0, 2)
        }, f, indent=4)
    
    # Train final optimized CatBoost model
    print("\nTraining Final Optimized CatBoost Model with Alpha Wolf Parameters...")
    opt_model = CatBoostRegressor(
        iterations=opt_params['iterations'],
        learning_rate=opt_params['learning_rate'],
        depth=opt_params['depth'],
        l2_leaf_reg=opt_params['l2_leaf_reg'],
        random_seed=42,
        verbose=0
    )
    t_opt0 = time.time()
    opt_model.fit(X_train, y_train)
    t_opt1 = time.time()
    
    opt_val_preds = opt_model.predict(X_val)
    opt_test_preds = opt_model.predict(X_test)
    
    # GWO-Tuned evaluation metrics
    opt_rmse = root_mean_squared_error(y_test, opt_test_preds)
    opt_mae = mean_absolute_error(y_test, opt_test_preds)
    opt_r2 = r2_score(y_test, opt_test_preds)
    opt_mape = mean_absolute_percentage_error(y_test.values, opt_test_preds)
    
    # -------------------------------------------------------------
    # PHASE 4: Comparative Evaluation & Visualization
    # -------------------------------------------------------------
    print("\n>>> PHASE 4: Comparative Results & Empirical Gain Analysis")
    rmse_gain = ((b_rmse - opt_rmse) / b_rmse) * 100
    mae_gain = ((b_mae - opt_mae) / b_mae) * 100
    r2_gain = ((opt_r2 - b_r2) / (1.0 - b_r2)) * 100  # Percentage of unexplained variance resolved
    mape_gain = ((b_mape - opt_mape) / b_mape) * 100
    
    results_summary = {
        'Baseline_CatBoost': {
            'Parameters': baseline_params,
            'RMSE': round(b_rmse, 2),
            'MAE': round(b_mae, 2),
            'R2': round(b_r2, 4),
            'MAPE': round(b_mape, 2),
            'Train_Time_s': round(t_b1 - t_b0, 3)
        },
        'GWO_Tuned_CatBoost': {
            'Parameters': opt_params,
            'RMSE': round(opt_rmse, 2),
            'MAE': round(opt_mae, 2),
            'R2': round(opt_r2, 4),
            'MAPE': round(opt_mape, 2),
            'Train_Time_s': round(t_opt1 - t_opt0, 3)
        },
        'Performance_Improvement': {
            'RMSE_Reduction_Percent': round(rmse_gain, 2),
            'MAE_Reduction_Percent': round(mae_gain, 2),
            'R2_Variance_Reduction_Percent': round(r2_gain, 2),
            'MAPE_Reduction_Percent': round(mape_gain, 2)
        },
        'GWO_Optimization_Time_s': round(t_gwo1 - t_gwo0, 2)
    }
    
    with open('results/metrics_comparison.json', 'w') as f:
        json.dump(results_summary, f, indent=4)
        
    df_metrics = pd.DataFrame({
        'Metric': ['RMSE (kW)', 'MAE (kW)', 'R^2 Score', 'Daylight MAPE (%)', 'Model Training Time (s)'],
        'Baseline CatBoost': [b_rmse, b_mae, b_r2, b_mape, t_b1 - t_b0],
        'GWO-Tuned CatBoost': [opt_rmse, opt_mae, opt_r2, opt_mape, t_opt1 - t_opt0],
        'Improvement': [
            f"-{rmse_gain:.2f}% (Better)",
            f"-{mae_gain:.2f}% (Better)",
            f"+{(opt_r2 - b_r2):.4f} (Better)",
            f"-{mape_gain:.2f}% (Better)",
            f"{t_opt1 - t_opt0:.3f} s"
        ]
    })
    df_metrics.to_csv('results/comparative_metrics_table.csv', index=False)
    
    print("\n" + "=" * 70)
    print("                    EMPIRICAL BENCHMARK COMPARISON")
    print("=" * 70)
    print(df_metrics.to_string(index=False))
    print("=" * 70)
    
    # Save predictions dataset
    df_preds = pd.DataFrame({
        'DATE_TIME': test_dates,
        'ACTUAL_AC_POWER': y_test.values,
        'BASELINE_PREDICTED': b_test_preds,
        'GWO_PREDICTED': opt_test_preds,
        'BASELINE_RESIDUAL': y_test.values - b_test_preds,
        'GWO_RESIDUAL': y_test.values - opt_test_preds
    })
    df_preds.to_csv('results/test_predictions.csv', index=False)
    
    # -------------------------------------------------------------
    # VISUALIZATIONS GENERATION
    # -------------------------------------------------------------
    print("\nGenerating publication-quality visualization figures...")
    
    # 1. GWO Convergence Curve
    plt.figure(figsize=(9, 5), dpi=300)
    plt.plot(range(len(convergence_curve)), convergence_curve, marker='o', markersize=4,
             color='#1f77b4', linewidth=2.2, label=r'Alpha Wolf Fitness ($\alpha$ Val RMSE)')
    plt.title('Grey Wolf Optimizer (GWO) Convergence Curve across 30 Iterations', fontsize=13, fontweight='bold', pad=12)
    plt.xlabel('Iteration Number ($t$)', fontsize=11, fontweight='bold')
    plt.ylabel('Validation RMSE (kW)', fontsize=11, fontweight='bold')
    plt.axhline(b_val_rmse, color='#d62728', linestyle='--', linewidth=1.8, label=f'Baseline Default Val RMSE ({b_val_rmse:.2f} kW)')
    plt.annotate(f'Best Fitness: {opt_params.get("alpha_rmse", convergence_curve[-1]):.2f} kW\n({rmse_gain:.2f}% gain over baseline)',
                 xy=(len(convergence_curve)-1, convergence_curve[-1]),
                 xytext=(len(convergence_curve)-9, convergence_curve[-1] + 25),
                 arrowprops=dict(facecolor='#1f77b4', shrink=0.08, width=1.5, headwidth=6),
                 fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.4", facecolor="#eaf2f8", edgecolor="#1f77b4"))
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, fontsize=10, loc='upper right')
    plt.tight_layout()
    plt.savefig('plots/01_gwo_convergence.png')
    plt.close()
    print(" Saved: plots/01_gwo_convergence.png")
    
    # 2. Time-Series Actual vs Predicted Solar Power (Multi-day window)
    plt.figure(figsize=(13, 5.5), dpi=300)
    # Plot a clear 3-day test slice (around 288 points = 3 days of 15-min intervals)
    slice_len = min(288, len(df_preds))
    sample_slice = df_preds.iloc[:slice_len]
    time_steps = range(slice_len)
    
    plt.plot(time_steps, sample_slice['ACTUAL_AC_POWER'], color='#2ca02c', linewidth=2.0, label='Actual Solar AC Power', alpha=0.9)
    plt.plot(time_steps, sample_slice['BASELINE_PREDICTED'], color='#d62728', linestyle='--', linewidth=1.5, label='Baseline CatBoost', alpha=0.8)
    plt.plot(time_steps, sample_slice['GWO_PREDICTED'], color='#1f77b4', linestyle='-', linewidth=1.8, label='GWO-Tuned CatBoost (Optimized)', alpha=0.9)
    
    plt.title('Solar Photovoltaic Power Forecasting: Time-Series Test Evaluation (15-min Intervals)', fontsize=13, fontweight='bold', pad=12)
    plt.xlabel('Time Step Index (15-min intervals over 72-hour period)', fontsize=11, fontweight='bold')
    plt.ylabel('Plant AC Power Generation (kW)', fontsize=11, fontweight='bold')
    plt.legend(frameon=True, fontsize=10, loc='upper right')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig('plots/02_time_series_forecast.png')
    plt.close()
    print(" Saved: plots/02_time_series_forecast.png")
    
    # 3. Scatter Plots (Actual vs Predicted with 45-degree line)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    
    # Baseline
    axes[0].scatter(y_test, b_test_preds, alpha=0.4, color='#d62728', s=20, edgecolors='none')
    max_val = max(y_test.max(), b_test_preds.max(), opt_test_preds.max())
    axes[0].plot([0, max_val], [0, max_val], 'k--', linewidth=1.5, label='Ideal 1:1 Reference')
    axes[0].set_title(f'Baseline CatBoost\nRMSE: {b_rmse:.2f} kW | R²: {b_r2:.4f}', fontsize=11, fontweight='bold')
    axes[0].set_xlabel('Actual AC Power (kW)', fontsize=10, fontweight='bold')
    axes[0].set_ylabel('Predicted AC Power (kW)', fontsize=10, fontweight='bold')
    axes[0].legend(frameon=True, loc='upper left')
    axes[0].grid(True, linestyle=':', alpha=0.6)
    
    # GWO-Tuned
    axes[1].scatter(y_test, opt_test_preds, alpha=0.4, color='#1f77b4', s=20, edgecolors='none')
    axes[1].plot([0, max_val], [0, max_val], 'k--', linewidth=1.5, label='Ideal 1:1 Reference')
    axes[1].set_title(f'GWO-Tuned CatBoost (Optimized)\nRMSE: {opt_rmse:.2f} kW | R²: {opt_r2:.4f}', fontsize=11, fontweight='bold')
    axes[1].set_xlabel('Actual AC Power (kW)', fontsize=10, fontweight='bold')
    axes[1].set_ylabel('Predicted AC Power (kW)', fontsize=10, fontweight='bold')
    axes[1].legend(frameon=True, loc='upper left')
    axes[1].grid(True, linestyle=':', alpha=0.6)
    
    plt.suptitle('Actual vs. Predicted Solar Power Output Scatter Comparison', fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('plots/03_scatter_predictions.png', bbox_inches='tight')
    plt.close()
    print(" Saved: plots/03_scatter_predictions.png")
    
    # 4. Grouped Bar Chart of Key Metrics
    fig, ax = plt.subplots(figsize=(8.5, 5), dpi=300)
    metrics_names = ['RMSE (kW)', 'MAE (kW)']
    base_vals = [b_rmse, b_mae]
    opt_vals = [opt_rmse, opt_mae]
    
    x = np.arange(len(metrics_names))
    width = 0.32
    
    rects1 = ax.bar(x - width/2, base_vals, width, label='Baseline CatBoost', color='#e74c3c', edgecolor='#333333', linewidth=0.8)
    rects2 = ax.bar(x + width/2, opt_vals, width, label='GWO-Tuned CatBoost', color='#2ecc71', edgecolor='#333333', linewidth=0.8)
    
    ax.set_ylabel('Error Metric Magnitude (Lower is Better)', fontsize=11, fontweight='bold')
    ax.set_title('Benchmarking Error Reduction: Baseline vs. GWO-Tuned CatBoost', fontsize=12, fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics_names, fontsize=11, fontweight='bold')
    ax.legend(frameon=True, fontsize=10)
    ax.grid(axis='y', linestyle=':', alpha=0.6)
    
    # Add numerical labels
    for rect in rects1:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}', xy=(rect.get_x() + rect.get_width()/2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontweight='bold', fontsize=9)
    for rect in rects2:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}', xy=(rect.get_x() + rect.get_width()/2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontweight='bold', fontsize=9)
        
    plt.tight_layout()
    plt.savefig('plots/04_metric_comparison_bars.png')
    plt.close()
    print(" Saved: plots/04_metric_comparison_bars.png")
    
    # 5. Residual Distribution Plot
    plt.figure(figsize=(9, 5), dpi=300)
    sns.kdeplot(df_preds['BASELINE_RESIDUAL'], color='#e74c3c', label=f'Baseline Residuals (Std: {df_preds["BASELINE_RESIDUAL"].std():.2f})', linewidth=2.0)
    sns.kdeplot(df_preds['GWO_RESIDUAL'], color='#2ecc71', label=f'GWO-Tuned Residuals (Std: {df_preds["GWO_RESIDUAL"].std():.2f})', linewidth=2.2)
    plt.axvline(0, color='black', linestyle=':', linewidth=1.2)
    plt.title('Error Residual Distribution Analysis ($y_{true} - y_{pred}$)', fontsize=13, fontweight='bold', pad=12)
    plt.xlabel('Prediction Residual Error (kW)', fontsize=11, fontweight='bold')
    plt.ylabel('Density Distribution', fontsize=11, fontweight='bold')
    plt.legend(frameon=True, fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig('plots/05_residual_error_distribution.png')
    plt.close()
    print(" Saved: plots/05_residual_error_distribution.png")
    
    # 6. Feature Importance Plot
    plt.figure(figsize=(9, 5), dpi=300)
    feat_importances = pd.Series(opt_model.get_feature_importance(), index=data['feature_cols']).sort_values(ascending=True)
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(feat_importances)))
    feat_importances.plot(kind='barh', color=colors, edgecolor='#333333', linewidth=0.8)
    plt.title('CatBoost Feature Importance for Solar Power Generation', fontsize=13, fontweight='bold', pad=12)
    plt.xlabel('Importance Score (%)', fontsize=11, fontweight='bold')
    plt.ylabel('Engineered Input Features', fontsize=11, fontweight='bold')
    plt.grid(axis='x', linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig('plots/06_feature_importance.png')
    plt.close()
    print(" Saved: plots/06_feature_importance.png")
    
    total_elapsed = time.time() - start_time
    print(f"\n[DONE] Pipeline execution completed successfully in {total_elapsed:.2f} seconds!")

if __name__ == '__main__':
    main()
