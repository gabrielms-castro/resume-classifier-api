
from app.services.text_extractor_service import call_text_extractor, clean_output_text

def test_pdf_text_extractor_extract_text():
    print("\n[DEBUG] Testing PDF Text Extractor...")
    # Simulating the UploadFile object file.read() method
    with open("tests/files/sample.pdf", "rb") as file:
        content = file.read()
        print(f"[DEBUG] Bytes: {len(content)}")
        
    extractor = call_text_extractor(file_type="application/pdf")
    text = extractor.extract_text(content)
    # text = clean_text(text)
    print(f"[DEBUG] Extracted Text Sample: {text[:100]}")

    assert isinstance(text, str)
    assert len(text.strip()) > 0 
       
def test_docx_text_extractor_extract_text():
    print("\n[DEBUG] Testing DOCX Text Extractor...")
    # Simulating the UploadFile object file.read() method
    with open("tests/files/sample.docx", "rb") as file:
        content = file.read()
        print(f"[DEBUG] Bytes: {len(content)}")
        
    extractor = call_text_extractor(file_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    text = extractor.extract_text(content)
    # text = clean_text(text)
    print(f"[DEBUG] Extracted Text Sample: {text[:100]}")

    assert isinstance(text, str)
    assert len(text.strip()) > 0  
      
def test_txt_text_extractor_extract_text():
    print("\n[DEBUG] Testing TXT Text Extractor...")
    # Simulating the UploadFile object file.read() method
    with open("tests/files/sample.txt", "rb") as file:
        content = file.read()
        print(f"[DEBUG] Bytes: {len(content)}")
        
    extractor = call_text_extractor(file_type="text/plain")
    text = extractor.extract_text(content)
    # text = clean_text(text)
    print(f"[DEBUG] Extracted Text Sample: {text[:100]}")

    assert isinstance(text, str)
    assert len(text.strip()) > 0    
