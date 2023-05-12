# Chain-of-Thought-GPT

The 2 python scripts utilize a prompting framework which combines the following methods of :  
- the Chain-of-thought (CoT) highlighted in the paper published in the 4th of May, 2023 titled: [An automatically discovered chain-of-thought prompt generalizes to novel models and datasets](https://arxiv.org/abs/2305.02897)
- Reflexion published in the 20th of March, 2023 titled: [Reflexion: an autonomous agent with dynamic memory and self-reflection](https://arxiv.org/abs/2303.11366)
- Dialogue Enabled Resolving Agents in the paper published in the 30th of March, 2023 titled: [DERA: Enhancing Large Language Model Completions with Dialog-Enabled Resolving Agents](https://arxiv.org/abs/2303.17071)  
Alongside with the prompting method "Let’s Work This Out Step By Step..." to significantly boost the quality of ChatGPT's performance.

#### - cot_gpt.py:
Automatically executes a series of prompts following a 3-step framework of asking questions, self-reflection and self-evaluation to arrive at the most optimal answer.

#### - logic_gpt.py:   
For OpenAI free-plan users, which compresses the Reflextion and Dialog steps into 1, due to the OpenAI's free API request per minute limit.
 

## How to:
Create your OpenAI API key at: https://platform.openai.com/account/api-keys  
Save it to an environment variable named `OPENAI_API_KEY` in a .env file     
Run `pip install -r requirement.txt`  
Run `python cot_gpt.py` or `python logic_gpt.py` 
