# Chain-of-Thought-GPT

This python script utilizes the Chain-of-thought (CoT) prompting method highlighted in the paper published in the 4th of May, 2023 titled: [An automatically discovered chain-of-thought prompt generalizes to novel models and datasets](https://arxiv.org/abs/2305.02897) which significantly improves the performance of ChatGPT's outputs.

### Note:
Due to the OpenAI's free API requests per minute is limited to 3, the default argument of each thought | prompt is set to 1. 

### Some important details from the paper:

- Chain-of-thought (CoT) prompting is a new method for improving the performance of LLMs.  
CoT prompting works by first identifying the chain of thoughts that led to the LLM's output.  
Once the chain of thoughts has been identified, it is then evaluated to see if it is logical and consistent.  
If the chain of thoughts is not logical or consistent, it is then modified to make it so.  
The paper evaluated the proposed method on a variety of tasks, including question answering, summarization, and translation.
- The results showed that the proposed method was able to significantly improve the performance of LLMs on these tasks.  
The paper concludes by discussing the implications of the proposed method.  
The authors argue that the proposed method can be used to improve the performance of LLMs on a variety of tasks.  
They also argue that the proposed method can be used to make LLMs more human-like in their reasoning.
