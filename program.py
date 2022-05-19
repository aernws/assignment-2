import yaml
import json

if(in.ext1 = jsonfile){
    data = json.load(in.ext1)
    yaml_data = yaml.dump(data) 
    print(out.ext2, yaml_data)
}
if(in.ext2 = yamlfile){
    data = yaml.load(in.ext1)
    json_data = json.dump(data)
    print(out.ext2, json_data)
}

