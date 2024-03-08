from openai import OpenAI
client = OpenAI(api_key='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')

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

