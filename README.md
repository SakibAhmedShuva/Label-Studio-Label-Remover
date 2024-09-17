# Label Studio Text Label or Annotation Remover

This Python script removes specific labels from JSON annotations output from label studio.

## Usage

To use the script, follow the steps below:

1.Export annotations in json format from label studio:


![{51316E63-E75A-41B9-BF8F-DB574CBDA587}](https://github.com/user-attachments/assets/05afb760-ecb0-4308-945b-82ab5604e5f2)



2. Clone the repository
   ```bash
   git clone https://github.com/yourusername/json-label-cleaner.git
   cd json-label-cleaner

3. Modify the file_path, labels_to_remove, and output_path in the script as needed.

4. Run the script:
   ```bash
   python remove_labels.py

Example:

   ```bash
   file_path = r'c:\Users\Sakib Ahmed\Documents\USA.json'  # Replace with your input file path
   labels_to_remove = ["Issue_Date", "DOB", "Expiration", "Revision_Date"]  # Labels to remove
   output_path = 'output.json'

   remove_labels_from_annotations(file_path, labels_to_remove, output_path)
