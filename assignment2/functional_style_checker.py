import ast
import os
import re

# function to find the file in the parent directory or its subdirectories
def find_file(filename, root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    raise FileNotFoundError(f"{filename} not found in {root_directory} or its subdirectories.")

# function to generate the report
def generate_report(filename, output_dir):
    # automatically set the root directory to the parent directory of the current working directory
    root_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    
    # search for the file in the parent directory
    filepath = find_file(filename, root_directory)
    
    # read the Python file and parse its AST
    with open(filepath, 'r') as file:
        source_code = file.read()
    tree = ast.parse(source_code)
    
    # prepare the report
    report_lines = []

    # file structure
    total_lines, imports, classes, functions = check_file_structure(filepath)
    report_lines.append("File Structure:")
    report_lines.append(f"Total lines of code: {total_lines}")
    report_lines.append(f"Imported packages: {imports}")
    report_lines.append(f"Classes: {classes}")
    report_lines.append(f"Functions: {functions}")
    report_lines.append("\n")

    # docstring check
    report_lines.append("Doc String Check:")
    report_lines.extend(check_docstrings(tree))
    report_lines.append("\n")

    # type annotation Check
    report_lines.append("Type Annotation Check:")
    report_lines.extend(check_type_annotations(tree))
    report_lines.append("\n")

    # naming convention Check
    report_lines.append("Naming Convention Check:")
    report_lines.extend(check_naming_conventions(tree))
    report_lines.append("\n")

    # write the report to the output directory
    os.makedirs(output_dir, exist_ok=True)
    report_filename = os.path.join(output_dir, f"style_report_{filename}.txt")
    with open(report_filename, 'w') as report_file:
        report_file.write("\n".join(report_lines))
    
    print(f"Style report generated: {report_filename}")

# check file structure (total lines, imports, classes, functions)
def check_file_structure(filepath):
    total_lines = 0
    imports = []
    classes = []
    functions = []
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        for line in lines:
            if line.startswith("import") or line.startswith("from"):
                imports.append(line.strip())
            elif line.strip().startswith("class "):
                class_name = line.split()[1].split('(')[0]
                classes.append(class_name)
            elif line.strip().startswith("def "):
                func_name = line.split()[1].split('(')[0]
                functions.append(func_name)
    
    return total_lines, imports, classes, functions

# check for docstrings in classes and functions
def check_docstrings(tree):
    report = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            name = node.name
            docstring = ast.get_docstring(node)
            if docstring:
                report.append(f"{name}:\n{docstring}")
            else:
                report.append(f"{name}: DocString not found")
    return report

# check if all functions and methods have type annotations
def check_type_annotations(tree):
    report = []
    missing_annotations = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not all(arg.annotation for arg in node.args.args):
                missing_annotations.append(node.name)
    
    if missing_annotations:
        report.append("Functions missing type annotations: " + ", ".join(missing_annotations))
    else:
        report.append("All functions use type annotations.")
    
    return report

# check naming conventions for classes and functions
def check_naming_conventions(tree):
    report = []
    invalid_class_names = []
    invalid_function_names = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            if not re.match(r'[A-Z][a-zA-Z0-9]+$', node.name):
                invalid_class_names.append(node.name)
        elif isinstance(node, ast.FunctionDef):
            if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                invalid_function_names.append(node.name)
    
    if invalid_class_names:
        report.append("Classes with invalid naming conventions: " + ", ".join(invalid_class_names))
    else:
        report.append("All classes follow CamelCase naming conventions.")
    
    if invalid_function_names:
        report.append("Functions with invalid naming conventions: " + ", ".join(invalid_function_names))
    else:
        report.append("All functions follow snake_case naming conventions.")
    
    return report

# main function to execute the program
if __name__ == "__main__":
    # get the filename from user input
    filename = input("Enter the Python file to check (e.g., 'my_file.py'): ").strip()
    
    # define the output directory where the report will be saved
    output_dir = os.path.dirname(os.path.abspath(__file__))  # Save the report in the same directory as the script
    
    # generate the report
    generate_report(filename, output_dir)
