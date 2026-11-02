"""
Generate University Presentation (PPT) for Bio-Inspired Algorithms AAT
File: Solar_Power_Forecasting_GWO_CatBoost.pptx
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    os.makedirs('reports', exist_ok=True)
    prs = Presentation()
    # 16:9 Widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Color palette
    NAVY = RGBColor(24, 43, 73)
    GOLD = RGBColor(212, 143, 24)
    SLATE = RGBColor(50, 60, 75)
    LIGHT_BG = RGBColor(245, 247, 250)
    WHITE = RGBColor(255, 255, 255)
    GREEN = RGBColor(34, 139, 34)
    RED = RGBColor(178, 34, 34)
    
    blank_layout = prs.slide_layouts[6] # Blank
    
    def add_header(slide, title_text, category_text="COURSE: 23DS7BSBIO | ALTERNATIVE ASSESSMENT TOOL (AAT)"):
        # Header banner
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p0 = tf.paragraphs[0]
        p0.text = category_text.upper()
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = GOLD
        
        p1 = tf.add_paragraph()
        p1.text = title_text
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = NAVY
        
    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.color.rgb = NAVY
    
    title_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.0))
    tf1 = title_box.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "BIO-INSPIRED ALGORITHMS (23DS7BSBIO)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = GOLD
    
    p = tf1.add_paragraph()
    p.text = "Solar Photovoltaic Power Generation Forecasting\nOptimized with Grey Wolf Optimizer (GWO)"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(15)
    
    p = tf1.add_paragraph()
    p.text = "Hyperparameter Tuning of CatBoost Regressor using Swarm Social Hierarchy\nEmpirical Comparative Benchmarking & Diurnal Forecasting"
    p.font.size = Pt(16)
    p.font.color.rgb = RGBColor(200, 215, 230)
    p.space_before = Pt(12)
    
    p = tf1.add_paragraph()
    p.text = "Alternative Assessment Tool (AAT) Deliverable | 7th Semester"
    p.font.size = Pt(13)
    p.font.italic = True
    p.font.color.rgb = GOLD
    p.space_before = Pt(25)

    # -------------------------------------------------------------
    # SLIDE 2: Problem Statement & Motivation
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "1. Problem Formulation & Motivation")
    
    tb2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    
    def add_bullet(tf, heading, body, before=10):
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.space_before = Pt(before)
        run_h = p.add_run()
        run_h.text = heading + " "
        run_h.font.bold = True
        run_h.font.size = Pt(14)
        run_h.font.color.rgb = NAVY
        
        run_b = p.add_run()
        run_b.text = body
        run_b.font.size = Pt(13)
        run_b.font.color.rgb = SLATE
        
    add_bullet(tf2, "The Core Engineering Problem:",
               "Solar photovoltaic (PV) power generation exhibits non-linear intermittency driven by solar irradiation, ambient air temperatures, and module thermal dynamics. Reliable grid dispatch requires precise 15-minute generation forecasting.")
    add_bullet(tf2, "The Baseline Limitation:",
               "Standard Machine Learning baselines (CatBoost/GBDT with default hyperparameters) often settle in sub-optimal configurations, yielding higher Root Mean Squared Error (RMSE) and poor generalization during peak diurnal irradiance.")
    add_bullet(tf2, "Why Nature-Inspired Optimization (GWO)?:",
               "Traditional grid search or random search are computationally exhaustive. Grey Wolf Optimizer (GWO) mathematically models leadership hierarchy (Alpha, Beta, Delta) and adaptive exploration-to-exploitation mechanisms to discover global optimal hyperparameters.")
    add_bullet(tf2, "Objective of This Project:",
               "1) Formulate clean time-series pipeline on real-world Kaggle Solar Power plant data.\n2) Establish benchmark default CatBoost regressor.\n3) Design chromosome vector and fitness function for GWO.\n4) Empirically demonstrate statistically significant error reduction.")

    # -------------------------------------------------------------
    # SLIDE 3: Dataset & Preprocessing Pipeline
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "2. Dataset Pipeline & Feature Engineering")
    
    tb3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.2))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    
    add_bullet(tf3, "Dataset Specifications:",
               "• Benchmark Kaggle Solar Power Generation Dataset (Plant 1)\n• 34 days of continuous sensor records at 15-minute resolution (3,157 intervals)\n• 22 Inverter generation streams aggregated to total plant AC Power generation (kW)")
    add_bullet(tf3, "Engineered Feature Matrix (9 Dimensions):",
               "1. AMBIENT_TEMPERATURE (°C)\n2. MODULE_TEMPERATURE (°C)\n3. IRRADIATION (kW/m²)\n4. TEMP_DIFF (Thermal gradient: Module - Ambient)\n5. HOUR & MINUTE (Temporal markers)\n6. HOUR_SIN & HOUR_COS (Cyclical diurnal solar trajectory)\n7. IRRAD_TEMP_INTERACTION (Thermal-radiation physics coupling)")
    add_bullet(tf3, "Temporal Chronological Split:",
               "• Train Set: 70% (2,209 samples, May 15 – June 08)\n• Validation Set: 15% (474 samples, June 08 – June 13) [For GWO Fitness]\n• Test Set: 15% (474 samples, June 13 – June 17) [Final Unseen Evaluation]\n• Zero future leakage guaranteed via chronological partitioning.")
               
    if os.path.exists('plots/06_feature_importance.png'):
        s3.shapes.add_picture('plots/06_feature_importance.png', Inches(7.1), Inches(1.8), width=Inches(5.4))

    # -------------------------------------------------------------
    # SLIDE 4: Baseline Model Development
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "3. Baseline Benchmark: CatBoost Regressor")
    
    tb4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    
    add_bullet(tf4, "Why CatBoost Regressor?:",
               "CatBoost implements symmetric (oblivious) decision trees that offer superior computational speed, resistance to overfitting, and balanced tree structure, making it ideal for inner-loop metaheuristic evaluations.")
    add_bullet(tf4, "Default Baseline Configuration:",
               "• Number of Trees (iterations): 200\n• Learning Rate: 0.03\n• Tree Depth: 6\n• L2 Leaf Regularization: 3.0")
    add_bullet(tf4, "Recorded Baseline Benchmark Metrics (On Unseen Test Data):",
               "• Root Mean Squared Error (RMSE): 587.15 kW\n• Mean Absolute Error (MAE): 330.50 kW\n• Coefficient of Determination (R²): 0.9949\n• Daylight Mean Absolute Percentage Error (MAPE): 12.84%\n• Training Latency: 0.49 seconds")
    add_bullet(tf4, "Baseline Evaluation Verdict:",
               "While default CatBoost captures general diurnal curves, systematic errors persist during rapid cloud transients and thermal saturation peaks, necessitating bio-inspired hyperparameter optimization.")

    # -------------------------------------------------------------
    # SLIDE 5: Nature-Inspired Algorithm Formulation: GWO
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "4. Grey Wolf Optimizer (GWO) Formulation")
    
    tb5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf5 = tb5.text_frame
    tf5.word_wrap = True
    
    add_bullet(tf5, "Biological Inspiration (Mirjalili et al., 2014):",
               "Simulates social dominance hierarchy and collective cooperative hunting mechanisms of grey wolves (Canis lupus) in nature.")
    add_bullet(tf5, "Social Leadership Hierarchy:",
               "• Alpha (α): Fittest individual; leads hunting decisions (Global Best Hyperparameter Vector)\n• Beta (β): Second fittest wolf; assists in commanding the pack\n• Delta (δ): Third fittest wolf; serves as scouts and sentinels\n• Omega (ω): Subordinate pack wolves repositioned relative to α, β, and δ")
    add_bullet(tf5, "Mathematical Encircling & Hunting Equations:",
               "Distance to Leaders:  D_α = |C_1 · X_α - X|,   D_β = |C_2 · X_β - X|,   D_δ = |C_3 · X_δ - X|\n"
               "Position Candidates: X_1 = X_α - A_1 · D_α,   X_2 = X_β - A_2 · D_β,   X_3 = X_δ - A_3 · D_δ\n"
               "Wolf Position Update:  X(t+1) = (X_1 + X_2 + X_3) / 3\n"
               "Decaying Coefficient:  a = 2 - 2(t / MaxIter),   A = 2a · r_1 - a,   C = 2 · r_2")
    add_bullet(tf5, "Exploration vs. Exploitation Balance:",
               "When |A| > 1, wolves diverge to explore new hyperparameter regions. When |A| < 1, wolves converge to attack and exploit the global minimum around Alpha.")

    # -------------------------------------------------------------
    # SLIDE 6: Chromosome & Fitness Function Design
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. Chromosome Design & Fitness Formulation")
    
    tb6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    
    add_bullet(tf6, "Chromosome / Decision Vector Representation:",
               "Every wolf position vector represents a candidate hyperparameter tuple:  X = [x_1, x_2, x_3, x_4]")
    add_bullet(tf6, "Search Space Domain Boundaries:",
               "1. x_1 (iterations): [60, 350]  (Discrete integer, tree ensemble count)\n"
               "2. x_2 (learning_rate): [0.02, 0.25]  (Continuous float, gradient step size)\n"
               "3. x_3 (depth): [3, 7]  (Discrete integer, oblivious tree depth)\n"
               "4. x_4 (l2_leaf_reg): [1.0, 10.0]  (Continuous float, L2 regularization penalty)")
    add_bullet(tf6, "Fitness Function Formulation:",
               "Objective is to minimize generalization error on the Validation split:\n"
               "   Fitness(X) = RMSE_val(X) = sqrt( (1 / N_val) * sum (y_val - y_pred(X))^2 )\n"
               "Alternative Fitness Formulation: Fitness_Score = 1 / (1 + RMSE_val)")
    add_bullet(tf6, "Optimizer Hyperparameters:",
               "• Population Size: N = 10 wolves\n• Max Generations / Iterations: T = 30\n• Total Evaluations: 300 models\n• Seed: 42 (Reproducible)")

    # -------------------------------------------------------------
    # SLIDE 7: Convergence Analysis
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "6. Optimization Convergence Analysis")
    
    tb7 = s7.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.2))
    tf7 = tb7.text_frame
    tf7.word_wrap = True
    
    add_bullet(tf7, "Convergence Dynamics:",
               "• Initial Wolf Pack Best: 467.03 kW Val RMSE (already better than 574 kW baseline)\n"
               "• Iterations 1–10: Rapid exploration phase (|A| > 1); Alpha drops to 441.77 kW\n"
               "• Iterations 11–24: Steady refinement around leadership wolves\n"
               "• Iteration 27: Final exploitation breakthrough (|A| < 0.2); Alpha achieves 430.06 kW Val RMSE")
    add_bullet(tf7, "Discovered Optimal Alpha Chromosome:",
               "• iterations: 178\n• learning_rate: 0.2148\n• depth: 6\n• l2_leaf_reg: 6.1076")
    add_bullet(tf7, "Key Algorithmic Finding:",
               "GWO dynamically found that a higher learning rate (0.21 vs 0.03) combined with stronger L2 leaf regularization (6.11 vs 3.0) and slightly fewer trees (178 vs 200) prevents overfitting while accelerating convergence.")
               
    if os.path.exists('plots/01_gwo_convergence.png'):
        s7.shapes.add_picture('plots/01_gwo_convergence.png', Inches(6.8), Inches(1.8), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 8: Empirical Comparison (Table & Bar Chart)
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "7. Empirical Results: Baseline vs. GWO-Tuned")
    
    # Text summary on left
    tb8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.2))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    
    add_bullet(tf8, "Performance Summary (Unseen Test Set):",
               "• RMSE: Reduced from 587.15 kW to 550.70 kW (6.21% Error Reduction)\n"
               "• MAE: Reduced from 330.50 kW to 295.27 kW (10.66% Error Reduction)\n"
               "• Daylight MAPE: Reduced from 12.84% to 11.31% (11.89% Error Reduction)\n"
               "• R² Score: Improved from 0.9949 to 0.9955\n"
               "• Training Speed: 0.336 s (faster than baseline 0.492 s due to 178 vs 200 trees)")
    add_bullet(tf8, "Empirical Validation:",
               "The nature-inspired GWO model decisively outperforms the default baseline across all four core regression metrics simultaneously.")
               
    if os.path.exists('plots/04_metric_comparison_bars.png'):
        s8.shapes.add_picture('plots/04_metric_comparison_bars.png', Inches(7.0), Inches(1.8), width=Inches(5.6))

    # -------------------------------------------------------------
    # SLIDE 9: Forecasting Visualizations
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "8. Time-Series & Error Residual Visualizations")
    
    if os.path.exists('plots/02_time_series_forecast.png'):
        s9.shapes.add_picture('plots/02_time_series_forecast.png', Inches(0.8), Inches(1.6), width=Inches(6.0))
        
    if os.path.exists('plots/05_residual_error_distribution.png'):
        s9.shapes.add_picture('plots/05_residual_error_distribution.png', Inches(7.0), Inches(1.6), width=Inches(5.6))
        
    tb9 = s9.shapes.add_textbox(Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.4))
    tf9 = tb9.text_frame
    tf9.word_wrap = True
    add_bullet(tf9, "Visual Insights:",
               "• Time Series Plot: GWO-Tuned model matches daily solar midday peaks tightly without the baseline's premature clipping.\n"
               "• Residual Distribution: GWO residuals exhibit a significantly tighter standard deviation and zero-centered Gaussian symmetry.")

    # -------------------------------------------------------------
    # SLIDE 10: Conclusion & Deliverables
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "9. Conclusion & Practical Impact")
    
    tb10 = s10.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf10 = tb10.text_frame
    tf10.word_wrap = True
    
    add_bullet(tf10, "Summary of Achievements:",
               "1. Successfully implemented complete end-to-end solar power forecasting pipeline on Kaggle Plant 1 sensor data.\n"
               "2. Encoded CatBoost hyperparameters into a 4D decision chromosome.\n"
               "3. Simulated 30 generations of Grey Wolf hunting dynamics, proving continuous fitness improvement from 467 kW to 430 kW.\n"
               "4. Empirically demonstrated 10.66% MAE reduction and 6.21% RMSE reduction on unseen test data.")
    add_bullet(tf10, "Practical Grid Management Impact:",
               "Lower forecasting error reduces spinning reserve requirements for power grid operators, mitigates imbalance penalties for solar plant managers, and enables reliable renewable energy grid penetration.")
    add_bullet(tf10, "Project Deliverables Checklist:",
               "✔ Clean Preprocessing & Feature Engineering Pipeline (`preprocess.py`)\n"
               "✔ Baseline Model Benchmark (`run_project.py`)\n"
               "✔ Complete GWO Optimizer Implementation (`gwo_optimizer.py`)\n"
               "✔ High-Resolution Visualizations & Metric Tables (`plots/`, `results/`)\n"
               "✔ Comprehensive Academic Report (`reports/*.docx`, `FINAL_PROJECT_REPORT.md`)\n"
               "✔ Professional Presentation Deck (`reports/*.pptx`)")

    prs.save('reports/Solar_Power_Forecasting_GWO_CatBoost.pptx')
    print(" Presentation created: reports/Solar_Power_Forecasting_GWO_CatBoost.pptx")

if __name__ == '__main__':
    create_deck()

