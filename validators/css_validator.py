import yaml
from css_parser import parse_stylesheet

class CssValidator:

    def __init__(self, criteria_file):
        self.criteria = self.load_criteria(criteria_file)
        self.results = []

    def load_criteria(self, criteria_file):
        try:
            with open(criteria_file, 'r') as f:
                return yaml.safe_load(f)
        except (IOError, yaml.YAMLError) as e:
            raise ValueError(f"Error loading criteria from '{criteria_file}': {e}")

    def validate_css(self, css_content):
        stylesheet = parse_stylesheet(css_content)

        for selector, expected_props in self.criteria['css'].items():
            matching_declarations = stylesheet.select(selector)
            for declaration in matching_declarations:
                missing_props = [prop for prop, value in expected_props.items()
                                 if not declaration.has_property(prop) or
                                 declaration.get_property(prop) != value]
                if missing_props:
                    self.results.append(f"Selector '{selector}' has missing properties: {', '.join(missing_props)}")

    def get_results(self):
        return self.results


if __name__ == "__main__":
    criteria_file = "criteria.yaml"  # Replace with your actual criteria file path
    css_validator = CssValidator(criteria_file)

    # Read your CSS content (replace with your logic)
    with open("style.css", 'r') as f:
        css_content = f.read()

    css_validator.validate_css(css_content)
    results = css_validator.get_results()

    # Print or process validation results
    if results:
        print("**CSS Validation Results:**")
        for result in results:
            print(f"\t- {result}")
    else:
        print("CSS validation successful! All required properties found.")
