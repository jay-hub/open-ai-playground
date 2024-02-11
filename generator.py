from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

import constants as const

client = OpenAI(api_key=const.API_KEY)


def ask_away(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Write a meaningful sentence with the word '{prompt}'"
            }
        ]
    )
    return completion.choices[0].message


def ask_recipie_idea(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"A delicious recipie that I can make with '{prompt}'"
            }
        ]
    )
    return completion.choices[0].message


if __name__ == "__main__":
    # input_text: str = input('What is the word you like to see in a sentence? ')
    input_text: str = input('What do you want to see in a recipe? ')
    # chat_reply: ChatCompletionMessage = ask_away(input_text)
    chat_reply: ChatCompletionMessage = ask_recipie_idea(input_text)
    print(chat_reply.content)
