def format_test_answer(tast_prompt,query, history):
    prompt = ""
    if history == ():
            prompt += f"{tast_prompt}\n\nQ: {query}\n A:"
    else:    
            for i, (old_query, response) in enumerate(history):    
                if i == 0:  
                    prompt += f"{tast_prompt}\n\nQ: {old_query} \nA:{response} \n\n"
                else:
                    prompt += f"Q: {old_query} \n A:{response} \n\n"
            prompt += f"Q: {query} \n A:"
    return prompt

def format_vicuna_answer(tast_prompt,query, history):
    prompt = ""
    if history == ():
            prompt += f"<s>USER: \n\n{tast_prompt}\n\nQ: {query} \n ASSISTANT: A:"
    else:    
            for i, (old_query, response) in enumerate(history):    
                if i == 0:  
                    prompt += f"<s>USER: \n\n{tast_prompt}\n\nQ: {old_query} \n ASSISTANT: A:{response} \n\n</s>"
                else:
                    prompt += f"<s>USER: Q: {old_query} ASSISTANT: A:{response} \n\n</s>"
            prompt += f"<s>USER: Q: {query} ASSISTANT: A:"
    return prompt

Llama2_OVERALL_INSTRUCTION = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."

def format_llama2_answer(tast_prompt,query, history):
    if history == ():
            prompt += f"<s>[INST] <<SYS>>\n\n{Llama2_OVERALL_INSTRUCTION}\n\n{tast_prompt}\n\n<</SYS>>\n\nQ: {query} [/INST]\n\nA:  "
    else:    
            for i, (old_query, response) in enumerate(history):
                if i == 0: 
                    prompt += f"<s>[INST] <<SYS>>\n\n{Llama2_OVERALL_INSTRUCTION}\n\n{tast_prompt}\n\n<</SYS>>\n\n Q: {old_query} [/INST]A:  {response} </s>"
                else:
                    prompt += f"<s>[INST] Q: {old_query}\n\n [/INST]\n\nA:  {response} </s>"
            prompt += f"<s>[INST]\n\n Q: {query} \n\n[/INST]\n\nA: "
    return prompt




from typing import (
    AbstractSet,
    cast,
    Collection,
    Dict,
    Iterator,
    List,
    Literal,
    Sequence,
    TypedDict,
    Union,
)

Role = Literal["user", "assistant"]


class Message(TypedDict):
    role: Role
    content: str


Dialog = Sequence[Message]

class ChatFormat:
    def __init__(self):
        self.input = ""

    def add_header(self, message: Message):
        tokens = []
        tokens.append("<|start_header_id|>")
        tokens.extend(message["role"])
        tokens.append("<|end_header_id|>")
        tokens.extend("\n\n")
        return tokens

    def add_message(self, message: Message):
        tokens = self.add_header(message)
        tokens.extend(message["content"].strip())
        tokens.append("<|eot_id|>")
        return tokens

    def add_dialog_prompt(self, dialog: Dialog):
        tokens = []
        tokens.append("<|begin_of_text|>")
        for message in dialog:
            tokens.extend(self.add_message(message))
        # Add the start of an assistant message for the model to complete.
        tokens.extend(self.add_header({"role": "assistant", "content": "A: "}))
        return "".join(tokens)  # Return a single string concatenated from the list of tokens.





def format_llama3_answer(tast_prompt,query, history):
        format = ChatFormat()

        if history == ():
            dialog = [
                {
                "role": "user",
                "content": tast_prompt+query,
                },
            ]
        else:    
            for i, (old_query, response) in enumerate(history):
                dialog = []
                if i == 0:
                    dialog.extend([
                        {
                            "role": "user",
                            "content": f"{tast_prompt} Q: {old_query}",
                        },
                        {
                            "role": "assistant",
                            "content": f"A: {response}",
                        },
                    ])
                else:
                    dialog.extend([
                        {
                            "role": "user",
                            "content": f"Q: {old_query}",
                        },
                        {
                            "role": "assistant",
                            "content": f"A: {response}",
                        },
                    ])
            dialog.extend([
                {
                    "role": "user",
                    "content": f"Q: {query}",
                },
                ])
        question = format.add_dialog_prompt(dialog)
        return question
