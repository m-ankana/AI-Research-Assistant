import fitz
import re

def extract_text_pdf(pdf_file):

    
    # input
    # pdf_file: string with file extension .pdf /
    # doc = fitz.open(pdf_file)
    # text = ""

    # for page in doc:
    #     text += page.get_text()+ "\n"

    # return text.strip()
    doc = fitz.open(stream = pdf_file, filetype = "pdf")
    text = "".join([page.get_text("text") for page in doc ])
    
    return text
    
def extract_dynamic_sections(text):
    """
    Dynamically detect and extract sections based on common heading patterns
    """
    # Regex pattern to capture headings - e.g., all uppercase, followed by normal text.
    # You can extend this based on more complex patterns.
    pattern = re.compile(r"([A-Z][A-Za-z0-9\s]+(?=\n))")  # Matches uppercase words (i.e., likely headings)
    headings = re.findall(pattern, text)

    sections = {}
    start = 0  # Start index for the content under each heading

    # Iterate over detected headings
    for heading in headings:
        # Find the start and end of each heading's content
        start_idx = text.lower().find(heading.lower(), start)
        end_idx = text.find("\n", start_idx + len(heading))  # End at the next newline after the heading

        # Extract content for this section, handling the next heading or end of document
        next_heading_index = len(text)
        for next_heading in headings:
            if next_heading.lower() > heading.lower():
                next_heading_start = text.lower().find(next_heading.lower())
                next_heading_index = min(next_heading_index, next_heading_start)

        content = text[start_idx + len(heading):next_heading_index].strip()
        sections[heading] = content
        start = next_heading_index  # Update start for next section

    return sections


def chunk_text(text, chunk_size = 500):
    
    sentences = text.split(".")
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence)<chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."


    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks 


# pdf_text = extract_det("physics.pdf")
# print(pdf_text[:1000])

# print(chunk_text("my name"))

