import os
from html_validator import HtmlValidator
from css_validator import CssValidator  # Replace with actual import if needed
from javascript_validator import validate_javascript  # Replace with actual import if needed

criteiraPath = "C:/Users/jayes/Desktop/GFG-Project/new"
assignmentPath = "C:/Users/jayes/Desktop/GFG-Project/new/assignment"

def main():
    criteria_file = criteiraPath+"/criteria.yaml"  # Or your chosen config file path

    # Validate HTML
    html_validator = HtmlValidator(criteria_file)
    html_filepath = assignmentPath+"/index.html"  # Replace with actual HTML file path
    html_validator.feed(open(html_filepath, 'r').read())
    html_results = html_validator.get_results()

    # Validate CSS (if needed)
    css_filepath = assignmentPath+"/style.css"  # Replace with actual CSS file path (optional)
    css_results = {}  # Empty dictionary for CSS results (replace with actual call if used)
    if css_filepath:
        css_results = validate_css(css_filepath, criteria_file)  # Replace with actual call

    # Validate JavaScript (if needed)
    javascript_filepath = assignmentPath+"/script.js"  # Replace with actual JavaScript file path (optional)
    javascript_results = {}  # Empty dictionary for JavaScript results (replace with actual call if used)
    if javascript_filepath:
        javascript_results = validate_javascript(javascript_filepath, criteria_file)  # Replace with actual call

    # Print or process validation results
    print("**Web Development Assignment Evaluation**")

    print("\n**HTML Validation Results:**")
    for result_type, details in html_results.items():
        print(f"\t-{result_type.upper()}")
        for detail in details:
            print(f"\t\t{detail}")

    # Print CSS validation results (if applicable)
    if css_filepath:
        print("\n**CSS Validation Results:**")
        print(f"\tValid: {css_results.get('valid', False)}")  # Handle potential missing key
        if css_results.get('messages'):
            print("\tMessages:")
            for message in css_results['messages']:
                print(f"\t\t{message}")

    # Print JavaScript validation results (if applicable)
    if javascript_filepath:
        print("\n**JavaScript Validation Results:**")
        print(f"\tValid: {javascript_results.get('valid', False)}")  # Handle potential missing key
        if javascript_results.get('messages'):
            print("\tMessages:")
            for message in javascript_results['messages']:
                print(f"\t\t{message}")

# Run the main function if executed directly
if __name__ == "__main__":
    main()
