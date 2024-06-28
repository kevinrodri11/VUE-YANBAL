import pdfkit
import os
import subprocess
import time
import uno
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python Lector.py <codigo>")
    sys.exit(1)

# Capture the codigo argument
codigo = sys.argv[1]
print(f"Received codigo: {codigo}")

# Convert codigo to int
try:
    id_coordinator = int(codigo)
except ValueError:
    print("Invalid codigo: Must be an integer")
    sys.exit(1)

# Run stopwatch to measure execution time, formatting it as a string
print(time.strftime("%H:%M:%S"))

# Function to start LibreOffice in headless mode
def start_libreoffice():
    try:
        subprocess.Popen(["libreoffice", "--headless", "--invisible", "--accept=socket,host=localhost,port=2002;urp;"])
        print("LibreOffice started successfully.")
        print(time.strftime("%H:%M:%S"))
    except Exception as e:
        print("Error starting LibreOffice:", e)

import time

# Function to retrieve data from the first column starting from a specific row
def get_first_column_data(sheet, start_row, end_row):
    max_row = sheet.Rows.Count
    start_row = min(start_row, max_row)
    end_row = min(end_row, max_row)
    first_column_range = sheet.getCellRangeByPosition(1, start_row - 1, 1, end_row - 1)
    data_array = first_column_range.getDataArray()
    for i, row in enumerate(data_array):
        if not row[0]:  # Check if cell is empty
            print(i + start_row)
            return i + start_row  # Return the index of the first empty cell
    return end_row  # If no empty cell found, return the end row

# Function to format numerical values as currency
def format_currency(value):
    return f"$ {value:,.0f}"

