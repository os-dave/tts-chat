import sounddevice as sd
from kokoro_onnx import Kokoro
import time
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
kokoro = Kokoro("kokoro-v0_19.onnx", "voices.json")

conversation_history = []
MAX_HISTORY = 20


def chat_with_ai(prompt):
    conversation_history.append({"role": "user", "content": prompt})

    while len(conversation_history) > MAX_HISTORY:
        conversation_history.pop(0)

    messages = [
        {
            "role": "system",
            "content": "You are a friendly AI assistant. Keep your responses very short and concise (1-3 sentences max). Be conversational but brief."
        }
    ] + conversation_history

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=100,
    )

    response = chat_completion.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": response})
    return response


def speak_response(text):
    print("Generating audio response...")
    start_time = time.time()

    samples, sample_rate = kokoro.create(
        text, voice="af_nicole", speed=0.8, lang="en-us"
    )

    generation_time = time.time() - start_time
    print(f"Audio generated in {generation_time:.2f} seconds")
    print("Playing audio...")

    sd.play(samples, sample_rate)
    sd.wait()


def main():
    print("Welcome to the Speaking Chat Interface! (Type 'quit' to exit)")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'quit':
            print("\nGoodbye!")
            break

        if user_input:
            response = chat_with_ai(user_input)
            print("\nAI:", response)

            speak_response(response)


if __name__ == "__main__":
    main()
