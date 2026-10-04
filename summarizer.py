from google import genai

client = genai.Client("YOUR_API_KEY_HERE")

print("=== Text Summarizer (type 'quit' to exit) ===")

while True:
    text = input("\nPaste text to summarize: ")
    if text.lower() == "quit":
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Summarize this in 2-3 sentences:\n\n{text}"
    )

    print("\nSummary:")
    print(response.text)