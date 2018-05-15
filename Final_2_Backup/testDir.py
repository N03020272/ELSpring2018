import os

txt_files = [f for f in os.listdir('.') if f.endswith('.json')]
if len(txt_files) != 1:
	raise ValueError('should only be one JSON file here, found many')

filename = txt_files[0]

print(filename)
