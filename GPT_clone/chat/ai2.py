from decouple import config
from huggingface_hub import InferenceClient

HUGGINGFACE_API_TOKEN = config("HUGGINGFACE_API_TOKEN", cast=str, default=None)

repo_id = "microsoft/Phi-3.5-mini-instruct"

llm_client = InferenceClient(
    model=repo_id,
    token=HUGGINGFACE_API_TOKEN,
)

def get_llm_response(gpt_messages):
    # Construct the prompt from the messages
    prompt = ""
    for message in gpt_messages:
        role = message['role']
        content = message['content']
        prompt += f"{role}: {content}\n"
    
    prompt += "assistant: "  # Add this to prompt the model for a response
    
    try:
        response = llm_client.text_generation(
            prompt,
            max_new_tokens=230,
            return_full_text=False,
        )
        response = response.split("Assistant:", 1)[-1].strip()
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return "I'm sorry, an error occurred while processing your request."




