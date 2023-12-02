import autogen

config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST.json")

gpt4_config = {
    "seed": 42,  # change the seed for different trials
    "temperature": 0,
    "config_list": config_list_gpt4,
    "request_timeout": 120,
}