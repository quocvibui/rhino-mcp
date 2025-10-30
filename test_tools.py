#!/usr/bin/env python3
"""
Test script to verify all tools are correctly configured
"""

import sys
sys.path.insert(0, 'src')

from tools.geometry import GEOMETRY_TOOLS
from tools.solids import SOLIDS_TOOLS
from tools.curves import CURVES_TOOLS
from tools.surfaces import SURFACES_TOOLS
from tools.layers import LAYERS_TOOLS
from tools.objects import OBJECTS_TOOLS
from tools.view import VIEW_TOOLS
from tools.document import DOCUMENT_TOOLS


def print_tools_summary():
	"""
	Print summary of all available tools
	"""
	categories = [
		("Geometry", GEOMETRY_TOOLS),
		("Solids", SOLIDS_TOOLS),
		("Curves", CURVES_TOOLS),
		("Surfaces", SURFACES_TOOLS),
		("Layers", LAYERS_TOOLS),
		("Objects", OBJECTS_TOOLS),
		("View", VIEW_TOOLS),
		("Document", DOCUMENT_TOOLS)
	]

	print("=" * 70)
	print("Rhino MCP Server - Tool Summary")
	print("=" * 70)

	total_tools = 0
	for category_name, tools in categories:
		print(f"\n{category_name} Tools ({len(tools)}):")
		print("-" * 70)
		for tool in tools:
			print(f"  - {tool.name}: {tool.description}")
			total_tools += 1

	print("\n" + "=" * 70)
	print(f"Total Tools Available: {total_tools}")
	print("=" * 70)


if __name__ == "__main__":
	print_tools_summary()
