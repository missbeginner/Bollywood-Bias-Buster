import json
import pandas as pd
import matplotlib.pyplot as plt
import os


def save_reports(results, bias_stats, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    # Save CSV
    pd.DataFrame(results).to_csv(os.path.join(output_dir, "bias_report.csv"), index=False)

    # Save JSON
    with open(os.path.join(output_dir, "bias_report.json"), "w") as f:
        json.dump(results, f, indent=2)

    # Chart
    labels = list(bias_stats.keys())
    values = list(bias_stats.values())
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color='teal')
    plt.title("Bias Score by Gender")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "bias_chart.png"))