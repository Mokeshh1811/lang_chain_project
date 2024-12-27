from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
load_dotenv()
memory=ConversationBufferWindowMemory(k=2)
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
conversation=ConversationChain(llm=llm,memory=memory)
while True:
    user_input=input("\n Mokesh:")
    if user_input.lower() in ['bye', 'exit']:
        print("bye")
        print(conversation.memory.buffer)
        break
    response=conversation.predict(input= user_input)
    print("\n AI:",response)