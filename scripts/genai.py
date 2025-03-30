from google import genai

client = genai.Client(api_key="AIzaSyCfDiiSYF9Rr2oezb9qHdhos7q8ovZwvo8")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="can you write me a python script to query gemini ai using from google import genai, model is gemini-2.0-flash, also allow me to type my input into the command line rather than editing the script"
)
print(response.text)
