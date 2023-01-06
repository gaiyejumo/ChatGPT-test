import openai

# Set up the OpenAI API client
openai.api_key = "YOUR_API_KEY"

# Set the prompt for the model
prompt = "What is your favorite color?"

# Use the ChatGPT model to generate a response to the prompt
response = openai.Completion.create(
  engine="chatgpt",
  prompt=prompt,
  temperature=0.5,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Print the generated response
print(response.text)
