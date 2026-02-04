import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Load data
df = pd.read_csv("data/ab_test_data.csv")

# Basic summary
summary = (
    df.groupby("group_name")
      .agg(total_users=("user_id", "count"),
           conversions=("converted", "sum"))
)

summary["conversion_rate"] = summary["conversions"] / summary["total_users"]

print("\n=== Group Summary ===")
print(summary)

# Two-sample proportion z-test
successes = summary["conversions"].values
samples = summary["total_users"].values

z_stat, p_value_two_sided = proportions_ztest(successes, samples, alternative="two-sided")
z_stat_one, p_value_one_sided = proportions_ztest(successes, samples, alternative="larger")

print("\n=== Statistical Test (Proportions Z-test) ===")
print(f"Z-stat (two-sided): {z_stat:.4f}, p-value (two-sided): {p_value_two_sided:.6f}")
print(f"Z-stat (one-sided, treatment > control): {z_stat_one:.4f}, p-value (one-sided): {p_value_one_sided:.6f}")

# Simple conclusion helper
alpha = 0.05
print("\n=== Conclusion ===")
if p_value_two_sided < alpha:
    print("Result is statistically significant at alpha=0.05 (two-sided).")
else:
    print("Result is NOT statistically significant at alpha=0.05 (two-sided).")

print("\nNote: Use one-sided p-value only if the experiment hypothesis was pre-declared as treatment > control.")
