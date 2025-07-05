# Bollywood Bias Buster

## Overview

**Bollywood Bias Buster** is an AI-powered tool that detects gender stereotypes in Bollywood movie scripts. It helps writers, directors, and producers identify and address bias in their stories, making Indian cinema more inclusive and progressive.

---

## What Does It Do?

- **Finds gender stereotypes** in movie scripts (both English and Hindi written in English letters).
- **Quantifies bias** at the character and script level.
- **Suggests bias-free rewrites** for flagged dialogues.
- **Generates clear, visual feedback reports** for creators.

---

## Why Is This Important?

Gender stereotypes in films shape how society views men and women. By highlighting and fixing these biases, we can help create stories that empower everyone.

---

## How Does It Work?

1. **Data Ingestion:**  
   - Downloads and extracts Bollywood scripts.
   - Converts PDF scripts to plain text.

2. **Stereotype Detection:**  
   - Splits scripts into dialogue blocks.
   - Uses smart keyword matching (in both English and Romanized Hindi) to flag:
     - **Relationship-based stereotypes** (e.g., “beti”, “wife”, “bahu”)
     - **Profession-based stereotypes** (e.g., “kaam”, “job”, “engineer”)

3. **Bias Quantification:**  
   - Counts and visualizes the number of biased dialogues by gender and type.

4. **Remediation:**  
   - Suggests simple, bias-free rewrites for flagged dialogues.

5. **Reporting:**  
   - Outputs results as CSV, JSON, and visual charts.
   - Provides a sample feedback report for scriptwriters.

---

## How Was It Evaluated?

- **Manual Annotation:**  
  20 dialogues were manually labeled for stereotypes.
- **Model Performance:**  
  - **Precision:** 0.67 (when the model flags a stereotype, it’s correct 67% of the time)
  - **Recall:** 0.80 (the model finds 80% of all actual stereotypes)
  - **F1 Score:** 0.73 (overall accuracy)
  - ![image](https://github.com/user-attachments/assets/6839b1f5-3d1e-440a-9ab5-a3635da56bed)


---

## How To Use

1. **Install requirements:**  
   ```bash
   pip install -r Requirements.txt
   ```

2. **Run the pipeline:**  
   ```bash
   python main.py
   ```

3. **See the results:**  
   - Check the `outputs/` folder for:
     - `bias_report.json` and `bias_report.csv` (detailed results)
     - `bias_chart.png` (visual summary)
     - `manual_annotations.csv` (your annotated test set)
     - `model_predictions.csv` (model’s predictions)

---

## Bias Taxonomy

- **Relationship-based:**  
  Dialogues that define women by their relationships (e.g., “beti”, “wife”, “bahu”).
- **Profession-based:**  
  Dialogues that mention jobs or roles, often highlighting a gender gap.

---

## AI Strategy

- **Keyword-based detection** for both English and Romanized Hindi.
- **Gender inference** from context and keywords.
- **Modular pipeline** for easy extension (e.g., adding LLMs or more advanced NLP).

---

## Validation Approach

- **Manual annotation** of a sample of dialogues.
- **Comparison of model predictions** to human labels using precision, recall, and F1 score.

---

## Sample Output

![image](https://github.com/user-attachments/assets/be2b5d83-ec0c-4e32-a434-b1670f36812a)

---

## Acknowledgements

- Dataset: [BollywoodData/Bollywood-Data](https://github.com/BollywoodData/Bollywood-Data)
- Inspired by the need for more inclusive storytelling in Indian cinema.


---

**Let’s make Bollywood more bias-free, one script at a time!**
