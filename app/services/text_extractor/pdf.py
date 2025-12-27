import io
from pypdf import PdfReader

from importlib.readers import ZipReader
from app.services.text_extractor.interface import TextExtractor
from app.services.text_extractor.utils import clean_output_text


class PDFTextExtractor(TextExtractor):
    def extract_text(self, content):
        reader = PdfReader(io.BytesIO(content))
        text_pages = []
        for page in reader.pages:
            text = page.extract_text()
            text_pages.append(text)
        return clean_output_text("\n".join(text_pages))