import requests
import json
from color import Color

# personal access token generated in Figma. User needs to be a member of an enterprise org to read from variables
# endpoints and an editor to post
access_token='PAT_HERE'
# key of the figma file we want to retrieve values from
file_key='FILE_KEY'

base_url='https://api.figma.com/v1/'
endpoint=f"files/{file_key}/variables/local"
headers={
    'X-FIGMA-TOKEN': access_token
}

output_css_file_name="demo_figma_css_extraction.scss"

response = requests.get(f"{base_url}{endpoint}", headers=headers)

variable_collections=response.json()['meta']['variables']

# extend this list with desired types
figma_types_and_keys_to_extract = {'COLOR': '26:0'}

output_variables=[]

for variable in variable_collections.values():
    try:
        if variable['resolvedType'] in figma_types_and_keys_to_extract.keys():
            if variable['resolvedType'] == 'COLOR':
                r,g,b,a = variable['valuesByMode'][figma_types_and_keys_to_extract[variable['resolvedType']]].values()

                output_variables.append(Color(
                    variable['name'],
                    r,
                    g,
                    b,
                    a,
                    description=variable['description']
                ))
            elif False:
                # additional types here, e.g. padding
                pass
                
    except Exception as e:
        print(f"error parsing {json.dumps(variable), e}")

f = open(output_css_file_name, 'w')

f.write(":root{ \n")

for variable in output_variables:
    f.write(f"\t{variable.to_css()}\n")

f.write("}")

f.close()

