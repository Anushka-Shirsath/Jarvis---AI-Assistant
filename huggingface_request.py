from transformers import pipeline

# Load model once
generator = pipeline("text-generation", model="gpt2")

def send_request(messages):
    prompt = messages[-1]["content"]
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]
