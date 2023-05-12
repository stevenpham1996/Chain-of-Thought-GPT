import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def generate_response(messages, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    #messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"].strip()

def main(num_options=2):
    user_message = input("Ask LogicGPT a question: ")
    prefixed_message = f"Question: {user_message}.\n Answer: Let's work this out \
    in a step by step way to be sure we have the right answer."
    
    answer_options = []
    for i in range(num_options):
        answer_option = generate_response([
            {"role": "user", "content": prefixed_message},
        ])
        print()
        print()
        print(f"Answer option {i+1}:\n")
        print(answer_option)
        print("---------------------------------------------------")
        answer_options.append(f"Answer option number {i+1}: {answer_option}")
    
    prompt = f"Question: {prefixed_message}\n \
    Answers: {answer_options}"
    prompt += f"\n\nBased on the {num_options} answer options provided, \
    as a thoughtful thinker, you are tasked to identify the one answer option \
    whose chain of thoughts is the most logical or consistent, \
    correct any flaws and faulty logic that may still exist, \
    then discuss the one final improved answer in depth. \
    Let's work this out in a step by step way to make sure we achieve our objective:"
    response = generate_response([
        {"role": "user", "content": prompt},x
    ])
    print()
    print()
    print("LogicGPT's response:\n")
    print(response)


    
if __name__ == "__main__":
    main()