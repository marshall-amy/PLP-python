from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
import matplotlib.pyplot as plt

# Load dataset
dataset = CompasDataset()

# Split by protected attribute (race)
privileged = [{'race': 1}]   # Caucasian
unprivileged = [{'race': 0}] # African-American

# Compute initial metrics
metric = BinaryLabelDatasetMetric(dataset, privileged_groups=privileged, unprivileged_groups=unprivileged)

print("Mean difference:", metric.mean_difference())
print("Disparate impact:", metric.disparate_impact())

# Apply reweighing to reduce bias
RW = Reweighing(unprivileged_groups=unprivileged,
                privileged_groups=privileged)
dataset_transformed = RW.fit_transform(dataset)

metric_rw = BinaryLabelDatasetMetric(dataset_transformed, privileged, unprivileged)
print("After Reweighing - Disparate impact:", metric_rw.disparate_impact())

# Visualization example
plt.bar(['Before', 'After'], [metric.disparate_impact(), metric_rw.disparate_impact()])
plt.title('Disparate Impact Before and After Mitigation')
plt.ylabel('Disparate Impact Ratio')
plt.show()
