from transformers import pipeline

# Initialize the pipelines
summarizer = pipeline("text2text-generation", model="ingeniumacademy/bart-cnn-samsum-finetuned")
question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qa-qg-hl")

def preprocess_input(text):
    """
    Preprocess the input text to merge multiple paragraphs into one.
    """
    # Replace all newlines with a space to merge paragraphs
    return text.replace("\n", " ").strip()

def generate_dynamic_summary(text, min_percentage=0.4, max_percentage=0.5):
    # Preprocess the input text
    text = preprocess_input(text)
    
    # Calculate summary lengths
    input_length = len(text.split())
    min_summary_length = int(input_length * min_percentage)
    max_summary_length = int(input_length * max_percentage)
    
    # Generate the summary with the specified length constraints
    summary_config = {
        "max_length": max_summary_length,
        "min_length": min_summary_length,
        "length_penalty": 2.0
    }
    summary = summarizer(text, **summary_config)
    generated_text = summary[0]['generated_text']
    
    # Ensure the summary ends with a full stop
    if generated_text.endswith("."):
        return generated_text
    else:
        last_dot_index = generated_text.rfind(".")
        if last_dot_index != -1:
            return generated_text[:last_dot_index + 1]
        return generated_text

def generate_questions_and_answers(summary):
    sentences = summary.split('. ')
    qa_pairs = []
    for sentence in sentences:
        if sentence: 
            question = question_generator(f"generate question: {sentence}")[0]['generated_text']
            answer = sentence
            qa_pairs.append((question, answer))
    
    return qa_pairs