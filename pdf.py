from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.doctemplate import Indenter


def generateNormalReport(file_name, data, total ,header_elements):
    # Crear un objeto PDF con orientación horizontal
    pdf_file = f"{file_name}.pdf"

    # Crear una lista para almacenar los elementos a agregar al PDF
    elements = header_elements

    # Crear un objeto PDF con orientación horizontal y tamaño personalizado
    pdf = SimpleDocTemplate(pdf_file, pagesize=(landscape(A4)[0], landscape(A4)[1]), topMargin=0, bottomMargin=0)

    # Crear una tabla con los datos y establecer el ancho de las columnas
    table = Table(data)
    total_table = Table(total)

    # Estilo de la tabla principal
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D63864')),  # Fondo de la primera fila
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Color del texto en la primera fila
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),  # Alinear el contenido al centro
    ])

    style = getSampleStyleSheet()['Normal']
    style.fontName = 'Helvetica-Bold'

    for i in range(len(data[0])):
        table_style.add('FONTNAME', (i, 0), (i, 0), 'Helvetica-Bold')

    table.setStyle(table_style)

    # Estilo de la tabla de totales
    total_table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#000000')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ])

    total_table.setStyle(total_table_style)

    # Crear un espacio (Spacer) con un espaciado de 10 puntos
    spacer = Spacer(1, 20)

    # Crear un párrafo (h2) con el texto "Total:" y aplicar el espaciado con un padding de 10px
    total_paragraph = Paragraph("<font size='18'><b>Total:</b></font>", getSampleStyleSheet()['Normal'])
    total_paragraph.leading = 10  # Espaciado del párrafo en puntos

    # Agregar la tabla y el párrafo a la lista de elementos
    elements.append(spacer)
    elements.append(table)
    elements.append(spacer)
    elements.append(total_paragraph)
    elements.append(spacer)
    elements.append(total_table)

    # Construir el PDF con la lista de elementos
    pdf.build(elements)

    # Imprimir el nombre del archivo generado
    print(f"El archivo PDF se ha generado como: {pdf_file}")

def generatePDFHeader(report_name, store_name):
    elements = []

    # Crear una tabla para el logo y la información de la tienda
    data = [
        [Image('logo.assets.jpg', width=25, height=25), f"Report:{report_name}", f"Store: {store_name}"]
    ]

    header_table = Table(data, colWidths=[50, 500, 190])
    
    # Estilo de la tabla de encabezado
    header_table_style = TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),  # Borde exterior
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

    ])

    header_table.setStyle(header_table_style)
    header_table.vAlign = 'TOP'  # Alinear el contenido de la tabla hacia arriba
    header_table.hAlign = 'LEFT'  # Alinear el contenido de la tabla hacia la izquierda
    elements.append(Indenter(left=-50))
    elements.append(header_table)

    return elements

# Ejemplo de uso
data = [
    ['DATE', 'CARDS', 'CREDITS', 'TIMECARD', 'PARTY', 'QUANTITY', 'VOUCHER', 'BONUS', 'TOTAL', 'TOTAL CASH', 'TKSCHARGE', 'TKSDISCHARGE'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
]
total = [
    ['DATE', 'CARDS', 'CREDITS', 'TIMECARD', 'PARTY', 'QUANTITY', 'VOUCHER', 'BONUS', 'TOTAL', 'TOTAL CASH', 'TKSCHARGE', 'TKSDISCHARGE'],
    ['2023-08-14', '$2.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$2.00', '$2.00', '0', '0'],
]

header_elements = generatePDFHeader("Balance per day", "Development Elias")
# generatePDFContent("balance-per-day", data, total, header_elements)

data2 = [
    {
        "name": "Machine1",
        "transactions": 
        [
            ["DATE", "MACHINE", "TIMECARD", "PARTY", "CREDITS", "BONUS", "TOTAL"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"],
            ["2023-08-14", "Machine1", "$0.00", "$0.00", "$0.00", "$0.00", "$0.00"]    
        ]
    },
    {
        "name": "Machine 2",
        "transactions": 
        [
            ["DATE", "MACHINE", "TIMECARD", "PARTY", "CREDITS", "BONUS", "TOTAL"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],    
        ]
    },
    {
        "name": "Super Daytona",
        "transactions": 
        [
            ["DATE", "MACHINE", "TIMECARD", "PARTY", "CREDITS", "BONUS", "TOTAL"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
            ["2023-08-14", "Super Daytona", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],    
        ]
    }
]

total2 = [
    ["DATE", "MACHINE", "TIMECARD", "PARTY", "CREDITS", "BONUS", "TOTAL"],
    ["2023-08-14", "Machine 2", "$1.00", "$4.00", "$0.00", "$0.00", "$5.00"],
]

def generateBySomethingReport(pdf_name, data, total, header_elements):
    pdf_file = f"{pdf_name}.pdf"

    pdf = SimpleDocTemplate(pdf_file, pagesize=(landscape(A4)[0], landscape(A4)[1]), topMargin=0, bottomMargin=0)

    elements = header_elements
    spacer = Spacer(1, 20)

    total_table = Table(total, colWidths=[pdf.width / len(total[0])]*len(total[0]))

    for item in data:
        title_paragraph = Paragraph(f"<font size='18'><b>{item['name']}:</b></font>", getSampleStyleSheet()['Normal'])
        title_paragraph.leading = 10
        elements.append(spacer)
        elements.append(title_paragraph)
        elements.append(spacer)

        # Crear una tabla con los datos de cada item (maquina o cashier)
        table = Table(item['transactions'], colWidths=[pdf.width / len(item['transactions'][0])]*len(item['transactions'][0]))
        
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D63864')),  
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ])

        table.setStyle(table_style)
        elements.append(table)

    # Estilo de la tabla de totales
    total_table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#000000')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ])

    total_table.setStyle(total_table_style)

    # Crear un párrafo (h2) con el texto "Total:" y aplicar el espaciado con un padding de 10px
    total_paragraph = Paragraph("<font size='18'><b>Total:</b></font>", getSampleStyleSheet()['Normal'])
    total_paragraph.leading = 10  # Espaciado del párrafo en puntos
    elements.append(total_paragraph)
    elements.append(spacer)
    elements.append(total_table)
    pdf.build(elements)
    print(f"El archivo PDF se ha generado como: {pdf_file}")

generateBySomethingReport("collect-by-day-by-machine", data2, total2, header_elements)