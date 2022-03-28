# Getting started

Install the requirements

```bash
pip install mkdocs mkdocs-material
```

Serve a development version:

```bash
mkdocs serve
```

Build the website:

```bash
mkdocs build
```

## AirTable Integration

Get all jobs posted to AirTable, format them as markdown and add them to `jobs.md`

```sh
export EMEATECH_AIRTABLE_API_KEY=''

make Makefile
```
