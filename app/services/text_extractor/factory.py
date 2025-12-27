from app.services.text_extractor.docx import MSWordTextExtractor
from app.services.text_extractor.txt import PlainTextExtractor
from app.services.text_extractor.pdf import PDFTextExtractor


def call_text_extractor(file_type):
    extractors = {
        "application/pdf": PDFTextExtractor,
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": MSWordTextExtractor,
        "text/plain": PlainTextExtractor
    }
    return extractors[file_type]()
