import autogen

user_proxy = autogen.UserProxyAgent(
   name="Admin",
   system_message="A human admin. Interact with the physicians to discuss symptoms and other information about the patient.",
   code_execution_config=False,
   human_input_mode="ALWAYS"
)
