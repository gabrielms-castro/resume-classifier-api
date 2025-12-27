import docx
import io
from app.services.text_extractor.interface import TextExtractor
from app.services.text_extractor.utils import clean_output_text


class MSWordTextExtractor(TextExtractor):
    def extract_text(self, content):
        doc = docx.Document(io.BytesIO(content))
        text_pages = []
        for paragraph in doc.paragraphs:
            text_pages.append(paragraph.text)
        return clean_output_text("\n".join(text_pages))