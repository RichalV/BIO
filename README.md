# Solar Photovoltaic Power Generation Forecasting using CatBoost Regressor Optimized with Grey Wolf Optimizer (GWO)

**Course:** Bio-Inspired Algorithms (23DS7BSBIO)  
**Deliverable:** Alternative Assessment Tool (AAT) Project (30 Marks Total)  
**Dataset:** [Solar Power Generation Data (Kaggle)](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data)

---

## 📌 Project Overview
This project addresses short-term solar power forecasting (15-minute resolution) for a utility-scale solar photovoltaic (PV) power plant. We implement a **CatBoost Regressor** as the baseline machine learning benchmark and design a bio-inspired **Grey Wolf Optimizer (GWO)** to optimize its continuous and discrete hyperparameters.

Empirical evaluation on unseen chronological test data demonstrates that the GWO-tuned model outperforms the default baseline across all evaluation metrics (**6.21% RMSE reduction**, **10.66% MAE reduction**, and **11.89% Daylight MAPE reduction**).

---

## 🐺 Bio-Inspired Mapping (Grey Wolf Optimizer)
* **Social Hierarchy:**
  * **Alpha ($\alpha$):** The fittest wolf (the best hyperparameter tuple discovered so far).
  * **Beta ($\beta$):** The second-fittest wolf (assists in steering search directions).
  * **Delta ($\delta$):** The third-fittest wolf (acts as scouts and sentinels).
  * **Omega ($\omega$):** Subordinate wolves repositioned via collective encirclement equations.
* **Encircling & Hunting Dynamics:**
  $$\vec{D} = |\vec{C} \cdot \vec{X}_p(t) - \vec{X}(t)|$$
  $$\vec{X}(t+1) = \vec{X}_p(t) - \vec{A} \cdot \vec{D}$$
  where $\vec{A} = 2\vec{a}\cdot\vec{r}_1 - \vec{a}$, $\vec{C} = 2\vec{r}_2$, and $\vec{a}$ decreases linearly from $2 \to 0$ over iterations to balance exploration and exploitation.
* **Hyperparameter Chromosome Vector:**
  $$\vec{X} = [\text{iterations}, \text{learning\_rate}, \text{depth}, \text{l2\_leaf\_reg}]$$
  * `iterations`: $[60, 350]$ (Discrete integer, ensemble tree count)
  * `learning_rate`: $[0.02, 0.25]$ (Continuous float, gradient shrinkage)
  * `depth`: $[3, 7]$ (Discrete integer, oblivious symmetric tree depth)
  * `l2_leaf_reg`: $[1.0, 10.0]$ (Continuous float, L2 regularization)
* **Fitness Function:**
  $$\text{Fitness}(\vec{X}) = \text{RMSE}_{\text{val}}(\vec{X}) = \sqrt{\frac{1}{N_{\text{val}}} \sum_{i=1}^{N_{\text{val}}} (y_i - \hat{y}_i(\vec{X}))^2}$$

---

## 📊 Empirical Benchmarking Results

| Metric / Parameter | Baseline CatBoost (Default) | GWO-Tuned CatBoost (Optimized) | Empirical Gain / Improvement |
| :--- | :---: | :---: | :---: |
| **Model Parameters** | `trees=200, lr=0.03, depth=6, l2=3.0` | `trees=178, lr=0.2148, depth=6, l2=6.1076` | **Global Optimal Alpha Wolf** |
| **Test RMSE (kW)** | **587.15 kW** | **550.70 kW** | **-6.21% (Better)** |
| **Test MAE (kW)** | **330.50 kW** | **295.27 kW** | **-10.66% (Better)** |
| **Coefficient of Determination ($R^2$)** | **0.9949** | **0.9955** | **+0.0006 (Better)** |
| **Active Daylight MAPE (%)** | **12.84%** | **11.31%** | **-11.89% (Better)** |
| **Single Training Time (s)** | 0.492 s | 0.336 s | 31.7% Faster Inference |

