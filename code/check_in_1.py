
# %%
import pandas as pd
import matplotlib.pyplot as plt

# Load training metadata only
metadata = pd.read_csv(r"C:\Users\15712\OneDrive - University of Virginia\School\OneDrive - University of Virginia\Comp Mod 4\Module-4-Cancer_breckley_chen\data\TRAINING_SET_GSE62944_metadata.csv")

# Basic overview
print("Metadata shape:", metadata.shape)
print("\nColumns:")
print(metadata.columns.tolist())

print("\nFirst 5 rows:")
print(metadata.head())

print("\nMissing values by column:")
print(metadata.isna().sum())

# Focus on breast cancer
brca_metadata = metadata[metadata["cancer_type"] == "BRCA"].copy()

print("\nBRCA metadata shape:", brca_metadata.shape)

# Convert age to numeric
brca_metadata["age_at_diagnosis"] = pd.to_numeric(
    brca_metadata["age_at_diagnosis"], errors="coerce"
)

print("\nBRCA gender counts:")
print(brca_metadata["gender"].value_counts(dropna=False))

print("\nBRCA tumor stage counts:")
print(brca_metadata["ajcc_pathologic_tumor_stage"].value_counts(dropna=False))

print("\nBRCA tumor status counts:")
print(brca_metadata["tumor_status"].value_counts(dropna=False))

print("\nBRCA average age at diagnosis:")
print(brca_metadata["age_at_diagnosis"].mean())

print("\nBRCA survival summary:")
survival_cols = ["OS", "OS.time", "DSS", "DSS.time", "DFI", "DFI.time", "PFI", "PFI.time"]
for col in survival_cols:
    if col in brca_metadata.columns:
        print(f"\n{col}")
        print(brca_metadata[col].describe())

# Simplify tumor stage
def simplify_stage(stage):
    if pd.isna(stage):
        return pd.NA
    stage = str(stage).upper()
    if "STAGE I" in stage and "II" not in stage and "III" not in stage and "IV" not in stage:
        return "Stage I"
    elif "STAGE II" in stage:
        return "Stage II"
    elif "STAGE III" in stage:
        return "Stage III"
    elif "STAGE IV" in stage:
        return "Stage IV"
    else:
        return pd.NA

brca_metadata["stage_simple"] = brca_metadata["ajcc_pathologic_tumor_stage"].apply(simplify_stage)

print("\nSimplified BRCA stage counts:")
print(brca_metadata["stage_simple"].value_counts(dropna=False))

# Plot 1: tumor stage distribution
plt.figure(figsize=(8, 5))
brca_metadata["stage_simple"].value_counts().plot(kind="bar")
plt.title("Breast Cancer Sample Counts by Tumor Stage")
plt.xlabel("Tumor Stage")
plt.ylabel("Number of Samples")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: age at diagnosis distribution
plt.figure(figsize=(8, 5))
brca_metadata["age_at_diagnosis"].dropna().plot(kind="hist", bins=20)
plt.title("Age at Diagnosis Distribution in BRCA Samples")
plt.xlabel("Age at Diagnosis")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Plot 3: tumor status distribution
plt.figure(figsize=(8, 5))
brca_metadata["tumor_status"].value_counts().plot(kind="bar")
plt.title("Tumor Status in BRCA Samples")
plt.xlabel("Tumor Status")
plt.ylabel("Number of Samples")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# %%
