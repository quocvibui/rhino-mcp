#!/usr/bin/env python3
"""
Rhino MCP Server using FastMCP
Exposes 50 tools for controlling Rhino 8 via Model Context Protocol
"""

from mcp.server.fastmcp import FastMCP
import logging

from tools import (
	curve,
	document,
	geometry,
	layer,
	object,
	selection,
	surface,
	transformation,
	utility
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RhinoMCP")

mcp = FastMCP("rhino-mcp")


def main():
	"""Initialize and run the MCP server"""
	logger.info("Initializing Rhino MCP Server...")

	document.register_tools(mcp)
	geometry.register_tools(mcp)
	surface.register_tools(mcp)
	curve.register_tools(mcp)
	transformation.register_tools(mcp)
	layer.register_tools(mcp)
	object.register_tools(mcp)
	utility.register_tools(mcp)
	selection.register_tools(mcp)

	logger.info("All tools registered successfully")
	logger.info("Starting MCP server...")

	mcp.run()


if __name__ == "__main__":
	main()
