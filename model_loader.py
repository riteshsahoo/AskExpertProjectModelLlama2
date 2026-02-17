import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class Llama2ModelLoader:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def load_model(self):
        # Ensuring the model is in evaluation mode
        self.model.eval()

    def generate_response(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model.generate(**inputs)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

# Example usage:
# loader = Llama2ModelLoader('meta-llama/Llama-2-7b')
# loader.load_model()
# response = loader.generate_response('Hello, how are you?')
# print(response)