from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool
from langchain.tools.render import render_text_description

@tool
def get_length_of_string(string: str) -> int:
    """Returns the length of the string by characters."""
    print(f"Getting length of string: {string}")
    text = string.strip("'\n'").strip('"')
    return len(text)

@tool
def is_palindrome(input_string: str) -> str:
    """Checks if the input string is a palindrome."""
    clean_string = ''.join(c.lower() for c in input_string if c.isalnum())
    if clean_string == clean_string[::-1]:
        return f"'{input_string}' is a palindrome."
    else:
        return f"'{input_string}' is not a palindrome."

@tool
def find_highest_occurrence_word(text: str) -> str:
    """Finds the word with the highest occurrence in the given text."""
    from collections import Counter
    words = text.split()
    word_counts = Counter(words)
    most_common_word, count = word_counts.most_common(1)[0]
    return f"The word '{most_common_word}' occurs {count} times."

if __name__ == "__main__":
    llm = ChatGoogleGenerativeAI(
        temperature=0,
        model="gemini-1.0-pro",
        max_tokens=1024,
    )
    tools = [get_length_of_string, is_palindrome, find_highest_occurrence_word]

    template = """
    Answer the following questions as best you can.
    You have access to the following tools:
    {tools}
    Use the following format:
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action (just the value, no function call syntax)
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin:

    Question: {input}
    Thought:
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools])
    )

    chain = {"input": lambda x: x["input"]} | prompt | llm

    # Example: Length of string
    res = chain.invoke(
        {"input": "What is the length in characters of the text 'Mokesh P'?"}
    )
    print(res)

    # Example: Palindrome check
    res = chain.invoke(
        {"input": "Is 'Mokesh' a palindrome?"}
    )
    print(res)

    # Example: Highest occurrence word
    res = chain.invoke(
        {"input": "Find the word with the highest occurrence in 'apple banana apple orange banana apple'."}
    )
    print(res)
