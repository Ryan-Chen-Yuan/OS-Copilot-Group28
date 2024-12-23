def create_condensed_cheat_sheet(pdf_folder_path, output_docx_path):
    """
    Convert PDF files into a condensed Word document cheat sheet by removing special characters 
    and extra whitespace.
    
    Args:
        pdf_folder_path (str): Full path to the folder containing PDF files to process
        output_docx_path (str): Full path where the output Word document should be saved
        
    Returns:
        str: Absolute path to the generated Word document
    """
    from PyPDF2 import PdfReader
    from docx import Document
    from docx.shared import Pt, Inches
    import os
    import re
    from tqdm import tqdm
    
    # Create new Word document
    doc = Document()
    
    # Set margins (0.3 inches)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.3)
        section.bottom_margin = Inches(0.3)
        section.left_margin = Inches(0.3)
        section.right_margin = Inches(0.3)
    
    # Initial font size and line spacing
    font_size = 6.5
    line_spacing = 0.8
    
    # Function to clean text
    def clean_text(text):
        text = re.sub(r'[\n\r\t]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        patterns_to_remove = [
            r'\d+/\d+',  # Page numbers
            r'\u00a9.*?All Rights Reserved',  # Copyright information
            r'www\..*?\.com',  # Website addresses
            r'http\S+',  # URLs
            r'Figure\s*\d+',  # Figure labels
            r'Table\s*\d+'  # Table labels
        ]
        for pattern in patterns_to_remove:
            text = re.sub(pattern, '', text)
        return text.strip()
    
    # Process all PDF files
    for filename in tqdm(os.listdir(pdf_folder_path)):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, filename)
            pdf_reader = PdfReader(pdf_path)
            
            text = ""
            for page in tqdm(pdf_reader.pages, desc="Reading pages", leave=False):
                text += page.extract_text() if page.extract_text() else ""
            
            # Clean the text
            text = clean_text(text)
            
            paragraph = doc.add_paragraph(text)
            paragraph.paragraph_format.line_spacing = line_spacing
            paragraph.paragraph_format.space_after = Pt(0)
            paragraph.paragraph_format.space_before = Pt(0)
            for run in paragraph.runs:
                run.font.size = Pt(font_size)
    
    # Save the document
    doc.save(output_docx_path)
    return os.path.abspath(output_docx_path)