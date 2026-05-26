from dotenv import load_dotenv
from langchain_groq import ChatGroq

def test_groq_api():
    load_dotenv()
    
    try:
        # Initialize Groq client
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
        
        # Make a simple test call
        response = llm.invoke("Say 'Hello, Groq API is working!' and nothing else.")
        
        print("✅ Groq API Key is valid!")
        print(f"Response: {response.content}")
        return True
        
    except Exception as e:
        print(f"❌ Groq API Key test failed: {e}")
        return False


if __name__ == "__main__":
    test_groq_api()
