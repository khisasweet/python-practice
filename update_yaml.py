
import yaml

def set_state(state):
    file_name = "file_to_edit.yaml"
    with open(file_name) as f:
        doc = yaml.safe_load(f)
    doc['state'] = state
    with open(file_name, 'w') as f:
        yaml.safe_dump(doc, f, default_flow_style=False)


set_state("true")
