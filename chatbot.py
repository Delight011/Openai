from openai import OpenAI


client = OpenAI(api_key="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")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__== "__main__":
   while True:
     user_input = input("Você: ")
     if user_input.lower() in ["quit", "exit", "bye", "sair", "tchau"]:
        break
     
     response = chat_with_gpt (user_input)
     print("Chatbot: ", response)