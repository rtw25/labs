import ast
import os
import re

class StyleChecker:
    def __init__(self, filename):
        # Set the root directory to the parent directory of the current working directory
        root_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.filepath = self.find_file(filename, root_directory)
        self.tree = None
        self.load_file()

    def find_file(self, filename, root_directory):
        # Searches directories to find the file
        for dirpath, _, filenames in os.walk(root_directory):
            if filename in filenames:
                return os.path.join(dirpath, filename)
        raise FileNotFoundError(f"{filename} not found in {root_directory} or its subdirectories.")

    def load_file(self):
        with open(self.filepath, 'r') as file:
            self.tree = ast.parse(file.read())

    def generate_report(self):
        report_lines = []

        # File Structure
        file_structure = FileStructureChecker(self.filepath)
        report_lines.append("File Structure:")
        report_lines.append(f"Total lines of code: {file_structure.total_lines}")
        report_lines.append(f"Imported packages: {file_structure.imports}")
        report_lines.append(f"Classes: {file_structure.classes}")
        report_lines.append(f"Functions: {file_structure.functions}")
        report_lines.append("\n")

        # Doc String Check
        doc_checker = DocStringChecker(self.tree)
        report_lines.append("Doc String Check:")
        report_lines.extend(doc_checker.get_docstring_report())
        report_lines.append("\n")

        # Type Annotation Check
        type_checker = TypeAnnotationChecker(self.tree)
        report_lines.append("Type Annotation Check:")
        report_lines.extend(type_checker.get_type_annotation_report())
        report_lines.append("\n")

        # Naming Convention Check
        naming_checker = NamingConventionChecker(self.tree)
        report_lines.append("Naming Convention Check:")
        report_lines.extend(naming_checker.get_naming_convention_report())
        report_lines.append("\n")

        # Write to file
        report_path = f"style_report_{os.path.basename(self.filepath)}.txt"
        with open(report_path, 'w') as report_file:
            report_file.write("\n".join(report_lines))
        print(f"Report generated: {report_path}")

class FileStructureChecker:
    def __init__(self, filepath):
        self.filepath = filepath
        self.total_lines = 0
        self.imports = []
        self.classes = []
        self.functions = []
        self.check_file_structure()

    def check_file_structure(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
            self.total_lines = len(lines)
            for line in lines:
                if line.startswith("import") or line.startswith("from"):
                    self.imports.append(line.strip())
                elif line.strip().startswith("class "):
                    class_name = line.split()[1].split('(')[0]
                    self.classes.append(class_name)
                elif line.strip().startswith("def "):
                    func_name = line.split()[1].split('(')[0]
                    self.functions.append(func_name)

class DocStringChecker:
    def __init__(self, tree):
        self.tree = tree

    def get_docstring_report(self):
        report = []
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                name = node.name
                docstring = ast.get_docstring(node)
                if docstring:
                    report.append(f"{name}:\n{docstring}")
                else:
                    report.append(f"{name}: DocString not found")
        return report

class TypeAnnotationChecker:
    def __init__(self, tree):
        self.tree = tree

    def get_type_annotation_report(self):
        report = []
        missing_annotations = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if not all(arg.annotation for arg in node.args.args):
                    missing_annotations.append(node.name)
        if missing_annotations:
            report.append("Functions missing type annotations: " + ", ".join(missing_annotations))
        else:
            report.append("All functions use type annotations.")
        return report

class NamingConventionChecker:
    def __init__(self, tree):
        self.tree = tree

    def get_naming_convention_report(self):
        report = []
        invalid_class_names = []
        invalid_function_names = []

        for node in ast.walk(self.tree):
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

# Usage example
if __name__ == "__main__":
    filename = "lab05.py"  # Replace with your target file name
    checker = StyleChecker(filename)
    checker.generate_report()  # Report will generate in the working directory
