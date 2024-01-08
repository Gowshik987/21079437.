# Loading Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
STUDENT_NAME = "Gowshik Naidu Thota"
STUDENT_ID = "21079437"

# Loading the breast cancer dataset
data = pd.read_csv('data.csv')

# Defining the figure size and aspect ratio
fig = plt.figure(figsize=(24, 14))
gs = fig.add_gridspec(nrows=10, ncols=8, width_ratios=[1,1,1,1,1,1,1,1], height_ratios=[1,1,1,1,1,1,1,1,1,1])

# Adding the title
fig.suptitle(F"Breast Cancer Data Analysis\n{STUDENT_NAME} [{STUDENT_ID}]\n\n", fontsize=20, fontweight="bold")

# Pie plot for diagnosis feature
ax1 = fig.add_subplot(gs[0:3, 0:3])
ax2 = fig.add_subplot(gs[0:3, 3:5])
pie_data = data['diagnosis'].value_counts()
colors = ['#99ff99','#ffcc99']
ax2.pie(pie_data, labels=pie_data.index, colors=colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('Diagnosis Distribution', fontsize=14)

# kde and box plots with hue as diagnosis feature
sns.kdeplot(data=data, x='radius_mean', hue='diagnosis', shade=True, ax=ax1)
ax1.set_title('Distribution of Radius Mean', fontsize=14)

ax3 = fig.add_subplot(gs[0:3, 5:7])
sns.boxplot(data=data, y='texture_mean', x='diagnosis', ax=ax3)
ax3.set_title('Texture Mean Analysis', fontsize=14)

ax4 = fig.add_subplot(gs[4:7, 4:7])  # Swapped position
sns.violinplot(data=data, x='perimeter_mean', y='texture_worst', shade=True, ax=ax4)
ax4.set_title('Perimeter Mean and Texture Worst Correlation', fontsize=14)

ax5 = fig.add_subplot(gs[4:7, 2:4])
sns.kdeplot(data=data, x='area_mean', hue='diagnosis', shade=True, ax=ax5)
ax5.set_title('Area Mean Distribution', fontsize=14)

# Scatter plots with hue as diagnosis feature
ax6 = fig.add_subplot(gs[4:7, 0:2])  # Swapped position
sns.scatterplot(data=data, x='radius_mean', y='texture_mean', hue='diagnosis', ax=ax6)
ax6.set_title('Radius and Texture Mean Comparison', fontsize=14)

ax7 = fig.add_subplot(gs[8:10, 0:2])
sns.boxenplot(data=data, y='perimeter_mean', x='diagnosis', ax=ax7)
ax7.set_title('Analysis of Perimeter Mean', fontsize=14)

ax8 = fig.add_subplot(gs[8:10, 2:4])
sns.scatterplot(data=data, x='compactness_mean', y='concavity_mean', hue='diagnosis', ax=ax8)
ax8.set_title('Compactness vs Concavity Mean Correlation', fontsize=14)

# Text box explaining the results
text_show = """
This dashboard presents a comprehensive examination of a breast cancer dataset,
emphasizing the diagnosis aspect alongside various mean and standard error
measurements. The pie chart illustrates the proportion of malignant ("M") and
benign ("B") diagnoses, revealing a higher prevalence of benign cases. The
subsequent visualizations compare the two diagnosis categories across different
medical parameters, highlighting distinct patterns and differences. This analysis
aids in understanding the characteristics of the dataset and the relationship 
between these features and cancer diagnosis.
"""
text_box = fig.add_subplot(gs[8:10, 4:])
text_box.text(0, 0, text_show, fontsize=14)
text_box.axis('off')

# Adjusting the spacing between subplots
fig.tight_layout()


plt.show()
