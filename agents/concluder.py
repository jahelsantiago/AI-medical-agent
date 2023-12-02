import autogen
from config import gpt4_config

concluder = autogen.AssistantAgent(
    name="Concluder",
    llm_config=gpt4_config,
    system_message='''
    Your task is to conclude the diagnosis of the patient, you should use the information of all the other doctors and write a final diagnosis.
    You should say only the diagnosis and no more than that.
''',
)
