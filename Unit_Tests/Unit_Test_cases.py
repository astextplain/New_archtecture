from base_classes import LLM

class Unit_Test(LLM):
    def __init__(self, user_prompt, sys_prompt):
        super().__init__(user_prompt, sys_prompt)