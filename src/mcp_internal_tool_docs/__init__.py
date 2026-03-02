import argparse
from pathlib import Path

from fastmcp import FastMCP


def main():
    parser = argparse.ArgumentParser(
        description="MCP server for llms.txt package documentation"
    )
    parser.add_argument(
        "--path",
        type=Path,
        required=True,
        help="Directory containing llms.txt files (named <package>.txt)",
    )
    args = parser.parse_args()
    docs_dir = args.path.resolve()

    mcp = FastMCP("internal-tool-docs")

    @mcp.tool()
    def list_packages() -> list[str]:
        """List available package documentation."""
        return [f.stem for f in sorted(docs_dir.glob("*.txt"))]

    @mcp.tool()
    def get_package_docs(package_name: str) -> str:
        """Get the llms.txt documentation for a package."""
        file = docs_dir / f"{package_name}.txt"
        if not file.exists():
            available = [f.stem for f in docs_dir.glob("*.txt")]
            raise ValueError(
                f"No documentation for '{package_name}'. Available: {available}"
            )
        return file.read_text()

    mcp.run()
