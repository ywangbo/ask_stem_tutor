from vertexai.language_models import CodeChatModel

code_chat_model = CodeChatModel.from_pretrained("codechat-bison@001")
chat = code_chat_model.start_chat()

def ask_a_question(question: str, temperature: float = 0.5) -> object:

    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
    }

    response = chat.send_message(
        question, **parameters
    )
    #print(f"Response from Model: {response.text}")

    return response.text