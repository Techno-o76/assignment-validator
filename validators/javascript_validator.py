import yaml
from slimit.parser import Parser
from slimit.visitors import nodevisitor

class JavaScriptValidator:

    def __init__(self, criteria_file):
        self.criteria = self.load_criteria(criteria_file)
        self.results = []

    def load_criteria(self, criteria_file):
        try:
            with open(criteria_file, 'r') as f:
                return yaml.safe_load(f)
        except (IOError, yaml.YAMLError) as e:
            raise ValueError(f"Error loading criteria from '{criteria_file}': {e}")

    def validate_javascript(self, js_code):
        parser = Parser()
        tree = parser.parse(js_code)

        for func_name, expected_args in self.criteria['javascript'].items():
            found_function = False
            for node in nodevisitor.visit(tree):
                if hasattr(node, 'identifier') and node.identifier.value == func_name:
                    found_function = True
                    if hasattr(node, 'parameters') and len(node.parameters) != len(expected_args):
                        self.results.append(f"Function '{func_name}' has incorrect number of arguments")
                    break

            if not found_function:
                self.results.append(f"Function '{func_name}' not found")

    def get_results(self):
        return self.results


if __name__ == "__main__":
    criteria_file = "criteria.yaml"  # Replace with your actual criteria file path
    js_validator = JavaScriptValidator(criteria_file)

    # Read your JavaScript content (replace with your logic)
    with open("script.js", 'r') as f:
        js_code = f.read()

    js_validator.validate_javascript(js_code)
    results = js_validator.get_results()

    # Print or process validation results
    if results:
        print("**JavaScript Validation Results:**")
        for result in results:
            print(f"\t- {result}")
    else:
        print("JavaScript validation successful! All required functions found.")
