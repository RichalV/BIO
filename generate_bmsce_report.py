"""
Generate BMSCE Academic Report (.docx) Replicating media_1793598741249_c6bce7ad.pdf
Institution: B.M.S. College of Engineering (Autonomous under VTU)
Department: Department of Computer Science & Engineering (Data Science)
Course: Bio-Inspired Algorithms (23DS7BSBIO)
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_bg(cell, hex_code):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_code}"/>')
    tcPr.append(shd)

def add_footer_to_section(section, page_num_str=""):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run("Department of CSE(Data Science)          ")
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(70, 70, 70)
    if page_num_str:
        run2 = p.add_run(page_num_str)
        run2.font.name = 'Times New Roman'
        run2.font.size = Pt(10)

def build_bmsce_report():
    doc = docx.Document()
    
    # Page margins: standard academic 1.0 inch
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        
    def p_text(text, font_size=11, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=6, font_name="Times New Roman", color=RGBColor(0,0,0)):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(font_size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color
        return p

    def add_eq(eq_text, eq_num):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        
        run_eq = p.add_run(f"    {eq_text}")
        run_eq.font.name = 'Cambria Math'
        run_eq.font.size = Pt(11)
        run_eq.font.italic = True
        
        run_tab = p.add_run(f"          ({eq_num})")
        run_tab.font.name = 'Times New Roman'
        run_tab.font.size = Pt(11)

    # -------------------------------------------------------------
    # Title Page
    # -------------------------------------------------------------
    p_text("B.M.S. COLLEGE OF ENGINEERING", font_size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("(Autonomous College under VTU)", font_size=12, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("Bull Temple Road, Basavangudi, Bangalore - 560019", font_size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    
    if os.path.exists("bmsce_logo.png"):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(18)
        p_logo.add_run().add_picture("bmsce_logo.png", width=Inches(1.8))
        
    p_text("Bio Inspired Algorithms AAT on", font_size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    p_text("Solar Photovoltaic Power Generation Forecasting Using CatBoost Regressor\nOptimized with Grey Wolf Optimizer", 
           font_size=13, bold=True, color=RGBColor(180, 0, 0), align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    
    p_text("in fulfillment of the requirements for the award of degree", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    p_text("BACHELOR OF ENGINEERING", font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("in", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("Computer Science & Engineering (Data Science)", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    
    p_text("by", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    p_text("Richal (1BM22CDxxx)", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    
    p_text("Under the Guidance of", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    p_text("Manoj Kumar", font_size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("Assistant Professor", font_size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    
    p_text("Department of CSE (Data Science),", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("B.M.S. College of Engineering", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    p_text("AY 2024-2025", font_size=10, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    
    doc.add_page_break()

    # -------------------------------------------------------------
    # Certificate Page
    # -------------------------------------------------------------
    p_text("B.M.S. COLLEGE OF ENGINEERING", font_size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("(Autonomous College under VTU)", font_size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("Bull Temple Road, Basavangudi, Bangalore - 560019", font_size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    
    if os.path.exists("bmsce_logo.png"):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_after = Pt(10)
        p_logo2.add_run().add_picture("bmsce_logo.png", width=Inches(1.2))
        
    p_text("Department of Computer Science and Engineering", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    p_text("(Data Science)", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    p_text("CERTIFICATE", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    
    cert_text = (
        "This is to certify that the project entitled “Solar Photovoltaic Power Generation Forecasting "
        "Using CatBoost Regressor Optimized with Grey Wolf Optimizer” is a bona fide work carried out by "
        "the following student(s) for the course Bio Inspired Algorithms (Course Code: 23DS7BSBIO). "
        "It is certified that all corrections and suggestions indicated during the internal assessments have been incorporated "
        "in the final report submitted to the departmental library. The project report has been approved as it meets the "
        "academic requirements prescribed for the Bachelor of Engineering Degree in respect of project work."
    )
    p_text(cert_text, font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=16)
    
    p_text("Candidate details", font_size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    
    t_cert = doc.add_table(rows=2, cols=4)
    t_cert.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = ["SL. NO.", "Student Name", "USN", "Student's Signature"]
    for i, h in enumerate(hdr):
        cell = t_cert.rows[0].cells[i]
        cell.text = h
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(10)
        set_cell_bg(cell, "F2F2F2")
        
    row1 = ["1", "Richal", "1BM22CDxxx", ""]
    for i, val in enumerate(row1):
        cell = t_cert.rows[1].cells[i]
        cell.text = val
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell.paragraphs[0].runs[0].font.size = Pt(10)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(28)
    
    t_sig = doc.add_table(rows=2, cols=2)
    t_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sig.rows[0].cells[0].paragraphs[0].text = "Signature of the Guide\nManoj Kumar\nAssistant Professor"
    t_sig.rows[0].cells[1].paragraphs[0].text = "Signature of the HOD\nDr. Shambhavi B R\nProfessor & HOD"
    t_sig.rows[0].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    doc.add_paragraph().paragraph_format.space_after = Pt(24)
    p_text("Examiners", font_size=11, bold=True, space_after=6)
    
    t_ex = doc.add_table(rows=2, cols=2)
    t_ex.rows[0].cells[0].paragraphs[0].text = "Name of Examiner\n1.\n2."
    t_ex.rows[0].cells[1].paragraphs[0].text = "Signature of the examiner\n_________________________\n_________________________"
    t_ex.rows[0].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    doc.add_page_break()

    # -------------------------------------------------------------
    # Acknowledgements
    # -------------------------------------------------------------
    p_text("Acknowledgements", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    
    ack_1 = (
        "We would take this opportunity to express our heart-felt gratitude to Dr. B. S. Ragini Narayan, Chairperson, "
        "Donor Trustee, Member Secretary & Chairperson, BMSET. Dr. P. Dayananda Pai, Member Life Trustee, BMSET and "
        "Dr. Bheemsha Arya, Principal, B.M.S. College of Engineering for providing the necessary infrastructure to complete "
        "this Alternative Assessment."
    )
    p_text(ack_1, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12)
    
    ack_2 = (
        "We wish to express our deepest gratitude and thanks to Dr. Shambhavi B R, Head of the Department, "
        "Computer Science and Engineering (Data Science) and the Project Guide Manoj Kumar S for their constant support."
    )
    p_text(ack_2, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12)
    
    ack_3 = (
        "A warm thanks to all the faculty of the Department of Computer Science and Engineering (Data Science), "
        "who have helped us with their views and encouraging ideas."
    )
    p_text(ack_3, font_size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=16)
    
    doc.add_page_break()

    # -------------------------------------------------------------
    # Contents (Original Page Numbering As In User's Reference Document)
    # -------------------------------------------------------------
    p_text("Contents", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    
    toc_items = [
        ("Acknowledgements", "2"),
        ("0.1   Introduction", "1"),
        ("      0.1.1   Background and Motivation", "1"),
        ("      0.1.2   Problem Statement", "1"),
        ("      0.1.3   Research Objectives", "1"),
        ("      0.1.4   Contributions", "2"),
        ("      0.1.5   Paper Organization", "2"),
        ("0.2   Literature Review", "2"),
        ("      0.2.1   Solar Power Prediction Techniques", "2"),
        ("      0.2.2   Deep Learning & GBDT for Renewable Forecasting", "3"),
        ("      0.2.3   Hyperparameter Optimization Methods", "3"),
        ("      0.2.4   Metaheuristic Algorithms in Energy Systems", "3"),
        ("      0.2.5   CatBoost Optimization with Swarm Methods", "3"),
        ("      0.2.6   Indian Solar Plant Studies", "3"),
        ("      0.2.7   Research Gap", "4"),
        ("0.3   Theoretical Background", "4"),
        ("      0.3.1   Time Series Forecasting in Photovoltaics", "4"),
        ("      0.3.2   CatBoost Regressor Architecture", "4"),
        ("      0.3.3   Symmetric Oblivious Decision Trees", "4"),
        ("      0.3.4   Meteorological Feature Engineering", "5"),
        ("      0.3.5   Grey Wolf Optimizer Fundamentals", "5"),
        ("      0.3.6   Evaluation Metrics", "6"),
        ("0.4   Nature-Inspired Algorithms: Detailed Study", "7"),
        ("      0.4.1   Overview of Nature-Inspired Optimization", "7"),
        ("      0.4.2   Grey Wolf Optimizer: In-Depth Analysis", "7"),
        ("      0.4.3   Particle Swarm Optimization", "9"),
        ("      0.4.4   Ant Colony Optimization", "9"),
        ("      0.4.5   Simulated Annealing", "9"),
        ("      0.4.6   Differential Evolution", "10"),
        ("      0.4.7   Why Grey Wolf Optimizer for CatBoost?", "10"),
        ("      0.4.8   Hybrid Approaches", "10"),
        ("0.5   Methodology and Implementation", "10"),
        ("      0.5.1   System Architecture", "10"),
        ("      0.5.2   Data Collection & Solar Plant Specifications", "11"),
        ("      0.5.3   Data Preprocessing", "11"),
        ("      0.5.4   Feature Engineering", "12"),
        ("      0.5.5   CatBoost Model Architecture", "13"),
        ("      0.5.6   Grey Wolf Optimizer Implementation", "14"),
        ("      0.5.7   Training Procedure & Temporal Splitting", "15"),
        ("      0.5.8   Implementation Details", "16"),
        ("0.6   Experimental Setup and Test Functions", "17"),
        ("      0.6.1   Experimental Configuration", "17"),
        ("      0.6.2   Baseline Models", "17"),
        ("      0.6.3   Test Functions and Benchmarks", "19"),
        ("      0.6.4   Cross-Validation Strategy", "19"),
        ("      0.6.5   Sensitivity Analysis", "20"),
        ("      0.6.6   Statistical Significance Testing", "20"),
        ("      0.6.7   Computational Efficiency Metrics", "21"),
        ("0.7   Results and Discussion", "21"),
        ("      0.7.1   GWO Convergence Analysis", "21"),
        ("      0.7.2   Optimal Hyperparameter Configuration", "21"),
        ("      0.7.3   Prediction Performance", "22"),
        ("      0.7.4   Temporal Performance Analysis", "23"),
        ("      0.7.5   Comparison with Baseline Models", "23"),
        ("      0.7.6   Hyperparameter Importance Analysis", "24"),
        ("      0.7.7   Feature Importance Results", "24"),
        ("      0.7.8   Error Analysis", "24"),
        ("      0.7.9   Computational Performance", "25"),
        ("      0.7.10 Robustness Analysis", "25"),
        ("      0.7.11 Discussion", "26"),
        ("0.8   Conclusion", "28"),
        ("0.9   Future Work", "28"),
        ("      0.9.1   Methodological Enhancements", "28")
    ]
    
    t_toc = doc.add_table(rows=len(toc_items), cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (title, pg) in enumerate(toc_items):
        cell_l = t_toc.rows[idx].cells[0]
        cell_r = t_toc.rows[idx].cells[1]
        
        p_l = cell_l.paragraphs[0]
        p_l.text = title
        p_l.paragraph_format.space_after = Pt(2)
        p_l.runs[0].font.name = 'Times New Roman'
        p_l.runs[0].font.size = Pt(10)
        if not title.startswith("      "):
            p_l.runs[0].font.bold = True
            
        p_r = cell_r.paragraphs[0]
        p_r.text = pg
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_r.paragraph_format.space_after = Pt(2)
        p_r.runs[0].font.name = 'Times New Roman'
        p_r.runs[0].font.size = Pt(10)
        if not title.startswith("      "):
            p_r.runs[0].font.bold = True
            
    doc.add_page_break()

    # -------------------------------------------------------------
    # List of Figures (Original Page Numbering)
    # -------------------------------------------------------------
    p_text("List of Figures", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    
    lof_items = [
        ("1   Model performance before optimization - baseline model", "27"),
        ("2   Model performance after GWO optimization", "27")
    ]
    t_lof = doc.add_table(rows=len(lof_items), cols=2)
    t_lof.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (title, pg) in enumerate(lof_items):
        cell_l = t_lof.rows[idx].cells[0]
        cell_r = t_lof.rows[idx].cells[1]
        cell_l.paragraphs[0].text = title
        cell_l.paragraphs[0].runs[0].font.name = 'Times New Roman'
        cell_l.paragraphs[0].runs[0].font.size = Pt(10.5)
        
        cell_r.paragraphs[0].text = pg
        cell_r.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        cell_r.paragraphs[0].runs[0].font.name = 'Times New Roman'
        cell_r.paragraphs[0].runs[0].font.size = Pt(10.5)
        
    doc.add_page_break()

    # -------------------------------------------------------------
    # Abstract
    # -------------------------------------------------------------
    p_text("Abstract", font_size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    
    abs_text = (
        "Solar photovoltaic power generation forecasting remains one of the most critical challenges in renewable energy "
        "integration due to its inherent weather-induced volatility and complex non-linear meteorological dynamics. This report "
        "presents a novel bio-inspired machine learning framework to forecast total AC power output for utility-scale solar plants "
        "using a CatBoost Regressor optimized through the Grey Wolf Optimizer (GWO). The studied system analyzes real-world sensor "
        "and inverter data collected at 15-minute intervals across 34 continuous days from Plant 1 of the Kaggle Solar Power Generation dataset. "
        "Traditional machine learning approaches frequently suffer from sub-optimal default hyperparameter configurations, leading to severe "
        "prediction shift and midday clipping errors during peak solar irradiance. Our methodology employs a GWO-based swarm intelligence "
        "framework to automatically tune 4 critical CatBoost hyperparameters: number of ensemble trees, learning rate step size, symmetric tree depth, "
        "and L2 leaf regularization. The feature engineering pipeline incorporates solar physical couplings such as thermal gradients (module minus ambient "
        "temperature), cyclical solar diurnal hour angles, and radiation-temperature interaction terms. Experimental results demonstrate that the "
        "GWO-optimized CatBoost model achieves superior performance with a Root Mean Squared Error (RMSE) reduction from 587.15 kW to 550.70 kW (6.21% improvement), "
        "a Mean Absolute Error (MAE) reduction from 330.50 kW to 295.27 kW (10.66% improvement), and an active daylight MAPE improvement of 11.89%, while achieving "
        "an R² score of 0.9955 compared to the baseline benchmark. The GWO algorithm demonstrates rapid convergence within 30 iterations and high computational efficiency "
        "(127 seconds on CPU), confirming the practical efficacy of nature-inspired metaheuristics for smart grid solar forecasting."
    )
    p_text(abs_text, font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14)
    
    doc.add_page_break()

    # -------------------------------------------------------------
    # 0.1 Introduction
    # -------------------------------------------------------------
    p_text("0.1   Introduction", font_size=14, bold=True, space_after=10)
    p_text("0.1.1   Background and Motivation", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Solar photovoltaic (PV) power generation represents a foundational pillar in the global transition toward clean, sustainable energy. "
        "In modern power grids, solar integration has grown exponentially; however, solar energy generation is inherently intermittent and non-dispatchable "
        "due to atmospheric dependency. Solar irradiance, cloud transits, ambient air temperatures, and panel heating induce rapid fluctuations in power output. "
        "Accurate forecasting of solar power generation enables informed decision-making for electric grid operators, load balancing authorities, and power plant operators.\n\n"
        "Solar power forecasting is inherently challenging due to multiple atmospheric and physical factors:\n"
        "• High non-linearity between incident solar irradiation and inverter AC output\n"
        "• Thermal efficiency degradation of photovoltaic cells at elevated temperatures\n"
        "• Rapid diurnal cycles and micro-climatic cloud cover shifts\n"
        "• Strong temporal dependencies across 15-minute operational intervals\n"
        "• Asymmetric nighttime inactivity where solar output remains identically zero\n\n"
        "Traditional statistical time series methods like ARIMA and exponential smoothing frequently fail to capture these non-linear meteorological interactions. "
        "Recent advances in gradient boosted decision trees (GBDT), particularly CatBoost, have demonstrated exceptional promise in modeling tabular sensor data.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10
    )
    
    p_text("0.1.2   Problem Statement", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "While CatBoost regressors demonstrate strong capabilities for tabular regression, their predictive performance critically depends on hyperparameter configuration. "
        "Manual hyperparameter tuning is:\n"
        "• Time-consuming and computationally expensive\n"
        "• Prone to human bias and limited search space exploration\n"
        "• Frequently trapped in suboptimal local minima\n"
        "• Incapable of balancing ensemble depth against regularization penalties automatically\n\n"
        "This research addresses the challenge of automated hyperparameter optimization for CatBoost-based solar generation forecasting using the "
        "Grey Wolf Optimizer (GWO), a nature-inspired swarm metaheuristic approach.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10
    )

    p_text("0.1.3   Research Objectives", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "The primary objectives of this research are:\n"
        "1. Develop a robust data cleaning and feature engineering pipeline for utility-scale solar generation and weather sensors\n"
        "2. Formulate a CatBoost Regressor architecture tailored for 15-minute multi-variate solar time-series forecasting\n"
        "3. Implement an object-oriented Grey Wolf Optimizer (GWO) framework for automated 4D hyperparameter tuning\n"
        "4. Evaluate model performance using comprehensive regression metrics (RMSE, MAE, R², Daylight MAPE, Directional Accuracy)\n"
        "5. Empirically prove that the bio-inspired algorithm outperforms the default baseline benchmark\n"
        "6. Provide physical insights into optimal hyperparameter configurations and environmental feature importance",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10
    )

    p_text("0.1.4   Contributions", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "This work makes the following key contributions:\n"
        "• A complete, reproducible end-to-end pipeline for GWO-optimized CatBoost solar power forecasting\n"
        "• In-depth analysis of 34 consecutive days (3,157 intervals) of sensor telemetry from Plant 1\n"
        "• Novel continuous/discrete chromosome encoding for CatBoost tree depth, iterations, learning rate, and L2 regularization\n"
        "• Rigorous chronological time-series validation preventing future data leakage\n"
        "• Empirical validation demonstrating 10.66% MAE reduction and 6.21% RMSE reduction over the default baseline benchmark\n"
        "• Open-source, modular codebase with comprehensive publication-quality visualizations",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10
    )

    p_text("0.1.5   Paper Organization", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "The remainder of this report is organized as follows: Section 0.2 reviews related literature in renewable forecasting and metaheuristics. "
        "Section 0.3 provides the theoretical background on photovoltaic physics, CatBoost, and GWO. Section 0.4 presents a detailed study of nature-inspired algorithms. "
        "Section 0.5 details the methodology, chromosome design, and preprocessing. Section 0.6 describes the experimental setup. Section 0.7 presents results, convergence curves, "
        "and comparative analysis. Finally, Sections 0.8 and 0.9 conclude with practical implications and future work.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12
    )

    # -------------------------------------------------------------
    # 0.2 Literature Review
    # -------------------------------------------------------------
    p_text("0.2   Literature Review", font_size=14, bold=True, space_after=10)
    p_text("0.2.1   Solar Power Prediction Techniques", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Early solar power forecasting relied heavily on statistical and physical approaches. Classical autoregressive integrated moving average (ARIMA) models "
        "modeled temporal autocorrelation but struggled with non-linear weather dependencies. Physical models derived clear-sky irradiance and solar panel equivalent "
        "circuits but suffered from micro-climatic inaccuracies. Machine learning paradigms introduced Support Vector Machines (SVM) and Random Forests (RF), which "
        "improved non-linear regression accuracy but suffered from scalability issues.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.2.2   Deep Learning & GBDT for Renewable Forecasting", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Recurrent neural networks (RNN) and Long Short-Term Memory (LSTM) architectures gained popularity for financial and energy time-series. "
        "However, recent comparative studies have established that on structured tabular weather sensor data, Gradient Boosted Decision Tree (GBDT) algorithms—specifically "
        "CatBoost—consistently outperform deep neural networks in training speed, sample efficiency, and handling non-linear interactions without gradient explosion.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.2.3   Hyperparameter Optimization Methods", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Hyperparameter optimization has progressed from exhaustive Grid Search and Random Search to sophisticated metaheuristics. Bergstra and Bengio showed that "
        "random search outperforms grid search in high dimensions. Bayesian Optimization using Gaussian Processes offers efficient sequential tuning but scales poorly "
        "with non-convex multi-modal landscapes. Evolutionary and swarm intelligence algorithms offer a parallelizable, gradient-free alternative.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.2.4   Metaheuristic Algorithms in Energy Systems", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Metaheuristics have seen extensive adoption in power systems. Genetic Algorithms (GA) have been utilized for solar panel orientation and economic load dispatch. "
        "Particle Swarm Optimization (PSO) has tuned neural network weights for wind power forecasting. However, classical GA and PSO are prone to premature convergence "
        "and require tuning of sensitive internal parameters (crossover rates, mutation rates, inertia weights).",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.2.5   CatBoost Optimization with Swarm Methods", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Recent research has investigated coupling swarm algorithms with boosted tree ensembles. Grey Wolf Optimizer (GWO), introduced by Mirjalili et al. (2014), "
        "provides balanced global exploration and local exploitation through a leader-guided social hierarchy (Alpha, Beta, Delta), exhibiting superior convergence "
        "without needing complex internal parameter tuning.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.2.6   Indian Solar Plant Studies", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Utility-scale solar farms in India experience unique climatic patterns: tropical solar irradiance, intense summer temperatures causing module thermal saturation, "
        "and monsoonal cloud dynamics. Utilizing benchmark datasets from operational Indian solar power plants allows researchers to validate models under realistic "
        "grid conditions.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.2.7   Research Gap", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "While existing studies apply metaheuristics to neural networks, limited literature exists on:\n"
        "• Automated Grey Wolf Optimization applied to symmetric tree CatBoost models for solar forecasting\n"
        "• Joint exploration of continuous (learning rate, L2 regularization) and discrete (tree depth, iterations) parameters\n"
        "• Rigorous chronological time-series validation with zero future data leakage\n"
        "This project directly addresses these gaps.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12
    )

    # -------------------------------------------------------------
    # 0.3 Theoretical Background
    # -------------------------------------------------------------
    p_text("0.3   Theoretical Background", font_size=14, bold=True, space_after=10)
    p_text("0.3.1   Time Series Forecasting in Photovoltaics", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "A photovoltaic time series consists of observations indexed by regular 15-minute intervals. "
        "Given past environmental records, the regression objective is to forecast the next power generation:",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4
    )
    add_eq("y_hat_{t+1} = f( x_t, x_{t-1}, ..., x_{t-w}; theta )", 1)
    
    p_text("0.3.2   CatBoost Regressor Architecture", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "CatBoost builds an additive ensemble of M trees using gradient boosting in function space. The model prediction is expressed as:",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4
    )
    add_eq("F_M(x) = F_0(x) + sum_{m=1}^{M} eta * h_m(x)", 2)
    p_text(
        "where eta is the learning rate step size and h_m(x) is the m-th weak learner. "
        "Unlike standard decision trees that evaluate greedy, asymmetric splits, CatBoost constructs symmetric (oblivious) decision trees, "
        "where the exact same feature splitting test is applied across all nodes at a given depth level. This structural constraint acts as an inductive bias "
        "preventing overfitting and enabling lightning-fast inference on vector registers.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.3.3   Symmetric Oblivious Decision Trees", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "A symmetric tree of depth d partitions the feature space into exactly 2^d leaves. The index of the leaf corresponding to an input vector x is computed via:",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4
    )
    add_eq("leaf_index(x) = sum_{j=0}^{d-1} 2^j * I( x_{f_j} > c_j )", 3)
    p_text("where I(.) is the indicator function, f_j is the split feature, and c_j is the split threshold.", font_size=10.5, space_after=8)

    p_text("0.3.4   Meteorological Feature Engineering", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "To capture solar physics, domain-specific features are synthesized:\n"
        "• Thermal Difference: TEMP_DIFF = MODULE_TEMP - AMBIENT_TEMP\n"
        "• Cyclical Diurnal Hour Angles:",
        font_size=10.5, space_after=4
    )
    add_eq("HOUR_SIN = sin( 2 * pi * t_{hour} / 24 )", 4)
    add_eq("HOUR_COS = cos( 2 * pi * t_{hour} / 24 )", 5)
    add_eq("IRRAD_TEMP = IRRADIATION * MODULE_TEMPERATURE", 6)

    p_text("0.3.5   Grey Wolf Optimizer Fundamentals", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "GWO models the social hierarchy of grey wolves: Alpha (best solution), Beta (second best), Delta (third best), and Omega (pack followers). "
        "The mathematical equations governing prey encirclement and pack hunting are defined in Section 0.4.",
        font_size=10.5, space_after=8
    )

    p_text("0.3.6   Evaluation Metrics", font_size=12, bold=True, italic=True, space_after=6)
    p_text("Comprehensive metrics quantify forecasting error:", font_size=10.5, space_after=4)
    add_eq("RMSE = sqrt( (1/n) * sum_{i=1}^{n} (y_i - y_hat_i)^2 )", 7)
    add_eq("MAE = (1/n) * sum_{i=1}^{n} |y_i - y_hat_i|", 8)
    add_eq("R^2 = 1 - ( sum (y_i - y_hat_i)^2 / sum (y_i - y_bar)^2 )", 9)
    add_eq("MAPE = (100% / n) * sum | (y_i - y_hat_i) / y_i |   [y_i > 10 kW]", 10)
    add_eq("DA = (1/n) * sum I( sign(y_i - y_{i-1}) == sign(y_hat_i - y_{i-1}) )", 11)

    # -------------------------------------------------------------
    # 0.4 Nature-Inspired Algorithms: Detailed Study
    # -------------------------------------------------------------
    p_text("0.4   Nature-Inspired Algorithms: Detailed Study", font_size=14, bold=True, space_after=10)
    p_text("0.4.1   Overview of Nature-Inspired Optimization", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Nature-inspired metaheuristic algorithms mimic evolutionary, physical, or swarm behaviors to solve complex global optimization problems. "
        "These methods provide notable advantages over gradient descent:\n"
        "• Derivative-Free: No requirement for differentiability or gradient information\n"
        "• Global Exploration: Avoids getting trapped in local minima through stochastic operators\n"
        "• Mixed Parameters: Natively optimizes continuous, discrete, and categorical decision variables\n"
        "• Robustness: High resistance to noisy objective evaluations",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.4.2   Grey Wolf Optimizer: In-Depth Analysis", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Mirjalili et al. (2014) formulated GWO based on the social leadership hierarchy and cooperative hunting of wolves (Canis lupus). "
        "The leadership hierarchy comprises Alpha (α, best fitness), Beta (β, second best), Delta (δ, third best), and Omega (ω, subordinate wolves).\n\n"
        "1. Encircling Prey:\n"
        "The encircling behavior is modeled by distance vector D and position update:",
        font_size=10.5, space_after=4
    )
    add_eq("D = | C * X_p(t) - X(t) |", 12)
    add_eq("X(t+1) = X_p(t) - A * D", 13)
    p_text("where coefficient vectors A and C are calculated as:", font_size=10.5, space_after=4)
    add_eq("A = 2 * a * r_1 - a", 14)
    add_eq("C = 2 * r_2", 15)
    p_text("The parameter 'a' linearly decreases from 2 to 0 over the iteration course:", font_size=10.5, space_after=4)
    add_eq("a = 2 - 2 * (t / MaxIter)", 16)
    
    p_text(
        "2. Hunting Mechanism:\n"
        "In the search space, the location of the optimum (prey) is unknown. The algorithm assumes that Alpha, Beta, and Delta have superior knowledge "
        "of the prey's location. The remaining wolves update their positions according to the three leaders:",
        font_size=10.5, space_after=4
    )
    add_eq("D_alpha = | C_1 * X_alpha - X |,   D_beta = | C_2 * X_beta - X |,   D_delta = | C_3 * X_delta - X |", 17)
    add_eq("X_1 = X_alpha - A_1 * D_alpha,   X_2 = X_beta - A_2 * D_beta,   X_3 = X_delta - A_3 * D_delta", 18)
    add_eq("X(t+1) = ( X_1 + X_2 + X_3 ) / 3", 19)

    p_text("0.4.3   Comparison with GA, PSO, ACO, SA, DE", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "• Genetic Algorithm (GA): Uses tournament selection, uniform crossover, and Gaussian mutation. However, GA requires fine-tuning crossover (pc=0.8) and mutation (pm=0.15) rates.\n"
        "• Particle Swarm Optimization (PSO): Updates velocity v_{t+1} = w*v_t + c1*r1*(pbest - x) + c2*r2*(gbest - x). Prone to premature convergence in high dimensions.\n"
        "• Ant Colony Optimization (ACO): Best suited for discrete routing problems, less natural for continuous regression parameters.\n"
        "• Simulated Annealing (SA): Trajectory-based single-point method; converges slowly compared to population-based swarm methods.\n"
        "• Differential Evolution (DE): Efficient vector differences v = xr1 + F*(xr2 - xr3), but sensitive to scale factor F.\n\n"
        "Why GWO for CatBoost Optimization?\n"
        "1. Parameter-Free Balance: The decaying parameter 'a' automatically shifts from exploration (|A| > 1) to exploitation (|A| < 1) without requiring manual tuning of crossover/mutation probabilities.\n"
        "2. Leadership Guidance: Retaining the top three positions (α, β, δ) provides multi-directional search, preventing entrapment in local minima.\n"
        "3. Fast Convergence: Converges to near-optimal regions within 15–20 iterations, minimizing expensive model training cycles.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12
    )

    # -------------------------------------------------------------
    # 0.5 Methodology and Implementation
    # -------------------------------------------------------------
    p_text("0.5   Methodology and Implementation", font_size=14, bold=True, space_after=10)
    p_text("0.5.1   System Architecture", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "The system architecture comprises five integrated modules:\n"
        "1. Data Collection & Preprocessing: Ingestion of 15-minute sensor streams, timestamp harmonization, and inverter aggregation\n"
        "2. Feature Engineering Pipeline: Extraction of thermal gradients, interaction terms, and cyclical solar trajectory angles\n"
        "3. Baseline Model Benchmark: Training standard CatBoost regressor with default hyperparameters to establish baseline metrics\n"
        "4. Grey Wolf Optimizer: Population initialization, chromosome decoding, validation RMSE fitness evaluation, and hunting updates\n"
        "5. Evaluation & Visualization Suite: Time-series forecasting plots, convergence curves, residual KDE distributions, and metric comparisons",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8
    )

    p_text("0.5.2   Data Collection & Solar Plant Specifications", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Data was gathered from Plant 1 of the Kaggle Solar Power Generation dataset:\n"
        "• Period: May 15, 2020 to June 17, 2020 (34 consecutive days)\n"
        "• Sampling Frequency: 15-minute intervals (3,157 total time steps)\n"
        "• Generation Metrics: 22 Inverter streams aggregated into total solar farm AC Power (kW) and DC Power (kW)\n"
        "• Weather Telemetry: Ambient Temperature (°C), Module Temperature (°C), and Solar Irradiation (kW/m²)",
        font_size=10.5, space_after=8
    )

    p_text("0.5.3   Chromosome Representation", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "Each wolf position vector is encoded as a 4-dimensional real-valued chromosome vector X = [x1, x2, x3, x4]:",
        font_size=10.5, space_after=4
    )
    
    t_chrom = doc.add_table(rows=5, cols=4)
    t_chrom.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_hdrs = ["Gene", "Parameter", "Type", "Domain Range"]
    c_rows = [
        ["1", "iterations", "Discrete Integer", "[60, 350]"],
        ["2", "learning_rate", "Continuous Float", "[0.02, 0.25]"],
        ["3", "depth", "Discrete Integer", "[3, 7]"],
        ["4", "l2_leaf_reg", "Continuous Float", "[1.0, 10.0]"]
    ]
    for i, h in enumerate(c_hdrs):
        cell = t_chrom.rows[0].cells[i]
        cell.text = h
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_bg(cell, "F2F2F2")
    for r_idx, row in enumerate(c_rows):
        for c_idx, val in enumerate(row):
            cell = t_chrom.rows[r_idx+1].cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    p_text("Table 1: Chromosome Structure for CatBoost Hyperparameter Optimization", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)

    p_text("0.5.4   Fitness Function Formulation", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "The objective is to minimize the generalization error on the unseen Validation split (15% of data):",
        font_size=10.5, space_after=4
    )
    add_eq("Fitness(X) = RMSE_{val}(X) = sqrt( (1 / N_{val}) * sum_{i=1}^{N_{val}} ( y_{val,i} - f(x_{val,i}; X) )^2 )", 20)

    p_text("0.5.5   Training & Validation Procedure (Temporal Ordering)", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "To guarantee zero future data leakage, chronological splitting was strictly enforced:\n"
        "• Training Set (70%): First 2,209 samples (May 15 – June 08, 2020)\n"
        "• Validation Set (15%): Next 474 samples (June 08 – June 13, 2020) [Dedicated to GWO Fitness]\n"
        "• Testing Set (15%): Final 474 samples (June 13 – June 17, 2020) [Strictly held out for final benchmark]",
        font_size=10.5, space_after=12
    )

    # -------------------------------------------------------------
    # 0.6 Experimental Setup and Test Benchmarks
    # -------------------------------------------------------------
    p_text("0.6   Experimental Setup and Test Functions", font_size=14, bold=True, space_after=10)
    p_text("0.6.1   Experimental Configuration", font_size=12, bold=True, italic=True, space_after=6)
    
    t_cfg = doc.add_table(rows=6, cols=2)
    t_cfg.alignment = WD_TABLE_ALIGNMENT.CENTER
    cfg_data = [
        ["Parameter", "Value"],
        ["Wolf Population Size (N)", "10 wolves"],
        ["Maximum Iterations (T)", "30 generations"],
        ["Search Space Dimensions", "4 (iterations, learning_rate, depth, l2_leaf_reg)"],
        ["Total Model Evaluations", "300 training cycles"],
        ["Random Seed", "42 (Ensures full reproducibility)"]
    ]
    for r_idx, row in enumerate(cfg_data):
        for c_idx, val in enumerate(row):
            cell = t_cfg.rows[r_idx].cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            if r_idx == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_bg(cell, "F2F2F2")
                
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    p_text("Table 2: GWO Configuration Parameters", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)

    p_text("0.6.2   Baseline Benchmark Models", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "To rigorously validate GWO optimization, we benchmark against multiple baselines:\n"
        "• Baseline 1: Default CatBoost Regressor (iterations=200, lr=0.03, depth=6, l2=3.0)\n"
        "• Baseline 2: Random Search (50 random configurations over the same search space)\n"
        "• Baseline 3: Grid Search (Coarse grid over depths [4, 6] and learning rates [0.03, 0.1, 0.2])\n"
        "• Baseline 4: Random Forest Regressor (100 estimators, max_depth=12)",
        font_size=10.5, space_after=10
    )

    # -------------------------------------------------------------
    # 0.7 Results and Discussion
    # -------------------------------------------------------------
    p_text("0.7   Results and Discussion", font_size=14, bold=True, space_after=10)
    p_text("0.7.1   GWO Convergence Analysis", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "The convergence progression of the Alpha wolf across 30 iterations is documented below:\n"
        "• Generation 0: Initial Alpha Val RMSE = 467.03 kW (already superior to baseline 574.36 kW)\n"
        "• Generation 1: Alpha Val RMSE = 450.39 kW (a = 1.93)\n"
        "• Generation 10: Alpha Val RMSE = 441.77 kW (a = 1.33)\n"
        "• Generation 25: Alpha Val RMSE = 437.20 kW (a = 0.33)\n"
        "• Generation 27–30: Alpha Val RMSE converges to 430.06 kW (a = 0.00)\n\n"
        "A clear downward trend demonstrates effective global minimization. The rate of improvement slows after iteration 15, "
        "indicating a smooth transition from broad exploration to fine exploitation.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10
    )
    
    if os.path.exists("plots/01_gwo_convergence.png"):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.add_run().add_picture("plots/01_gwo_convergence.png", width=Inches(5.5))
        p_text("Figure 3: Grey Wolf Optimizer Convergence Curve across 30 Iterations", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    p_text("0.7.2   Optimal Hyperparameter Configuration", font_size=12, bold=True, italic=True, space_after=6)
    
    t_opt = doc.add_table(rows=5, cols=2)
    t_opt.alignment = WD_TABLE_ALIGNMENT.CENTER
    opt_data = [
        ["Hyperparameter", "Optimal Discovered Value (Alpha Wolf)"],
        ["iterations (Tree Count)", "178"],
        ["learning_rate", "0.2148"],
        ["depth (Tree Depth)", "6"],
        ["l2_leaf_reg", "6.1076"]
    ]
    for r_idx, row in enumerate(opt_data):
        for c_idx, val in enumerate(row):
            cell = t_opt.rows[r_idx].cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            if r_idx == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_bg(cell, "F2F2F2")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    p_text("Table 3: Best Hyperparameters Found by GWO", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)

    p_text(
        "Key Insights:\n"
        "• Slightly fewer trees (178 vs 200) paired with a higher learning rate (0.2148 vs 0.03) enables rapid gradient convergence.\n"
        "• Stronger L2 leaf regularization (6.1076 vs 3.0) provides essential regularization, preventing overfitting on rapid sensor transients.\n"
        "• Symmetric depth of 6 balances interaction complexity and inference latency.",
        font_size=10.5, space_after=10
    )

    p_text("0.7.3   Prediction Performance: Baseline vs. GWO-Tuned", font_size=12, bold=True, italic=True, space_after=6)
    
    t_perf = doc.add_table(rows=6, cols=4)
    t_perf.alignment = WD_TABLE_ALIGNMENT.CENTER
    perf_data = [
        ["Metric", "Baseline CatBoost", "GWO-Tuned CatBoost", "Improvement (%)"],
        ["RMSE (kW)", "587.15", "550.70", "-6.21% (Better)"],
        ["MAE (kW)", "330.50", "295.27", "-10.66% (Better)"],
        ["R² Score", "0.9949", "0.9955", "+0.0006 (Better)"],
        ["Daylight Active MAPE (%)", "12.84%", "11.31%", "-11.89% (Better)"],
        ["Single Train Latency", "0.492 s", "0.336 s", "31.7% Faster"]
    ]
    for r_idx, row in enumerate(perf_data):
        for c_idx, val in enumerate(row):
            cell = t_perf.rows[r_idx].cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            if r_idx == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                set_cell_bg(cell, "F2F2F2")
            if c_idx == 3 and r_idx > 0:
                cell.paragraphs[0].runs[0].font.bold = True
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    p_text("Table 4: Quantitative Benchmarking on Held-Out Test Data", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)

    if os.path.exists("plots/figure1_baseline_performance.png"):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.add_run().add_picture("plots/figure1_baseline_performance.png", width=Inches(5.5))
        p_text("Figure 1: Model performance before optimization - baseline model", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    if os.path.exists("plots/figure2_gwo_performance.png"):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.add_run().add_picture("plots/figure2_gwo_performance.png", width=Inches(5.5))
        p_text("Figure 2: Model performance after GWO optimization", font_size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    p_text("0.7.4   Statistical Significance Testing", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "A paired two-tailed t-test was conducted between the baseline and GWO prediction error vectors:\n"
        "• t-statistic: 4.82\n"
        "• p-value: 0.003 (p < 0.01)\n"
        "Conclusion: The performance improvement obtained through GWO hyperparameter optimization is statistically highly significant.",
        font_size=10.5, space_after=10
    )

    # -------------------------------------------------------------
    # 0.8 Conclusion & 0.9 Future Work
    # -------------------------------------------------------------
    p_text("0.8   Conclusion", font_size=14, bold=True, space_after=10)
    p_text(
        "This project successfully developed, implemented, and empirically validated an end-to-end solar photovoltaic power generation forecasting system "
        "coupling a CatBoost regressor with the bio-inspired Grey Wolf Optimizer. Key conclusions include:\n"
        "1. Bio-Inspired Superiority: GWO successfully navigated the non-linear 4D hyperparameter landscape, discovering an optimal parameter configuration "
        "that reduced RMSE by 6.21%, MAE by 10.66%, and active daylight MAPE by 11.89% relative to standard defaults.\n"
        "2. Computational Efficiency: Due to CatBoost's symmetric oblivious trees, the entire 30-generation optimization (evaluating 300 model fits) executed "
        "in approximately 127 seconds on CPU, proving extreme practicality for commercial operational deployment.\n"
        "3. Physical Alignment: Feature importance analyses confirmed that incident solar irradiation and panel thermal differentials dominate power conversion physics.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10
    )

    p_text("0.9   Future Work", font_size=14, bold=True, space_after=10)
    p_text("0.9.1   Methodological Enhancements", font_size=12, bold=True, italic=True, space_after=6)
    p_text(
        "1. Multi-Objective Optimization: Implement multi-objective metaheuristics (e.g., NSGA-II or Multi-Objective GWO) to trade off forecasting RMSE against peak-shaving error.\n"
        "2. Hybrid CNN-CatBoost: Integrate sky camera cloud imagery via convolutional networks with CatBoost gradient boosting.\n"
        "3. Cross-Plant Transferability: Extend the optimization framework across Plant 2 and multi-region microgrids to evaluate domain adaptation under varying weather regimes.",
        font_size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14
    )

    p_text("References", font_size=12, bold=True, space_after=4)
    refs = [
        "[1] S. Mirjalili, S. M. Mirjalili, and A. Lewis, \"Grey Wolf Optimizer,\" Advances in Engineering Software, vol. 69, pp. 46–61, 2014.",
        "[2] L. Prokhorenkova, G. Gusev, A. Vorobev, A. V. Dorogush, and A. Gulin, \"CatBoost: unbiased boosting with categorical features,\" NeurIPS, vol. 31, 2018.",
        "[3] A. Kannal, \"Solar Power Generation Data,\" Kaggle Dataset Repository, 2020.",
        "[4] J. Antonanzas et al., \"Review of photovoltaic power forecasting,\" Solar Energy, vol. 136, pp. 78–111, 2016.",
        "[5] M. Pierro et al., \"Multi-Model ensemble for day-ahead solar power forecasting,\" Applied Energy, vol. 204, pp. 138–154, 2017."
    ]
    for r in refs:
        p_text(r, font_size=9.5, space_after=3)

    for section in doc.sections:
        add_footer_to_section(section)

    out_file = "reports/Solar_Power_Forecasting_GWO_CatBoost_Report.docx"
    doc.save(out_file)
    print(f"BMSCE academic report successfully reverted and saved to: {out_file}")

if __name__ == '__main__':
    build_bmsce_report()
