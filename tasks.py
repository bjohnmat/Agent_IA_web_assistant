# tasks.py

from invoke import task
from agent import load_environment, get_agent

@task
def ask(ctx, query=None):
    """
    Pose une question à l'agent LangChain.
    Ex: invoke ask --query="What's the weather in Tokyo?"
    """
    try:
        load_environment()
        agent = get_agent()
        if query:
            response = agent.run(query)
            print("\n🤖 Agent Response:\n", response)
        else:
            print("💬 Mode interactif (tape 'exit' pour quitter)")
            while True:
                user_input = input("🧠> ")
                if user_input.lower() in ("exit", "quit"):
                    print("👋 Fin.")
                    break
                try:
                    result = agent.run(user_input)
                    print("\n🤖 Réponse:\n", result)
                except Exception as err:
                    print(f"❌ Erreur: {err}")
    except Exception as e:
        print(f"🚨 Échec de l'initialisation: {e}")
