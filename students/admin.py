from django.contrib import admin
from django.http import HttpResponse
from .models import Application
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.units import inch
from django.conf import settings
import os
from .forms import ApplicationForm
from datetime import datetime

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
   # form = ApplicationForm
    list_display = ['id', 'internship', 'apply_date', 'status']
    list_filter = ('applicant', 'apply_date', 'status') 

    def username(self, obj):
        return obj.applicant.username
    
    
    def apply_date(self, obj):
        return obj.apply_date

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions['export_to_pdf'] = (
            self.export_to_pdf,
            'export_to_pdf',
            "Export selected payments to PDF",
        )
        return actions

    def export_to_pdf(self, modeladmin, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="applications.pdf"'

     # Create a PDF document
        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []

     # Add logo at the top
        logo_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'org(3).png')
        logo = Image(logo_path, width=1.5*inch, height=1.5*inch)
        elements.append(logo)

     # Add space after the logo
        elements.append(Paragraph("<br/>", getSampleStyleSheet()['Normal']))

     # Add system name before the heading
        system_name = Paragraph("<b>System:</b> Internconnect", getSampleStyleSheet()['Normal'])
        elements.append(system_name)


     # Add today's date
        today = datetime.today().strftime("%Y-%m-%d")
        date_text = Paragraph(f"<b>Date:</b> {today}", getSampleStyleSheet()['Normal'])
        elements.append(date_text)
    
     # Add space before the heading
        elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))

     # Add heading
        heading = Paragraph("<b>Applicants Report</b>", getSampleStyleSheet()['Heading1'])
        elements.append(heading)

     # Add space before the table
        elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))


     # table data
        data = [['#','Applicant', 'Internship', 'apply_date', 'status']]
        for index, application in enumerate(queryset, start=1):
            formatted_date = application.apply_date.strftime("%Y-%m-%d")
            data.append([index, application.applicant.username, application.internship, formatted_date, application.status])

     # Calculate column widths
        num_cols = len(data[0])
        table_width = letter[0] - inch * 0.5 # Subtracting 2 inches for left and right margins
        col_width = table_width / num_cols
        col_widths = [col_width] * num_cols


        col_widths[0] -= 0.7 * inch 
        
        col_widths[2] += inch

     # Create a table with specified column widths
        table = Table(data, colWidths=col_widths)

     # Add style to the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Header background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Align text to the left
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Body background color
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid color
            ('BOX', (0, 0), (-1, -1), 1, colors.black),  # Box color
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),  # Inner grid color
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # Header font size
            ('LEADING', (0, 0), (-1, -1), 12),  # Leading (line spacing)
            ('TOPPADDING', (0, 0), (-1, -1), 6),  # Top padding
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Bottom padding
            ('LEFTPADDING', (0, 0), (-1, -1), 12),  # Left padding
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),  # Right padding
        ])
        table.setStyle(style)
        elements.append(table)

     # Build PDF document
        doc.build(elements)

        return response


    export_to_pdf.short_description = "Export selected payments to PDF"

 