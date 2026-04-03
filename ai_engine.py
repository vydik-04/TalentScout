import requests

def chat_with_ai(messages):
    url = "http://127.0.0.1:11434/api/chat"
    payload = {
        "model": "llama3", # Double check this matches 'ollama list'
        "messages": messages,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        
        # Check if the HTTP request actually worked
        response.raise_for_status() 
        
        data = response.json()
        return data.get("message", {}).get("content", "⚠️ AI response error")
        
    except requests.exceptions.RequestException as e:
        print(f"Ollama Connection Error: {e}")
        raise Exception("Could not connect to the local AI server. Is Ollama running?")
    except KeyError:
        print(f"Unexpected Response Format: {data}")
        raise Exception("The AI returned an unexpected response format.")