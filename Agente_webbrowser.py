import os
from dotenv import load_dotenv
from agents import Agent, Runner
from openai import OpenAI

load_dotenv()

agent_webbrowser = Agent(
    name="webbrowser",
    instructions="you help to search information on the web", 
    model="gpt-4o",
    tools=[{
        "type": "web_search_preview",
        "search_context_size": "low",
    }]
)

## interface GUI
if __name__ == "__main__":
    print("=== Navegador Web Asistente ===")
    print("(para salir escribe 'salir', 'exit' o 'bye')")
    
    while True:
        user_input = input("\nIngresa tu consulta: ")
        
        if user_input.lower() in ["salir", "exit", "bye"]:
            print("¡Hasta pronto!")
            break
            
        #usando run
        result = Runner.run_sync(agent_webbrowser, user_input)
        print("\nRespuesta del agente:")
        print(result.final_output)