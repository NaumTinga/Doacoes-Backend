# # from reportlab.lib import colors
# # from reportlab.lib.pagesizes import A4
# # from reportlab.lib.styles import getSampleStyleSheet
# # from reportlab.lib.units import mm
# # from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
# # from reportlab.lib.enums import TA_CENTER
# # from reportlab.lib.fonts import addMapping
# # from reportlab.lib.colors import black
# # from reportlab.pdfgen.canvas import Canvas
# #
# #
# # # Helper function to create a paragraph with a given style
# # def create_paragraph(text, font_size=10, bold=False, align=TA_CENTER):
# #     style = getSampleStyleSheet()['Normal']
# #     style.fontSize = font_size
# #     style.alignment = align
# #     if bold:
# #         style.fontName = 'Helvetica-Bold'
# #     return Paragraph(text, style)
# #
# #
# # # Create a PDF document
# # doc = SimpleDocTemplate("requisicao_fundos.pdf", pagesize=A4)
# # elements = [create_paragraph("Requisição de Fundos", font_size=12, bold=True), Spacer(1, 10)]
# #
# # # Title
# #
# # # Section with multiple fields
# # data = [
# #     [create_paragraph("N. Req (Comp):", font_size=10), "Value for numRequisicaoComp"],
# #     [create_paragraph("Requisição n:", font_size=10), "Value for reqNumero"],
# #     [create_paragraph("N/Ref:", font_size=10), "Value for refNumero"],
# #     [create_paragraph("Projecto:", font_size=10), "Value for projecto"],
# #     [create_paragraph("Ref Bancária:", font_size=10), "Value for refBancaria"],
# #     [create_paragraph("Financiador:", font_size=10), "Value for financiador"],
# #     [create_paragraph("Banco:", font_size=10), "Value for banco"],
# #     [create_paragraph("Conta:", font_size=10), "Value for conta"],
# #     [create_paragraph("Valor:", font_size=10), "Value for valor"],
# #     [create_paragraph("Data de Emissão:", font_size=10), "Value for dataEmissao"],
# # ]
# #
# # table = Table(data, colWidths=[100 * mm, 80 * mm])
# # table.setStyle(TableStyle([
# #     ('TEXTCOLOR', (0, 0), (-1, -1), black),
# #     ('LINEBELOW', (1, 0), (1, -1), 0.3, colors.grey),
# # ]))
# #
# # elements.append(table)
# # elements.append(Spacer(1, 20))
# #
# # # Create the PDF document
# # doc.build(elements)
#
#
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML
#
#
# def generate_pdf(request):
#     # Example context data
#     context = {
#         'numRequisicaoComp': '12345',
#         'reqNumero': '67890',
#         'projecto': 'Project A',
#         'refBancaria': 'ABC123',
#         # Add more context data as needed
#     }
#
#     # Render HTML template with context data
#     html_string = render_to_string('template.html', context)
#
#     # Create PDF from HTML
#     html = HTML(string=html_string)
#     pdf = html.write_pdf()
#
#     # Return PDF response
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     return response
