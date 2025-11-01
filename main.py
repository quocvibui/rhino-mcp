#!/usr/bin/env python3
"""
Rhino MCP Server using FastMCP
Production-ready implementation with comprehensive tools organized by category
"""

from mcp.server.fastmcp import FastMCP
import logging

# Import all MCP tool modules
from tools import (
	application,
	block,
	curve,
	dimension,
	document,
	geometry,
	grips,
	group,
	hatch,
	layer,
	light,
	line,
	linetype,
	material,
	mesh,
	object,
	plane,
	pointvector,
	selection,
	surface,
	toolbar,
	transformation,
	userdata,
	userinterface,
	utility,
	view
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RhinoMCP")

mcp = FastMCP("rhino-mcp")


def main():
	"""Initialize and run the MCP server"""
	logger.info("Initializing Rhino MCP Server...")

	# Register all tool modules
	document.register_tools(mcp)
	geometry.register_tools(mcp)
	surface.register_tools(mcp)
	curve.register_tools(mcp)
	transformation.register_tools(mcp)
	layer.register_tools(mcp)
	object.register_tools(mcp)
	utility.register_tools(mcp)
	selection.register_tools(mcp)

	# Placeholder modules (no tools yet)
	application.register_tools(mcp)
	block.register_tools(mcp)
	dimension.register_tools(mcp)
	grips.register_tools(mcp)
	group.register_tools(mcp)
	hatch.register_tools(mcp)
	light.register_tools(mcp)
	line.register_tools(mcp)
	linetype.register_tools(mcp)
	material.register_tools(mcp)
	mesh.register_tools(mcp)
	plane.register_tools(mcp)
	pointvector.register_tools(mcp)
	toolbar.register_tools(mcp)
	userdata.register_tools(mcp)
	userinterface.register_tools(mcp)
	view.register_tools(mcp)

	logger.info("All tools registered successfully")
	logger.info("Starting MCP server...")

	# Run the MCP server
	mcp.run()


if __name__ == "__main__":
	main()
