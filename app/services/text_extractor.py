from abc import ABC, abstractmethod

from pypdf import PdfReader


class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self):
        raise NotImplementedError("This method should be implemented by subclasses")

class PDFTextExtractor(TextExtractor):
    ...

class MSWordTextExtractor(TextExtractor):
    ...

class PlainTextExtractor(TextExtractor):
    ...
    
def read_pdf(file_path):
    reader = PdfReader(file_path)
    
    pdf_txt = []
    for page in reader.pages:
        text = page.extract_text()
        pdf_txt.append(text)
    return pdf_txt

def call_text_extractor(file_type):
    extractors = {
        "application/pdf": PDFTextExtractor,
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": MSWordTextExtractor,
        "text/plain": PlainTextExtractor
    }
    return extractors[file_type]()