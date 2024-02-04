import os
import dotenv
import requests

dotenv.load_dotenv()

API_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

def pipeline():
    # post(self.api_url, headers=self.headers, json=payload, data=data)
    api_url = "https://api-inference.huggingface.co/pipeline/text-generation/mistralai/Mixtral-8x7B-Instruct-v0.1"
    payload = {
        "options": {"wait_for_model": True, "use_gpu": False},
        "inputs": "\n  Use the following pieces of context to answer the query at the end.\n  If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\n  \n\n  Query: hi\n\n  Helpful Answer:\n",
        "parameters": {"temperature": 0.1, "max_new_tokens": 250, "top_p": 0.1},
    }
    return requests.post(api_url, headers={"Authorization": f"Bearer {API_TOKEN}"}, json=payload).json()


def query(payload, model_id, api_token=API_TOKEN):
    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def chat(text: str):
    return query({"inputs": text, "options": {"wait_for_model": True}}, model_id)


model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# This one is not free.
# {'error': 'Model requires a Pro subscription; check out hf.co/pricing to learn more. Make sure to include your HF token in your query.'}
# model_id = "meta-llama/Llama-2-70b-chat-hf"

if __name__ == "__main__":
    prompt = "Write a quick sort function in python"
    response = chat(prompt)
    print(response)
    answer = response[0]["generated_text"][len(prompt) :]
    print(answer)
