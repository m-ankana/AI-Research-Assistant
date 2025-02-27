from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "t5-small"


def load_model(model_name):
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    return tokenizer, model

def summarise_text(text, max_length=150):
    input_text = "summarise : " + text
    tokenizer, model = load_model(model_name)

    inputs = tokenizer(input_text, return_tensors = "pt", max_length = 512, truncation=True)

    summary_ids = model.generate(inputs["input_ids"], max_length = max_length, min_length = 50, length_penalty = 2.0, num_beams = 4, early_stopping = True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens = True)

    return summary 