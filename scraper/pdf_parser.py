# The tool aimed to scrap a content from a PDF document, to use it for an LLM inference. 
# It's normally used once it's clear that URL given is a link to the PDF file.
#
import requests
import fitz


class PDFProcessor:
    def process(self, pdf_url):
        try:
            # Download PDF from URL
            response = requests.get(pdf_url)
            response.raise_for_status()  # Check for HTTP errors
            pdf_data = response.content
            
            # Open PDF from downloaded bytes
            doc = fitz.open(stream=pdf_data, filetype="pdf")
            total_pages = doc.page_count
            full_text = ""

            for page_num in range(1, total_pages + 1):
                try:
                    page = doc[page_num - 1]  # Access each page individually
                    blocks = page.get_text("blocks")
                    images = page.get_images(full=True)

                    # Sort blocks for multi-column layout
                    sorted_blocks = self.__sort_blocks_multicolumn(blocks, num_columns=2, page_width=page.rect.width)
                    result_text = ""
                    
                    for b in sorted_blocks:
                        x0, y0, x1, y1, text, block_no, block_type = b
                        result_text += text.strip() + " "
                    
                    # Append result text to the full text
                    full_text += result_text + "\n"

                except Exception as e:
                    logger.error(f"Warning: Failed to process page {page_num}. Error: {e}")
                    continue  # Skip to the next page if an error occurs

            return full_text.strip()  # Return all text as a single string

        except Exception as e:
            logger.error(f"Failed to download or process PDF from URL. Error: {e}")
            return None

    @staticmethod
    def __sort_blocks_multicolumn(blocks, num_columns=2, page_width=None):
        if page_width is None:
            page_width = max(b[2] for b in blocks)  # x1 of blocks

        column_width = page_width / num_columns
        sorted_blocks = []

        for col in range(num_columns):
            col_blocks = [b for b in blocks if (b[0] >= col * column_width) and (b[0] < (col + 1) * column_width)]
            col_blocks.sort(key=lambda b: b[1])  # Sort by y0 within the column
            sorted_blocks.extend(col_blocks)
        return sorted_blocks


if __name__ == '__main__':
    url = input.strip()
    processor = PDFProcessor()
    output = processor.process(url)
