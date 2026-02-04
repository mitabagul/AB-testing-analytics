# A/B Testing Analytics

This repository demonstrates an end-to-end A/B testing analysis for a product experiment, covering experiment design, metric computation using SQL, and statistical significance testing using Python.

The goal is to showcase how data is used to make **product decisions**, not just compute metrics.

---

## Objective

Evaluate whether a new product feature improves **user conversion** compared to the existing experience.

---

## Experiment Design

- Users are randomly assigned to one of two groups:
  - **Control (A):** Existing product experience
  - **Treatment (B):** New product feature
- Each user appears in **only one group**
- The experiment compares user behavior across the two groups

---

## Primary Metric

### Conversion Rate

Conversion Rate = Converted Users/Total Users


Where:
- `converted = 1` → user completed the desired action
- `converted = 0` → user did not convert

This metric directly reflects product success.

---

## Hypothesis

- **Null Hypothesis (H₀):**  
  There is no difference in conversion rate between the control and treatment groups.

- **Alternative Hypothesis (H₁):**  
  The treatment group has a higher conversion rate than the control group.

---

## Dataset

The dataset contains user-level experiment data with group assignment and conversion outcome.

**Columns**
- `user_id`: Unique user identifier
- `group_name`: `control` or `treatment`
- `converted`: 1 if user converted, 0 otherwise

Data is stored in:
data/ab_test_data.csv

---

## Metrics Computation (SQL)

Key experiment metrics are computed using SQL to mirror how analysis would be done in a data warehouse.

Metrics include:
- Total users per group
- Converted users per group
- Conversion rate per group

SQL logic is available in:
sql/ab_test_metrics.sql

---

## Statistical Analysis (Python)

Statistical significance is evaluated using a **two-sample proportion z-test**, which is appropriate for binary outcomes such as conversion.

The analysis is implemented in Python using:
- `pandas`
- `numpy`
- `statsmodels`

Analysis script:
analysis/ab_test_analysis.py

---

## Results

| Group      | Conversion Rate |
|------------|-----------------|
| Control    | **30%** |
| Treatment  | **70%** |

- **One-sided p-value (Treatment > Control):** `0.0368`
- **Two-sided p-value:** `0.0736`

---

## Interpretation

- The treatment group shows a **higher conversion rate** than the control group.
- Using a **one-sided test** (pre-declared hypothesis that treatment improves conversion), the result is **statistically significant at α = 0.05**.
- This indicates the observed lift is unlikely to be due to random chance.

---

## Conclusion & Recommendation

The treatment feature demonstrates a meaningful and statistically significant improvement in user conversion.

**Recommendation:**  
Roll out the treatment feature to all users.

---

## Reproducibility

Project dependencies are listed in:
requirements.txt

To reproduce the analysis:
```bash
pip install -r requirements.txt
python analysis/ab_test_analysis.py
```
---

## Results

- **X (Control Conversion Rate):** 30%  
- **Y (Treatment Conversion Rate):** 70%  
- **Absolute Lift:** +40 percentage points  

- **Z (Statistical Significance):**
  - One-sided p-value (Treatment > Control): **0.0368**
  - Two-sided p-value: **0.0736**

---

## Interpretation

- The treatment group shows a substantially higher conversion rate than the control group.
- Using a **one-sided hypothesis test** (pre-declared assumption that the treatment improves conversion),
  the result is **statistically significant at α = 0.05**.
- This suggests the observed lift is unlikely to be due to random chance.

---

## Conclusion & Recommendation

The treatment feature demonstrates a meaningful and statistically significant improvement in user conversion.

**Recommendation:**  
Roll out the treatment feature to all users.

