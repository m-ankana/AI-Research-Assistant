# from fastapi import FastAPI, File, UploadFile
# from load_model import load_model
# from extract_pdf_det import extract_text_pdf, extract_dynamic_sections, chunk_text


# app = FastAPI()
# model_name = "t5-small"
# tokenizer, model = load_model(model_name)


# @app.post("/summarise")
# async def summarise_pdf(file : UploadFile = File(...)):

#     pdf_bytes = await file.read()
#     text = extract_text_pdf(pdf_bytes)

#     input_text = "You are an expert in summarizing research papers. Summary each section separately with bullet points"
#     chunk_summary = ""
#     chunks = chunk_text(text)

#     for chunk in chunks :
#         inputs = tokenizer( input_text + chunk, return_tensors = "pt", max_length = 512, truncation= True)
#         summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=50, length_penalty=2.0)
#         summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
#         chunk_summary += summary + "\n"


#     return {"summary": chunk_summary}


#     # # Dynamically extract sections based on heading-like patterns
#     # sections = extract_dynamic_sections(text)
#     # print(sections)

#     # # Initialize an empty dictionary to store summaries of sections
#     # section_summaries = {}

#     # for heading, content in sections.items():
#     #     # Chunk the content of the section into smaller parts if needed
#     #     chunks = chunk_text(content, chunk_size=512)

#     #     section_summary = ""
#     #     for chunk in chunks:
#     #         # Process each chunk's content and summarize
#     #         inputs = tokenizer("summarise: " + chunk, return_tensors="pt", max_length=512, truncation=True)
#     #         summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=50, length_penalty=2.0)
#     #         summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     #         section_summary += summary + " "  # Combine summaries of chunks

#     #     # Store the section summary in the dictionary
#     #     section_summaries[heading] = section_summary.strip()

#     # # Return the summaries of each section
#     # return {"section_summaries": section_summaries}



from fastapi import FastAPI, File, UploadFile
from load_model import load_model
from extract_pdf_det import extract_text_pdf, chunk_text

app = FastAPI()
model_name = "t5-small"
tokenizer, model = load_model(model_name)

@app.post("/summarise")
async def summarise_pdf(file: UploadFile = File(...)):

    # Read the PDF bytes
    pdf_bytes = await file.read()
    text = extract_text_pdf(pdf_bytes)

    # Refined input prompt for summarization
    input_text = "You are an expert in summarizing research papers. Provide a concise, informative summary for the following section:"

    chunk_summary = ""
    chunks = chunk_text(text)

    for chunk in chunks:
        # Ensure chunk fits within token limit
        inputs = tokenizer(input_text + "\n" + chunk, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        chunk_summary += summary + "\n"

    return {"summary": chunk_summary.strip()}