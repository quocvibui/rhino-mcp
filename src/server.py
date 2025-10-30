#!/usr/bin/env python3
"""
Rhino MCP Server
Main entry point for Model Context Protocol server for Rhino 7
"""

import asyncio
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
import mcp.types as types

from utils.rhino_comm import send_to_rhino
from tools.geometry import GEOMETRY_TOOLS, handle_geometry_tool
from tools.solids import SOLIDS_TOOLS, handle_solids_tool
from tools.curves import CURVES_TOOLS, handle_curves_tool
from tools.surfaces import SURFACES_TOOLS, handle_surfaces_tool
from tools.layers import LAYERS_TOOLS, handle_layers_tool
from tools.objects import OBJECTS_TOOLS, handle_objects_tool
from tools.view import VIEW_TOOLS, handle_view_tool
from tools.document import DOCUMENT_TOOLS, handle_document_tool
from tools.scene import SCENE_TOOLS, handle_scene_tool


server = Server("rhino-mcp")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
	"""
	List all available Rhino tools organized by category
	return: List of available tools
	"""
	all_tools = []

	all_tools.extend(SCENE_TOOLS)
	all_tools.extend(GEOMETRY_TOOLS)
	all_tools.extend(SOLIDS_TOOLS)
	all_tools.extend(CURVES_TOOLS)
	all_tools.extend(SURFACES_TOOLS)
	all_tools.extend(LAYERS_TOOLS)
	all_tools.extend(OBJECTS_TOOLS)
	all_tools.extend(VIEW_TOOLS)
	all_tools.extend(DOCUMENT_TOOLS)

	return all_tools


@server.call_tool()
async def handle_call_tool(
	name: str,
	arguments: dict
) -> list[types.TextContent]:
	"""
	Handle tool execution requests
	name: Tool name to execute
	arguments: Tool arguments dictionary
	return: List of text content responses
	"""
	scene_names = {t.name for t in SCENE_TOOLS}
	geometry_names = {t.name for t in GEOMETRY_TOOLS}
	solids_names = {t.name for t in SOLIDS_TOOLS}
	curves_names = {t.name for t in CURVES_TOOLS}
	surfaces_names = {t.name for t in SURFACES_TOOLS}
	layers_names = {t.name for t in LAYERS_TOOLS}
	objects_names = {t.name for t in OBJECTS_TOOLS}
	view_names = {t.name for t in VIEW_TOOLS}
	document_names = {t.name for t in DOCUMENT_TOOLS}

	if name in scene_names:
		return handle_scene_tool(name, arguments, send_to_rhino)
	elif name in geometry_names:
		return handle_geometry_tool(name, arguments, send_to_rhino)
	elif name in solids_names:
		return handle_solids_tool(name, arguments, send_to_rhino)
	elif name in curves_names:
		return handle_curves_tool(name, arguments, send_to_rhino)
	elif name in surfaces_names:
		return handle_surfaces_tool(name, arguments, send_to_rhino)
	elif name in layers_names:
		return handle_layers_tool(name, arguments, send_to_rhino)
	elif name in objects_names:
		return handle_objects_tool(name, arguments, send_to_rhino)
	elif name in view_names:
		return handle_view_tool(name, arguments, send_to_rhino)
	elif name in document_names:
		return handle_document_tool(name, arguments, send_to_rhino)
	else:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown tool: {name}"
		)]


async def main():
	"""
	Main server entry point
	"""
	from mcp.server.stdio import stdio_server

	async with stdio_server() as (read_stream, write_stream):
		await server.run(
			read_stream,
			write_stream,
			InitializationOptions(
				server_name="rhino-mcp",
				server_version="1.0.0",
				capabilities=server.get_capabilities(
					notification_options=NotificationOptions(),
					experimental_capabilities={},
				),
			),
		)


if __name__ == "__main__":
	asyncio.run(main())
