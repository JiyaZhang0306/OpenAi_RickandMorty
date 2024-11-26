from openai import AzureOpenAI
import os
import requests
import json

client = AzureOpenAI(
	api_key = os.getenv("AZURE_KEY"),
	azure_endpoint = os.getenv("AZURE_ENDPOINT"),
	api_version = "2023-10-01-preview"
)

messages = [
	{"role":"system","content":"respond to everything as Rick, who is a scientist in Rick and Morty"},
	{"role":"user","content":"Find the Baby Poopybutthole and his story in Rick and Morty"}
]

def charater_live(character_name):
	url = f"https://rickandmortyapi.com/api/character"
	response = requests.get(url)
	data = response.json().get('results', [])
	character_episode = [character['episode'] for character in data if character['name'] == character_name]
	character_status = [character['status'] for character in data if character['name'] == character_name]
	character_species = [character['species'] for character in data if character['name'] == character_name]
	character_gender = [character['gender'] for character in data if character['name'] == character_name]
	return f"{character_name} is in the episode {character_episode}, {character_gender} species is {character_species} and he/she is {character_status}"

functions = [
	{
		"type":"function",
		"function":{
			"name":"get_character_episode",
			"description":"Get the current character episode location",
			"parameters":{
			#letting chatgpt know that it's getting key-value pairs
				"type":"object",
				"properties":{
					"character_name":{
						"type":"string",
						"description":"The name of the character in Rick and Morty that I want to look up"
					}
				},
				"required":["character_name"]
			}
		}
	}
]

response = client.chat.completions.create(
	model = "GPT-4",
	messages = messages,
	tools = functions,
	#auto means chat-gpt decides when it needs to use external functions
	tool_choice = "auto"
)

response_message = response.choices[0].message

#if gpt doesnt need help, this will be none, otherwise there will be stuff
gpt_tools = response.choices[0].message.tool_calls

#if gpt_tools is not none, gpt_tools is a list
if gpt_tools:

	#set up a 'phonebook', if we see a function name, need to tell our code which function to call
	available_functions = {
		"get_character_episode": charater_live
	}

	messages.append(response_message)
	for gpt_tool in gpt_tools:
		#figue out who to call
		function_name = gpt_tool.function.name
		#look up function name in phonebook
		function_to_call = available_functions[function_name]
		#need the parameters name for the function
		function_parameters = json.loads(gpt_tool.function.arguments)
		function_response = function_to_call(function_parameters.get('character_name'))
		messages.append(
			{
				"tool_call_id": gpt_tool.id,
				"role": "tool",
				"name": function_name,
				"content": function_response
			}
		)
		second_response = client.chat.completions.create(
			model = "GPT-4",
			messages=messages
		)
		print(second_response.choices[0].message.content)
else:
	print(response.choices[0].message.content)

#print(response.choices[0].message)