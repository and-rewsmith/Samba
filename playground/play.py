from transformers import AutoTokenizer

# Change `model_name` to your specific model (e.g., "facebook/llama")
model_name = "facebook/llama"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the tokenizer locally
tokenizer.save_pretrained("data/llama")