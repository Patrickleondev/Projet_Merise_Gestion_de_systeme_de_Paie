"""from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.units import inch
from reportlab.lib import colors

def creer_bulletin_paie_pdf(fichier, nom, prenom, poste, salaire, date_paiement, signature, logo_path):
    doc = SimpleDocTemplate(fichier, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    #logo de l'entreprise
    try:
        logo = Image("logo.jpg",width=doc.width, height=1.5 * inch)
        elements.append(logo)
    except Exception as e:
        print(f"Erreur lors du chargement du logo : {e}")

    #entete 
    header_data = [
        ["GROUPE 5 PME", "01/20"],
        ["33 rue Pasteur", ""],
        ["31000 Lomé-Togo", ""]
    ]
    header_table = Table(header_data, colWidths=[doc.width / 2.0, doc.width / 2.0])
    header_table.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('ALIGN', (0, 0), (1, 2), 'CENTER'),
        ('FONTNAME', (0, 0), (1, 2), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (1, 2), 12),
        ('BOTTOMPADDING', (0, 0), (1, 2), 12)
    ]))
    elements.append(header_table)

    #space html
    elements.append(Paragraph("<br/><br/>", styles['Normal']))

    #infos sur l'employé
    employe_data = [
        ["Nom", "Prénom", "Poste", "Salaire Net(XOF)", "Date de Paiement"],
        [nom, prenom, poste, f"{salaire}", date_paiement]
    ]
    
    employe_table = Table(employe_data, colWidths=[100, 150, 100, 100, 100])
    employe_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(employe_table)

    elements.append(Paragraph("<br/><br/>", styles['Normal']))

    #Signature
    signature_data = [
        ["Signature Du Directeur :", signature]
    ]
    signature_table = Table(signature_data, colWidths=[150, 300])
    signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (1, -1), 5)
    ]))
    elements.append(signature_table)

    doc.build(elements)


if __name__ == "__main__":
    nom = "GANDONOU"
    prenom = "Koffi Patrick-léon"
    poste = "Développeur"
    salaire = "500000"
    date_paiement = "20/06/2023"
    signature = "Signature de l'employé:"
    logo_path = "logo.jpg"

creer_bulletin_paie_pdf(f"{nom}-paie.pdf", nom, prenom, poste, salaire, date_paiement, signature, logo_path)"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.units import inch
from reportlab.lib import colors


def creer_bulletin_paie_pdf(fichier, nom, prenom, poste, salaire, date_paiement, signature):
    doc = SimpleDocTemplate(fichier, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # Logo de l'entreprise
    try:
        logo = Image("logo.jpg", width=doc.width, height=1.5 * inch)
        elements.append(logo)
    except Exception as e:
        print(f"Erreur lors du chargement du logo : {e}")

    # En-tête
    header_data = [
        ["GROUPE 5 PME", "01/20"],
        ["33 rue Pasteur", ""],
        ["31000 Lomé-Togo", ""]
    ]
    header_table = Table(header_data, colWidths=[doc.width / 2.0, doc.width / 2.0])
    header_table.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('ALIGN', (0, 0), (1, 2), 'CENTER'),
        ('FONTNAME', (0, 0), (1, 2), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (1, 2), 12),
        ('BOTTOMPADDING', (0, 0), (1, 2), 12)
    ]))
    elements.append(header_table)

    # Espace HTML
    elements.append(Paragraph("<br/><br/>", styles['Normal']))

    # Infos sur l'employé
    employe_data = [
        ["Nom", "Prénom", "Poste", "Salaire Net(XOF)", "Date de Paiement"],
        [nom, prenom, poste, f"{salaire}", date_paiement]
    ]
    
    employe_table = Table(employe_data, colWidths=[100, 150, 100, 100, 100])
    employe_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(employe_table)

    elements.append(Paragraph("<br/><br/>", styles['Normal']))

    # Signature
    signature_data = [
        ["Signature Du DRH :", signature]
    ]
    signature_table = Table(signature_data, colWidths=[150, 300])
    signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (1, -1), 5)
    ]))
    elements.append(signature_table)
    
    signature_data2 = [
        ["Signature de l'Employé:", nom + " "+prenom]
    ]
    signature_table = Table(signature_data2, colWidths=[150, 300])
    signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (1, -1), 5)
    ]))
    elements.append(signature_table)
    doc.build(elements)