# Function to generate HTML content
def generate_html_content(id_coordinator, data_values, data_rows_html):
    html_template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>PDF Report</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet" />
        </head>
        
        <style>
            body {{
                font-family: 'Inter', sans-serif;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            th, td {{
                padding: 8px;
                border: 1px solid #ddd;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            caption {{
                text-align: left;
                margin-bottom: 10px;
            }}
        </style>

        <body>
            <table>
                <thead>
                    <tr>
                        <th colspan="2">CODIGO DIRECTORA</th>
                        <th colspan="4">{id_coordinator}</th>
                    </tr>
                    <tr>
                        <th colspan="2">NOMBRE DIRECTORA</th>
                        <th colspan="4">{data_values[0]}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>TOTAL CARTERA ASIGNADA</th>
                        <th># FACTURAS</th>
                        <th></th>
                        <th>CARTERA ASIGNADA</th>
                        <th></th>
                        <th>RECAUDO</th>
                    </tr>
                    <tr>
                        <td>{data_values[1]}</td>
                        <td>{data_values[4]}</td>
                        <td>CONTACTO DIRECTO</td>
                        <td>{data_values[7]}</td>
                        <td>CONTACTO DIRECTO</td>
                        <td>{data_values[10]}</td>
                    </tr>
                    <tr>
                        <th>TOTAL RECAUDO AL DIA</th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                    </tr>
                    <tr>
                        <td>{data_values[2]}</td>
                        <td>{data_values[5]}</td>
                        <td>SIN CONTACTO</td>
                        <td>{data_values[8]}</td>
                        <td>SIN CONTACTO</td>
                        <td>{data_values[11]}</td>
                    </tr>
                    <tr>
                        <th>ACUERDOS DE PAGO</th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                    </tr>
                    <tr>
                        <td>{data_values[3]}</td>
                        <td>{data_values[6]}</td>
                        <td>SIN CONTACTO</td>
                        <td>{data_values[9]}</td>
                        <td>SIN CONTACTO</td>
                        <td>{data_values[12]}</td>
                    </tr>
                </tbody>
            </table>
            <table style="font-size: 12px">
                <thead>
                    <tr>
                        <th>CÓDIGO DIRECTORA</th>
                        <th>CÓDIGO</th>
                        <th>NOMBRE DIRECTORA</th>
                        <th>CELULAR</th>
                        <th>FACTURA</th>
                        <th>VALOR TOTAL AL DIA</th>198513

                        <th>DIAS MORA AL DIA</th>
                        <th>RECAUDO</th>
                        <th>MEJOR GESTIÓN</th>
                        <th>FECHA ACUERDO</th>
                        <th>VALOR ACUERDO</th>
                        <th>CONTACTABILIDAD</th>
                        <th>EDAD DE LIQUIDACIÓN</th>
                    </tr>
                </thead>
                {data_rows}
            </table>
        </body>
    </html>
    """
    # Insert dynamic data into HTML template
    html_content = html_template.format(id_coordinator=id_coordinator, data_values=data_values, data_rows=data_rows_html)
    return html_content

def main():
    # Replace 'file_path' with the path to your XLSX file
    file_path = "X:\kevin-project\src\\backend\estado_cartera\TEST.xlsb"

    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    print(f"The file {file_path} exists.")

    # Start LibreOffice in headless mode
    start_libreoffice()

    # Wait for LibreOffice to start (adjust sleep time if needed)
    time.sleep(5)

    # Connect to LibreOffice-
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)

    # Load the XLSX file
    url = uno.systemPathToFileUrl(os.path.abspath(file_path))
    document = desktop.loadComponentFromURL(url, "_blank", 0, ())
    if not document:
        print(f"Error loading file {file_path}.")
        return

    print(f"File {file_path} loaded successfully.")

    # Get a cell range
    sheet = document.Sheets.getByName("ESTADO DE CARTERA")

    # Get data from columns 1 to 13 starting from row 300
    start_row = 300
    end_row = sheet.Rows.Count  # Use the last row of the sheet
    first_empty_row = get_first_column_data(sheet, start_row, end_row)

    start_cell = "B300"
    end_cell = "N" + str(first_empty_row - 1)

    # Get data from the specified range
    data_range = sheet.getCellRangeByName(start_cell + ":" + end_cell)

    # Associate data with id_coordinator
    data_associated = {}
    for row in data_range.getDataArray():
        current_id_coordinator = row[0]  # Assuming id_coordinator is in the first column
        if current_id_coordinator == id_coordinator:
            if id_coordinator not in data_associated:
                data_associated[id_coordinator] = []
            data_associated[id_coordinator].append(row[1:])  # Exclude id_coordinator from the associated data

    # set containing the indices of columns that should be formatted as currency
    columns_to_format = {4, 6, 9}

    # Generate rows of HTML table
    data_rows_html = ""
    for key, value_list in data_associated.items():
        for row_tuple in value_list:
            row = "<tr>"
            row += f"<td>{key}</td>"
            for index, item in enumerate(row_tuple):
                # Round numerical values and convert to integers
                if isinstance(item, (int, float)):
                    item = int(round(item))
                # Check if the item is in a column that should be formatted
                if index in columns_to_format and isinstance(item, (int, float)):
                    item = format_currency(item)  # Format as currency
                row += f"<td>{item}</td>"
            row += "</tr>"
            data_rows_html += row

    # Insert id_coordinator into a specific cell in the Excel file
    id_coordinator_cell = "C6" 
    sheet.getCellRangeByName(id_coordinator_cell).setValue(id_coordinator)

    # Wait for a brief moment to allow the changes to be applied
    time.sleep(5)

    # Define data cells for retrieval
    data_cells = ["C7", "B11", "B14", "B17", "D11", "D14", "D17","F11", "F14", "F17", "H11", "H14", "H17"]
    data_values = [sheet.getCellRangeByName(cell).getString() for cell in data_cells]

    # Render HTML content
    html_content = generate_html_content(id_coordinator, data_values, data_rows_html)

    # Path where you want to save the PDF output
    pdf_output_path = os.path.abspath("output.pdf")

    # Options for PDF generation
    options = {
        "page-size": "Letter",
        "orientation": "Landscape",
        "encoding": "UFT-8"
    }

    # Path to wkhtmltopdf executable
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    # Convert HTML to PDF using pdfkit
    pdfkit.from_string(html_content, pdf_output_path, options=options, configuration=config)

    print("PDF generated successfully.")
    print(pdf_output_path)

if __name__ == "__main__":
    main()