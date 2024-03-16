from html.parser import HTMLParser
import yaml


class HtmlValidator(HTMLParser):

    def __init__(self, criteria_file):
        super().__init__()
        self.criteria = self.load_criteria(criteria_file)
        self.results = {
            'startElements': [],
            'endElements':[],
            'data':[],
            'classes': []
        }

    #loading the required criteria
    def load_criteria(self, criteria_file):
        try:
            with open(criteria_file, 'r') as f:
                return yaml.safe_load(f)  # Or use appropriate loader
        except (IOError, yaml.YAMLError) as e:
            raise ValueError(f"Error loading criteria from '{criteria_file}': {e}")

    #handling starttag
    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.criteria['html']['elements']:
            self.results['startElements'].append(f"Element '{tag}' found")
            
        for attr, value in attrs:
            if attr.lower() == 'class':
                # Iterate over space-separated classes in the value
                for cls in value.split():
                    if cls in self.criteria['html']['classes']:
                        self.results['classes'].append(f"Class '{cls}' found in '{tag}' element")


    # handling endtag
    def handle_endtag(self, tag):
        if tag.lower() in self.criteria['html']['elements']:
            self.results['endElements'].append(f"Element '{tag}' found")

    # handling data 
    def handle_data(self, data):
        if data.lower() in self.criteria['html']['data']:
            self.results['data'].append(f"data '{data}' found")


    def get_results(self):
        return self.results


# Example usage (replace with your actual logic in validator.py)
if __name__ == "__main__":
    criteria_file = "criteria.yaml"  # Or your chosen config file path
    html_validator = HtmlValidator(criteria_file)
    html_filepath = "index.html"  # Replace with actual HTML file path
    html_validator.feed(open(html_filepath, 'r').read())
    html_results = html_validator.get_results()

    # Print or process validation results
    print("**HTML Validation Results:**")
    for result_type, details in html_results.items():
        print(f"\t-{result_type.upper()}")
        for detail in details:
            print(f"\t\t{detail}")