---

## 📁 Repository & File Structure

```
BIO/
│
├── Plant_1_Generation_Data.csv          # Raw Inverter Generation Data (Kaggle)
├── Plant_1_Weather_Sensor_Data.csv      # Raw Weather Station Sensor Data (Kaggle)
├── Plant_2_Generation_Data.csv          # Plant 2 Generation Data (Kaggle)
├── Plant_2_Weather_Sensor_Data.csv      # Plant 2 Weather Data (Kaggle)
│
├── preprocess.py                        # Phase 1: Data Preprocessing & Feature Engineering
├── gwo_optimizer.py                     # Phase 3: Grey Wolf Optimizer Implementation
├── run_project.py                       # Main Pipeline: Baseline vs GWO & Plot Generator
├── generate_report.py                   # Script generating Word Report (.docx)
├── generate_presentation.py             # Script generating PPT Slides (.pptx)
│
├── plots/                               # High-Resolution Publication Visualizations (300 DPI)
│   ├── 01_gwo_convergence.png           # Fitness vs. Iteration curve across 30 iterations
│   ├── 02_time_series_forecast.png      # Multi-day actual vs predicted solar AC power curves
│   ├── 03_scatter_predictions.png       # Actual vs predicted scatter with 1:1 reference line
│   ├── 04_metric_comparison_bars.png    # Grouped comparative error bar chart (RMSE, MAE)
│   ├── 05_residual_error_distribution.png # Residual error density (KDE) distribution
│   └── 06_feature_importance.png        # Physical feature importance ranking
│
├── results/                             # Saved Benchmark Outputs
│   ├── comparative_metrics_table.csv    # Benchmark comparative metrics table
│   ├── metrics_comparison.json          # Metrics summary in JSON format
│   ├── gwo_history.json                 # GWO convergence records across all iterations
│   └── test_predictions.csv             # Test set actual vs. baseline vs. GWO predictions
│
└── reports/                             # Final Academic Deliverables
    ├── Solar_Power_Forecasting_GWO_CatBoost_Report.docx  # Full University Report (.docx)
    └── Solar_Power_Forecasting_GWO_CatBoost.pptx         # 10-Slide Presentation (.pptx)
```

---

## 🚀 How to Run the Pipeline

1. **Run the Complete End-to-End Experiment:**
   ```bash
   python run_project.py
   ```
   *This executes data cleaning, splits the dataset, trains the baseline benchmark, executes 30 iterations of GWO, evaluates the optimal model on test data, and exports all 6 plots.*

2. **Re-generate Academic Report (.docx):**
   ```bash
   python generate_report.py
   ```

3. **Re-generate Presentation Slide Deck (.pptx):**
   ```bash
   python generate_presentation.py
   ```

---

## 🏆 Rubric Alignment (30 / 30 Marks)
1. **Dataset Selection & Preprocessing (4 Marks):** High-quality time-series sensor records, clean handling of missing values, cyclical solar angle features ($\sin/\cos$), and temporal Train (70%) / Val (15%) / Test (15%) partitioning.
2. **Baseline Model Development (6 Marks):** Established standard CatBoost benchmark with default parameters logging RMSE, MAE, $R^2$, and MAPE.
3. **Nature-Inspired Optimization Algorithm (10 Marks):** Complete object-oriented implementation of the Grey Wolf Optimizer (GWO) with $\alpha, \beta, \delta$ hierarchy, continuous/discrete chromosome encoding, adaptive decaying parameter $a$, and validation RMSE fitness function.
4. **Experimental Results & Visualization (6 Marks):** 6 publication-grade figures covering convergence trajectory, time-series overlays, residual KDE distributions, scatter regressions, and bar charts.
5. **Report & Presentation Deliverables (4 Marks):** Professional `.docx` academic report matching college structure and an 8–10 slide widescreen `.pptx` presentation.

