import io
import re

from abc import ABC, abstractmethod
from pypdf import PdfReader


class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self):
        raise NotImplementedError("This method should be implemented by subclasses")

class PDFTextExtractor(TextExtractor):
    def extract_text(self, content):
        reader = PdfReader(io.BytesIO(content))
        text_pages = []
        for page in reader.pages:
            text = page.extract_text()
            text_pages.append(text)
        return clean_output_text("\n".join(text_pages))
    

class MSWordTextExtractor(TextExtractor):
    def extract_text(self, content):
        try:
            import docx
            doc = docx.Document(io.BytesIO(content))
            text_pages = []
            for paragraph in doc.paragraphs:
                text_pages.append(paragraph.text)
            return clean_output_text("\n".join(text_pages))
        
        except ImportError:
            raise RuntimeError("docx module not found")

class PlainTextExtractor(TextExtractor):
    def extract_text(self, content):
        if isinstance(content, bytes):
            return clean_output_text(content.decode(encoding='utf-8', errors='ignore'))
        return ""

def call_text_extractor(file_type):
    extractors = {
        "application/pdf": PDFTextExtractor,
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": MSWordTextExtractor,
        "text/plain": PlainTextExtractor
    }
    return extractors[file_type]()

def clean_output_text(text):
    if not text:
        return ""
    
    text = re.sub(r'[\n\s\t]+', " ", text)
    text = re.sub(r'\s{2,}', " ", text)
    return text.strip()