from langchain.chains.conversation.memory import ConversationSummaryMemory

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.chains import ConversationChain

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

memory = ConversationSummaryMemory(

llm=llm,

return_messages = True,

max_token_limit = 200)

conversation= ConversationChain (llm = llm, memory= memory)

while True:
    user_input = input("\n Mokesh:")

    if user_input.lower() in ['bye', 'exit']:
        print("Bye")
        print(conversation.memory.buffer)
        break
    response = conversation.predict(input = user_input)
    print("\n AI: ", response)











