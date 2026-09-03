import google.genai as genai, inspect
print([m for m in dir(genai.Client) if 'chat' in m.lower() or 'response' in m.lower()])
print(inspect.signature(genai.Client))
