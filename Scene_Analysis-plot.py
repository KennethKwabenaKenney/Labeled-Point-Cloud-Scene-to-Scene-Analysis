import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the path to your Excel file
excel_file = r'D:\ODOT_SPR866\My Label Data Work\New Manual Labelling\6_Analysis\Scene Analyis_ A_site.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Define the features in the order they appear in your Excel file
features = ['Pole-like Objects', 
            'Powerlines',
            'Street_lamp',
            'Traffic Light',
            'Traffic Sign',
            'Trees',
            'Wire Conductor',
            'Lane Marking', 
            'High Vegetation',
            'Highway Gantry',
            'Telephone/TV cables',
            'Bush',
            'Unclassified',
            'Unknown']

# Sort DataFrame by 'Segment No.' (assuming 'Segment No.' is the column name)
df_sorted = df.sort_values(by='Site No.')

# Extract columns containing '% Confidence'
confidence_columns = [col for col in df_sorted.columns if '% Confidence' in col]

# Create a new DataFrame with only the '% Confidence' columns
confidence_data = df_sorted[confidence_columns].T

# Extract the segment numbers and feature counts
segment_numbers = df_sorted['Site No.']
feature_counts = df_sorted[features].values.T  # Transpose to match feature order

# Define custom colors (can be hex codes or named colors)
custom_colors = ['#8c564b',
                 '#9467bd',
                 '#F7DC6F',
                 '#E67E22',
                 '#E64A19',
                 '#66BB6A',
                 '#aec7e8',
                 '#660033', 
                 '#006600',
                 '#17becf',
                  '#3399CC',
                  '#CCFF99',
                 '#9E9E9E',
                 '#78909C']

# Plotting the stacked horizontal bars for number of samples
fig1, ax1 = plt.subplots(figsize=(18, 12))  # Adjust figsize as needed

# Calculate positions for bars
bar_positions1 = np.arange(len(segment_numbers))

# Plot each feature as stacked bars with custom colors
for i, feature in enumerate(features):
    ax1.barh(bar_positions1, feature_counts[i], label=feature, left=np.sum(feature_counts[:i], axis=0), color=custom_colors[i])

# Customize plot appearance
ax1.set_xlabel('Number of Object Samples', fontweight='bold', fontsize=16)
ax1.set_ylabel('Site ID',  fontweight='bold', fontsize=16)
ax1.set_title('Distribution of Object Samples Across Sites', pad=20, fontweight='bold', fontsize=16)
ax1.tick_params(axis='y', labelsize=16) 
ax1.tick_params(axis='x', labelsize=16) 
ax1.set_yticks(bar_positions1)
ax1.set_yticklabels(segment_numbers)
ax1.invert_yaxis()  # Invert y-axis to match desired order

# Adjust legend font size
ax1.legend(fontsize=25)
plt.tight_layout()
plt.show()


# # Plotting the stacked horizontal bars for confidence percentages
# fig2, ax2 = plt.subplots(figsize=(18, 12))  # Adjust figsize as needed

# # Transpose confidence_data to match segment_numbers
# confidence_data_transposed = confidence_data.values

# # Calculate positions for bars
# bar_positions2 = np.arange(len(segment_numbers))

# # Plot each feature as stacked bars with custom colors
# for i, feature in enumerate(features):
#     ax2.barh(bar_positions2, confidence_data_transposed[i], label=feature, left=np.sum(confidence_data_transposed[:i], axis=0), color=custom_colors[i])

# # Customize plot appearance
# ax2.set_xlabel('% Confidence')
# ax2.set_ylabel('Segment Number')
# ax2.set_title('Feature Confidence Across Segment Numbers')
# ax2.set_yticks(bar_positions2)
# ax2.set_yticklabels(segment_numbers)
# ax2.invert_yaxis()  # Invert y-axis to match desired order
# ax2.legend()

# plt.tight_layout()
# plt.show()
