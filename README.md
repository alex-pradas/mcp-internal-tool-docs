# internal-tool-docs-mcp

A lightweight MCP server that serves `llms.txt` API documentation for internal packages.

## Install

```bash
pip install internal-tool-docs-mcp
```

## Usage

Place your package documentation files in a directory, named `<package-name>.txt`:

```
docs/
├── ductile-loads.txt
├── my-other-tool.txt
```

Run the server:

```bash
internal-tool-docs-mcp --path ./docs
```

Or via `uvx` (no install needed):

```bash
uvx internal-tool-docs-mcp --path ./docs
```

## Configure in `.mcp.json`

```json
{
  "mcpServers": {
    "internal-tool-docs": {
      "command": "uvx",
      "args": ["internal-tool-docs-mcp", "--path", "./docs"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `list_packages()` | List available package documentation |
| `get_package_docs(package_name)` | Get the llms.txt content for a package |

## License

MIT
