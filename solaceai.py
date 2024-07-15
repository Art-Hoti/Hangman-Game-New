from transformers import pipeline, set_seed

def main():
    # Set seed for reproducibility
    set_seed(42)

    # Create a conversational pipeline with the DialoGPT model
    chatbot = pipeline('text-generation', model='microsoft/DialoGPT-medium')

    # Example conversation prompts and responses
    conversation_prompts = [
        "Hello, how are you?",
        "What's the weather like today?",
        "Tell me about your hobbies.",
    ]

    # Generate and print responses for each prompt
    for prompt in conversation_prompts:
        print(f"User: {prompt}")
        response = chatbot(prompt, max_length=100, num_return_sequences=1, truncation=True, pad_token_id=50256)
        generated_text = response[0]['generated_text'].replace(prompt, '').strip()
        print(f"Chatbot: {generated_text}")
        print()

if __name__ == "__main__":
    main()
