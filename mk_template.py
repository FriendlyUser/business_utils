import csv
from jinja2 import Environment, FileSystemLoader


environment = Environment(loader=FileSystemLoader(""))
template = environment.get_template("data/template.jinja2")

sample_template = f"""

"""
# Open the CSV file for reading
with open('data/sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    items = []
    # Loop over each row in the CSV file
    for row in reader:
        # Extract the item name, quantity, and price from the row
        item_name, quantity, price = row

        items.append({
            "item_name": item_name,
            "quantity": quantity,
            "price": price
        })

    print(items)
    context = {
        "invoice_items": items
    }
    latex = template.render(context)

# Write the LaTeX code to a new file
with open('output/invoices.tex', 'w') as texfile:
    texfile.write(latex)