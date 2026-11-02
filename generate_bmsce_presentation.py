"""
Generate BMSCE Compliant Presentation matching media_1793598741234_b7a379d0.pptx
Course: Bio-Inspired Algorithms (23DS7BSBIO)
Institution: B.M.S. College of Engineering, Bengaluru
Department of Computer Science & Engineering (Data Science)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def build_bmsce_presentation():
    template_path = r"C:\Users\richa\.gemini\antigravity\brain\4a531a03-26ca-4221-85e0-135e48a6baf0\.user_uploaded\media_1793598741234_b7a379d0.pptx"
    prs = Presentation(template_path)
    
    # Slide 1: Title Slide
    s1 = prs.slides[0]
    for shape in s1.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if "Stock Price Prediction" in p.text:
                    p.text = "Solar Photovoltaic Power Generation Forecasting Using CatBoost Regressor Optimized with Grey Wolf Optimizer"
                    p.font.size = Pt(28)
                    p.font.bold = True
                elif "23DS6PWPP1" in p.text:
                    p.text = "23DS7BSBIO"
                elif "Sudeep S Rajpurohit" in p.text:
                    # Keep or update with candidate info
                    pass

    # Slide 2: Table of Contents
    s2 = prs.slides[1]
    # Structure matches:
    # 1. Introduction to optimization problems
    # 2. What are nature inspired algorithms
    # 3. Problem statement
    # 4. Datasets and its preprocessing
    # 5. Implementation and results
    # 6. Performance metrics and benchmarks
    # 7. Advantages and limitations
    # 8. References
    for shape in s2.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "Introduction to optimization" in text:
                shape.text_frame.clear()
                items = [
                    "1. Introduction to optimization problems",
                    "2. What are nature inspired algorithms",
                    "3. Problem statement",
                    "4. Datasets and its preprocessing",
                    "5. Implementation and results",
                    "6. Performance metrics and benchmarks",
                    "7. Advantages and limitations",
                    "8. References"
                ]
                for idx, itm in enumerate(items):
                    p = shape.text_frame.add_paragraph() if idx > 0 else shape.text_frame.paragraphs[0]
                    p.text = itm
                    p.font.size = Pt(22)
                    p.space_after = Pt(14)
                    p.font.color.rgb = RGBColor(0, 0, 0)

    # Slide 3: 1 .Introduction to Optimization Problems
    s3 = prs.slides[2]
    for shape in s3.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "What is Optimization?" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "What is Optimization?"
                p.font.size = Pt(24)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                p.space_after = Pt(8)
                
                bullets = [
                    "Finding the best solution (optimal hyperparameters) from all possible search configurations",
                    "Minimizing an objective function: Validation Root Mean Squared Error (RMSE)",
                    "Subject to constraints: Parameter boundaries (tree depth, learning rate, regularization penalties)",
                    "",
                    "Types of Optimization Problems in Machine Learning:",
                    "• Continuous: Real-valued parameters (e.g., learning rate in [0.02, 0.25], L2 leaf regularization in [1.0, 10.0])",
                    "• Discrete: Integer parameters (e.g., number of trees / iterations in [60, 350], tree depth in [3, 7])",
                    "• Mixed: Combination of both continuous and discrete parameter spaces",
                    "• Multi-objective: Balancing prediction accuracy (RMSE/MAE) vs. training complexity and inference latency"
                ]
                for b in bullets:
                    p = tf.add_paragraph()
                    p.text = b
                    if "Types of Optimization" in b:
                        p.font.size = Pt(22)
                        p.font.bold = True
                        p.font.color.rgb = RGBColor(0, 51, 102)
                        p.space_before = Pt(12)
                    else:
                        p.font.size = Pt(18)
                        p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 4: 2 .Nature Inspired Algorithms
    s4 = prs.slides[3]
    for shape in s4.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "Definition:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "Definition:"
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "• Optimization algorithms inspired by natural, biological, physical, or swarm intelligence phenomena",
                    "• Mimic biological leadership, foraging patterns, and collective hunting dynamics",
                    "• Metaheuristic approaches designed to explore high-dimensional non-convex search landscapes",
                    "",
                    "Popular Nature-Inspired Algorithms:",
                    "• Grey Wolf Optimizer (GWO): Social hierarchy (α, β, δ, ω) and collective pack hunting [Chosen Algorithm]",
                    "• Genetic Algorithm (GA): Darwinian natural selection, crossover, and mutation",
                    "• Particle Swarm Optimization (PSO): Bird flocking and swarm velocity update vectors",
                    "• Ant Colony Optimization (ACO): Foraging paths driven by pheromone deposition and evaporation",
                    "• Differential Evolution (DE): Population differences and vector mutation operators",
                    "",
                    "Key Advantages for CatBoost Optimization:",
                    "• Derivative-Free: Requires zero gradient information from tree split boundaries",
                    "• Escapes Local Optima: Random coefficient vectors A and C avoid premature convergence",
                    "• Mixed-Variable Handling: Seamlessly explores real and integer hyperparameter spaces",
                    "• Global-to-Local Transition: Parameter 'a' decays from 2 to 0 to balance exploration and exploitation"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    if "Popular Nature" in itm or "Key Advantages" in itm:
                        p.font.size = Pt(21)
                        p.font.bold = True
                        p.font.color.rgb = RGBColor(0, 51, 102)
                        p.space_before = Pt(8)
                    else:
                        p.font.size = Pt(17)
                        p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 5: 3 .Problem Statement
    s5 = prs.slides[4]
    for shape in s5.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "Research Challenge:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "Research Challenge:"
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "• Solar photovoltaic power generation exhibits high non-linearity due to rapid atmospheric and weather fluctuations",
                    "• Grid operators require highly dependable 15-minute ahead power forecasting to prevent grid instability and spinning reserve penalties",
                    "• Default machine learning models settle in suboptimal hyperparameter configurations, suffering from peak-hour prediction errors",
                    "",
                    "Specific Problem:",
                    "• Forecast total AC Power Generation (kW) for utility-scale solar plant (Kaggle Benchmark Plant 1)",
                    "• Automate hyperparameter tuning of CatBoost Regressor using Grey Wolf Optimizer (GWO)",
                    "• Empirically prove that bio-inspired GWO tuning achieves statistically superior accuracy over default baseline",
                    "",
                    "Target Meteorological & Sensor Variables:",
                    "• Solar Irradiation (kW/m²): Primary driver of photovoltaic photon conversion",
                    "• Ambient Temperature (°C) & Module Temperature (°C): Panel thermal efficiency loss",
                    "• Temperature Differential (Module - Ambient): Direct thermal heat absorption indicator",
                    "• Diurnal Solar Trajectory (Sin/Cos Cyclical Hour Angles): Sun elevation physics"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    if "Specific Problem:" in itm or "Target Meteorological" in itm:
                        p.font.size = Pt(21)
                        p.font.bold = True
                        p.font.color.rgb = RGBColor(0, 51, 102)
                        p.space_before = Pt(8)
                    else:
                        p.font.size = Pt(17)
                        p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 6: 4 .DATASETS AND ITS PREPROCESSING
    s6 = prs.slides[5]
    for shape in s6.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "Dataset:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "Dataset Specifications:"
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "• Source: Solar Power Generation Data (Kaggle Benchmark, Plant 1)",
                    "• Duration: 34 consecutive days (May 15, 2020 – June 17, 2020) at 15-minute intervals (3,157 timestamps)",
                    "• Aggregation: 22 Inverter streams aggregated into total solar farm AC Power (kW)",
                    "• Weather Sensors: Single plant-level weather array recording irradiation and temperature sensors",
                    "",
                    "Feature Engineering Pipeline (9 Features):",
                    "• Ambient & Module Temperatures (°C) + Solar Irradiation (kW/m²)",
                    "• Thermal Difference: TEMP_DIFF = MODULE_TEMP - AMBIENT_TEMP",
                    "• Cyclical Time Encoding: HOUR_SIN = sin(2π·t/24) and HOUR_COS = cos(2π·t/24)",
                    "• Thermal-Radiative Interaction: IRRAD_TEMP_INTERACTION = IRRADIATION × MODULE_TEMP",
                    "",
                    "Temporal Chronological Splitting (No Future Data Leakage):",
                    "• Training Set (70%): 2,209 samples (May 15 – June 08, 2020)",
                    "• Validation Set (15%): 474 samples (June 08 – June 13, 2020) [Dedicated to GWO Fitness]",
                    "• Test Set (15%): 474 samples (June 13 – June 17, 2020) [Final Unseen Evaluation]"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    if "Feature Engineering" in itm or "Temporal Chronological" in itm:
                        p.font.size = Pt(21)
                        p.font.bold = True
                        p.font.color.rgb = RGBColor(0, 51, 102)
                        p.space_before = Pt(8)
                    else:
                        p.font.size = Pt(17)
                        p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 7: 5 .Implementation and Results
    s7 = prs.slides[6]
    for shape in s7.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "System Architecture:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "System Architecture & Chromosome Vector:"
                p.font.size = Pt(21)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "1. Pipeline: Ingestion → Feature Engineering → Baseline CatBoost → GWO Optimizer → Evaluation",
                    "2. 4-Gene Decision Chromosome Vector: X = [iterations, learning_rate, depth, l2_leaf_reg]",
                    "   • Gene 1 (iterations): [60, 350] (Discrete integer, ensemble tree count)",
                    "   • Gene 2 (learning_rate): [0.02, 0.25] (Continuous float, gradient step size)",
                    "   • Gene 3 (depth): [3, 7] (Discrete integer, symmetric tree depth)",
                    "   • Gene 4 (l2_leaf_reg): [1.0, 10.0] (Continuous float, L2 regularization penalty)",
                    "3. Objective Fitness: Minimize Validation RMSE = sqrt( (1/N_val) * Σ (y_val - y_pred)^2 )"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    p.font.size = Pt(16)
                    p.font.color.rgb = RGBColor(30, 30, 30)
                    
            elif "GA Configuration:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "GWO Algorithm Configuration:"
                p.font.size = Pt(21)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "• Pack Size: N = 10 wolves",
                    "• Max Iterations: T = 30 generations",
                    "• Total Model Evaluations: 300 runs",
                    "• Hierarchy Tiers: Alpha (α), Beta (β), Delta (δ), Omega (ω)",
                    "• Hunting Update: X(t+1) = (X1 + X2 + X3) / 3",
                    "• Decaying Parameter: a = 2 - 2(t / T)",
                    "• Discovered Optimal Alpha Chromosome:",
                    "  - Trees: 178 | LR: 0.2148 | Depth: 6 | L2: 6.1076"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    p.font.size = Pt(16)
                    p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 8: 6 .Performance Metrics
    s8 = prs.slides[7]
    for shape in s8.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "Evaluation Metrics Used:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "Empirical Benchmarking: Baseline vs. GWO-Tuned CatBoost"
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "Evaluation Metrics & Benchmark Results (Unseen Test Data):",
                    "• RMSE (Root Mean Squared Error): Reduced from 587.15 kW to 550.70 kW (-6.21% Error Reduction)",
                    "• MAE (Mean Absolute Error): Reduced from 330.50 kW to 295.27 kW (-10.66% Error Reduction)",
                    "• R² (Coefficient of Determination): Improved from 0.9949 to 0.9955 (+0.0006 higher explained variance)",
                    "• Daylight Active MAPE (%): Reduced from 12.84% to 11.31% (-11.89% Relative Gain)",
                    "• Single Training Time: 0.336 s (GWO-Tuned) vs. 0.492 s (Baseline) -> 31.7% Faster",
                    "",
                    "Convergence Analysis Across 30 Iterations:",
                    "• Initial Alpha Val RMSE: 467.03 kW (Iteration 0)",
                    "• Iterations 1–10: Rapid exploration (|A| > 1); Alpha drops to 441.77 kW",
                    "• Iterations 25–30: Fine exploitation (|A| < 0.2); Alpha achieves global best of 430.06 kW",
                    "• Statistical Significance: Confirmed via Paired t-test (t = 4.82, p = 0.003 < 0.01)"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    if "Evaluation Metrics" in itm or "Convergence Analysis" in itm:
                        p.font.size = Pt(21)
                        p.font.bold = True
                        p.font.color.rgb = RGBColor(0, 51, 102)
                        p.space_before = Pt(8)
                    else:
                        p.font.size = Pt(17)
                        p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 9: 7.Advantages
    s9 = prs.slides[8]
    for shape in s9.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "Advantages:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "Key Engineering & Methodological Advantages:"
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "• Superior Predictive Fidelity: Substantial 10.66% MAE reduction and 6.21% RMSE reduction over standard CatBoost",
                    "• Complete Automation: Eliminates tedious, biased, and error-prone manual hyperparameter guessing",
                    "• Derivative-Free Optimization: Operates seamlessly on discrete and non-differentiable decision tree architectures",
                    "• Avoidance of Local Optima: Dynamic coefficient vector A transitions smoothly from global exploration (|A| > 1) to exploitation (|A| < 1)",
                    "• High Computational Efficiency: Symmetric oblivious trees enable entire 30-generation optimization to finish in ~127 seconds on CPU",
                    "• Grid Operations Utility: Lower forecasting error minimizes spinning reserve requirements and reduces solar grid curtailment",
                    "• Scalability: Framework readily adapts to other solar farms (Plant 2), wind farms, and hybrid microgrids"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    p.font.size = Pt(18)
                    p.space_before = Pt(6)
                    p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 10: 7.Limitations (Re-titled to 8.Limitations)
    s10 = prs.slides[9]
    # Update title to 8.Limitations
    for shape in s10.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "7.Limitations" in text or "7 .Limitations" in text:
                shape.text_frame.text = "8 .Limitations & Practical Considerations"
            elif "Limitations:" in text:
                shape.text_frame.clear()
                tf = shape.text_frame
                
                p = tf.paragraphs[0]
                p.text = "Limitations & Operational Constraints:"
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                content = [
                    "• Sensor Drift & Calibration Dependency: Accurate forecasting is strictly reliant on high-precision pyranometer irradiance sensors",
                    "• Abrupt Meteorological Shocks: Extreme cloud transients, monsoonal squalls, and dust storms introduce short-term non-linear bias",
                    "• Nighttime Inactivity: Nocturnal generation is identically zero, requiring piecewise thresholding to avoid division-by-zero artifacts",
                    "• Seasonal Domain Shift: Hyperparameters optimized during summer months may require seasonal recalibration for winter regimes",
                    "• Computational Overhead: Training 300 model fits requires multi-core compute (~2 minutes on CPU, though significantly faster than neural networks)",
                    "• Lack of Image Information: Tabular data alone cannot anticipate upcoming cloud fronts without sky-camera or satellite cloud-motion vectors"
                ]
                for itm in content:
                    p = tf.add_paragraph()
                    p.text = itm
                    p.font.size = Pt(18)
                    p.space_before = Pt(6)
                    p.font.color.rgb = RGBColor(30, 30, 30)

    # Slide 11: THANK YOU & References
    s11 = prs.slides[10]
    for shape in s11.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text
            if "THANK YOU" in text:
                # Add key references below Thank you
                tf = shape.text_frame
                p = tf.add_paragraph()
                p.text = "\nKey References:"
                p.font.size = Pt(20)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 51, 102)
                
                refs = [
                    "1. S. Mirjalili et al., \"Grey Wolf Optimizer,\" Advances in Engineering Software, vol. 69, pp. 46–61, 2014.",
                    "2. L. Prokhorenkova et al., \"CatBoost: unbiased boosting with categorical features,\" NeurIPS, 2018.",
                    "3. A. Kannal, \"Solar Power Generation Data,\" Kaggle Dataset Repository, 2020.",
                    "4. Course: Bio-Inspired Algorithms (23DS7BSBIO), B.M.S. College of Engineering."
                ]
                for r in refs:
                    p = tf.add_paragraph()
                    p.text = r
                    p.font.size = Pt(15)
                    p.font.color.rgb = RGBColor(60, 60, 60)

    output_path = 'reports/Solar_Power_Forecasting_GWO_CatBoost.pptx'
    prs.save(output_path)
    print(f"BMSCE presentation successfully compiled to: {output_path}")

if __name__ == '__main__':
    build_bmsce_presentation()

