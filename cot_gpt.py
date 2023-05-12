import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def generate_response(messages, model="gpt-3.5-turbo", temperature=0.5): 
    #messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"].strip()

def main(num_options=3):
    user_message = input("Ask CoT-GPT a question: ")
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
    
    researcher_prompt = f"Question: {prefixed_message}\n \
    Answers: {answer_options}"
    researcher_prompt += f"\n\nBased on the {num_options} answer options provided, \
    you are tasked with investigating the flaws and faulty logics of each answer option.\
    Let's work this out in a step by step way to be sure we indentify all the errors:"
    researcher_response = generate_response([
        {"role": "user", "content": researcher_prompt},
    ])
    print()
    print()
    print("Researcher's response:\n")
    print(researcher_response)


    resolver_prompt = f"Question: {prefixed_message}\n \
    Answers: {answer_options}\n \
    Researcher's Response: {researcher_response}"
    resolver_prompt += f"\n\n You are a resolver taksed with finding which of the {num_options} answer options \
    the Reseacher thought was best, improving upon it and elaborate the improved answer in full.\
    Let's work this out in a step by step way to be sure we indentify all the errors:"           
    resolver_response = generate_response([
        {"role": "user", "content": resolver_prompt},
    ])
    print("---------------------------------------------------")
    print()
    print()
    print("Resolver's response:\n")
    print(resolver_response)
    
if __name__ == "__main__":
    main()
