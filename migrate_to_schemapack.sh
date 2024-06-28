#!/bin/bash

set -e



# directory where the final schemapack build sits and create README
mkdir build
touch build/README.md

migration_scripts=("scripts/extract_relationships.py" "scripts/extract_class_content.py" "scripts/linkml_to_schemapack.py" "scripts/build_resolved_schemapack.py")

# run python scripts
for script in "${migration_scripts[@]}"; do
    echo "Running $script..."
    python $script
done

# clean up repository

to_delete=("rename_properties.py" "mkdocs.yml" "environment.sh" "changelog.md" \
".linkml_linter.yaml" ".erdiagrams.yaml" "src/schema/submission.yaml" "spreadsheets" \
"scripts/update_entity_relations.py" "scripts/schema_linter.py" "scripts/generate_xlsx.py" \
"scripts/generate_linkml_docs.py" "docs" ".github/workflows/check_spreadsheets.yaml" \
".github/workflows/check_schema.yaml" ".github/workflows/check_erdiagrams.yaml" \
".github/workflows/build-documentation.yml")

# Delete the specified files
for item in "${to_delete[@]}"; do
    if [ -f $item ]; then
        echo "Deleting file: $item..."
        rm $item
    elif [ -d $item ]; then
        echo "Deleting directory: $item..."
        rm -r $item
    else
        echo "File $item not found, skipping..."
    fi
done

echo "All scripts have been executed and outdated files have been deleted."
