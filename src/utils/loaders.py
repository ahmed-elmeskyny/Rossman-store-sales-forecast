import yaml 

def load_config(filepath):
    print("opening file")
    try :
        with open(filepath,'r') as file:
            conf = yaml.safe_load(file)
        return conf
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None