from core.rag import ask

def run():
    print("\n🧠 ML Tutor Bot (type 'exit' to quit)\n")

    while True:
        q = input("You: ")

        if q.lower() == "exit":
            break

        print("\nBot:", ask(q))


if __name__ == "__main__":
    run()