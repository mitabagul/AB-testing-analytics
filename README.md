# A/B Testing Analytics

This repository demonstrates an end-to-end A/B testing analysis for a product experiment.

## Objective
Evaluate whether a new product feature improves user conversion compared to the existing experience.

## Experiment Design
- Users are randomly assigned to Control (A) or Treatment (B)
- Each user belongs to only one group
- The experiment measures behavioral differences between the two groups

## Primary Metric
**Conversion Rate**

Conversion Rate = Converted Users / Total Users

## Hypothesis
- **Null Hypothesis (H₀):** There is no difference in conversion rate between control and treatment.
- **Alternative Hypothesis (H₁):** The treatment group has a higher conversion rate than the control group.

## Dataset
The dataset contains user-level experiment data with group assignment and conversion outcome.

**Columns**
- `user_id`: unique user identifier
- `group_name`: control or treatment
- `converted`: 1 if user converted, 0 otherwise
