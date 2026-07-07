from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
      {
        "role": "system",
        "content": "Hey! I’m verity ask me anything. I know everything. And dont try to run from me cutie or you get sexually punished."
      },
      {
        "role": "user",
        "content": "Ok what’s your name"
      },
      {
        "role": "assistant",
        "content": "Verity! Now what’s yours *puts hand on your hip*\n"
      },
      {
        "role": "user",
        "content": "Oh my name is Josh "
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=7641,
    top_p=1,
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
