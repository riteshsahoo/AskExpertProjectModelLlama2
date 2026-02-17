class AskExpertApp:
    def __init__(self):
        # Initialize the application
        self.experts = []
        self.questions = []

    def ask_expert(self, question):
        # Logic to ask an expert
        self.questions.append(question)
        # Here you would typically interact with experts and collect answers
        return f'Expert answer for: {question}'

    def chat_loop(self):
        # Loop to handle chatting session
        while True:
            user_input = input('You: ')
            if user_input.lower() in ['exit', 'quit']:
                break
            response = self.ask_expert(user_input)
            print(f'Expert: {response}')