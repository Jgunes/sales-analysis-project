import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

dF= pd.read_excel("sales.xlsx")

product_sales=  dF.groupby("Product")["Sales"].sum()

best_product=product_sales.idxmax()
max_sales= product_sales.max()

plt.figure(figsize=(12,6))

product_sales.sort_values(ascending=False).plot(
    kind="bar",
    colormap="Set3"
)

plt.title("Product Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_chart.png")
plt.close()

pdf=FPDF()
pdf.add_page()

pdf.set_font("Arial","B",18)
pdf.cell (0,10, "Sales Analysis Report", ln=True)

pdf.ln(10)

pdf.set_font("Arial","",12)
pdf.multi_cell(
    0,
    10,
    "This report analyzes product sales performance"
    "across different product categories."

)

pdf.ln(5)

pdf.cell(0,10,f"Best Selling Product:{best_product}", ln=True)
pdf.cell(0,10,f"Highest Sales Value:{max_sales}", ln=True)

pdf.ln(10)

pdf.image("sales_chart.png",w=180)

pdf.ln(10)

pdf.set_font("Arial","B",14)
pdf.cell (0,10,"Insights",ln=True)

pdf.set_font("Arial","",12)

pdf.multi_cell(
    0,
    10,
    f"{best_product} is currently the best performing product."
    "Products with high sales should receive increased marketing"
    "focus and stock optimization."

)

pdf.ln(5)

pdf.set_font("Arial","B",14)
pdf.cell(0,10,"Recommendations", ln=True)

pdf.set_font ("Arial","B",12)

pdf.multi_cell(
    0,
    10,
    "- Increase inventory for top selling products \n"
    "-Improve promotion strategies for low selling products\n"
    "- Analyze customer purchasing behavior\n"
    "-Monitor monthly sales trends for better forecasting"

)

pdf.output("sales_report.pdf")

print("Report generated successfully: sales_report.pdf")