## For contributors: Checking if YAML syntax is correct.

The following section describes how to check if your YAML schema for LinkML is correct.
This can be done by generating all artifacts that are required by the __GHGA metadata environment__

Everything is orchestrated by a generic single [Makefile](Makefile). For this to work you should follow certain conventions:

 * Keep your schema in src/schema
 * Use the `.yaml` suffix for all schema files
 * Use the suggested directory layout here.

To run the Makefile you will need Python (>=3.7), and linkml. You can type:

```bash
make install
```

or equivalently

```bash
. environment.sh
pip install -r requirements.txt
```

You can make all targets with

```bash
make all
```
