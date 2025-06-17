import json
import os
from urllib.parse import urlparse

def get_namespace(uri):
    if '#' in uri:
        return uri.rsplit('#', 1)[0] + '#'
    else:
        return uri.rsplit('/', 1)[0] + '/'

def split_context_by_namespace(context):
    namespaces = {}
    for term, definition in context.items():
        if isinstance(definition, dict) and '@id' in definition:
            ns = get_namespace(definition['@id'])
            namespaces.setdefault(ns, {})[term] = definition
        elif isinstance(definition, str):
            ns = get_namespace(definition)
            namespaces.setdefault(ns, {})[term] = definition
        else:
            continue
    return namespaces

def infer_json_schema_property(definition):
    """Convert a context definition to a JSON Schema property."""
    if isinstance(definition, str):
        return {"type": "string"}  # Default simple mapping

    type_hint = definition.get('@type', 'string')

    if type_hint == '@id':
        return {"type": "string", "format": "uri"}
    elif type_hint in ['xsd:date', 'http://www.w3.org/2001/XMLSchema#date']:
        return {"type": "string", "format": "date"}
    elif type_hint in ['xsd:dateTime', 'http://www.w3.org/2001/XMLSchema#dateTime']:
        return {"type": "string", "format": "date-time"}
    elif type_hint in ['xsd:boolean', 'http://www.w3.org/2001/XMLSchema#boolean']:
        return {"type": "boolean"}
    elif type_hint in ['xsd:integer', 'http://www.w3.org/2001/XMLSchema#integer']:
        return {"type": "integer"}
    elif type_hint in ['xsd:decimal', 'xsd:float', 'http://www.w3.org/2001/XMLSchema#float']:
        return {"type": "number"}
    else:
        return {"type": "string"}

def create_json_schema_for_namespace(terms, namespace):
    properties = {}
    for term, definition in terms.items():
        properties[term] = infer_json_schema_property(definition)

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": f"Schema for namespace {namespace}",
        "type": "object",
        "properties": properties,
        "additionalProperties": True
    }
    return schema

def save_outputs(namespaces, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for ns, terms in namespaces.items():
        safe_ns = ns.replace("://", "_").replace("/", "_").replace("#", "_")

        # Save context file
        context_filename = os.path.join(output_dir, f"context_{safe_ns}.json")
        with open(context_filename, 'w', encoding='utf-8') as f:
            json.dump({'@context': terms}, f, indent=2)
        print(f"Saved context: {context_filename}")

        # Save schema file
        schema = create_json_schema_for_namespace(terms, ns)
        schema_filename = os.path.join(output_dir, f"schema_{safe_ns}.json")
        with open(schema_filename, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2)
        print(f"Saved schema: {schema_filename}")

def main(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    context = data.get('@context', data)

    if not isinstance(context, dict):
        raise ValueError("Expected a dictionary for the @context")

    namespaces = split_context_by_namespace(context)
    save_outputs(namespaces, output_dir)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Split JSON-LD context by namespace and generate JSON Schemas.")
    parser.add_argument("input_file", help="Path to the JSON-LD context file")
    parser.add_argument("output_dir", help="Directory to save output files")
    args = parser.parse_args()

    main(args.input_file, args.output_dir)
