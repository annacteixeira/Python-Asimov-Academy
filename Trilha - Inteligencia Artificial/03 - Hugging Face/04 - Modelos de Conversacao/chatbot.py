from transformers import pipeline

chatbot = pipeline(
    'text-generation', 
    model='Felladrin/Llama-68M-Chat-v1', 
    max_new_tokens=300,
    penalty_alpha=0.5,
    top_k=4
)

# <|im_start|>system
# {system_message}<|im_end|>
# <|im_start|>user
# {user_message}<|im_end|>
# <|im_start|>assistant

system_message = 'You are a helpful artificial intelligence.'
system_prompt = f'<|im_start|>system\n{system_message}<|im_end|>\n'

conversation = system_message

while True:
    

    question = input('What is your question? (write it in English)')
    print('User:', question)
    
    conversation += f'<|im_start|>user\n{question}<|im_end|>\n'
    answer = chatbot(conversation)
    conversation = answer[0]['generated_text']
    
    formatted_answer = conversation.split('<|im_start|>assistant\n')[-1].rstrip('<|im_end|>')
    print('Assistant:', formatted_answer)