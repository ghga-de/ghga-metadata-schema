# Testing

When you make changes to the GHGA Metadata Schema, be sure to try and build
the schema using LinkML. This will surface any syntax or structural errors.

To build the schema, run the following:

```sh
# Set up a virtual environment and install dependencies
make install

# Build all the artifacts from the YAML
make all
```
