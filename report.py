# Task 2: Professional PDF Report Generation

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("data.csv")

# -------------------------------
# ANALYSIS
# -------------------------------
avg_temp = df["Temperature"].mean()
max_temp = df["Temperature"].max()
min_temp = df["Temperature"].min()
avg_humidity = df["Humidity"].mean()

# -------------------------------
# CREATE PDF DOCUMENT
# -------------------------------
doc = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

content = []

# -------------------------------
# TITLE
# -------------------------------
content.append(Paragraph("Weather Data Report", styles["Title"]))
content.append(Spacer(1, 12))

# -------------------------------
# SUMMARY SECTION
# -------------------------------
content.append(Paragraph("Summary:", styles["Heading2"]))
content.append(Spacer(1, 10))

content.append(Paragraph(f"Average Temperature: {avg_temp:.2f} °C", styles["Normal"]))
content.append(Paragraph(f"Maximum Temperature: {max_temp} °C", styles["Normal"]))
content.append(Paragraph(f"Minimum Temperature: {min_temp} °C", styles["Normal"]))
content.append(Paragraph(f"Average Humidity: {avg_humidity:.2f} %", styles["Normal"]))

content.append(Spacer(1, 20))

# -------------------------------
# TABLE DATA
# -------------------------------
table_data = [["Day", "Temperature (°C)", "Humidity (%)"]]

for index, row in df.iterrows():
    table_data.append([row["Day"], row["Temperature"], row["Humidity"]])

# Create table
table = Table(table_data)

# Style the table
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
]))

content.append(Paragraph("Detailed Data:", styles["Heading2"]))
content.append(Spacer(1, 10))
content.append(table)

# -------------------------------
# BUILD PDF
# -------------------------------
doc.build(content)

print(" PDF generated successfully!")