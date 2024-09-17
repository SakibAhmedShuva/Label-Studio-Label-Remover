import json

def remove_labels_from_annotations(file_path, labels_to_remove, output_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    def remove_labels(annotations, labels_to_remove):
        for annotation in annotations:
            if 'result' in annotation:
                annotation['result'] = [res for res in annotation['result'] if not any(label in res['value']['labels'] for label in labels_to_remove)]
        return annotations

    for item in data:
        if 'annotations' in item:
            item['annotations'] = remove_labels(item['annotations'], labels_to_remove)

    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage:
file_path = r'c:\Users\Sakib Ahmed\Documents\USA.json'  # Replace with your input file path
labels_to_remove = ["Issue_Date", "DOB", "Expiration", "Revision_Date"]  # Add any labels you want to remove
output_path = 'output.json'

remove_labels_from_annotations(file_path, labels_to_remove, output_path)