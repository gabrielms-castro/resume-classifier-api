from app.services.text_extractor.interface import TextExtractor
from app.services.text_extractor.utils import clean_output_text


class PlainTextExtractor(TextExtractor):
    def extract_text(self, content):
        if isinstance(content, bytes):
            return clean_output_text(content.decode(encoding='utf-8', errors='ignore'))
        return ""