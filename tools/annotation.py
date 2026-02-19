"""
MCP tools for annotation operations
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all annotation tools with the MCP server"""

	@mcp.tool()
	def add_text(text: str, point_x: float, point_y: float, point_z: float,
				 height: float = 1.0, font: str = "") -> str:
		"""
		Add a text object in Rhino
		text: The text string to display
		point_x, point_y, point_z: Location point
		height: Text height (default 1.0)
		font: Font name (optional, uses default if empty)
		"""
		try:
			params = {
				"text": text,
				"point": [point_x, point_y, point_z],
				"height": height
			}
			if font:
				params["font"] = font
			result = send_to_rhino("add_text", params)
			return f"Added text '{text}' at ({point_x}, {point_y}, {point_z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def add_text_dot(text: str, point_x: float, point_y: float, point_z: float) -> str:
		"""
		Add a text dot (always faces camera, constant screen size)
		text: The text to display in the dot
		point_x, point_y, point_z: Location point
		"""
		try:
			params = {"text": text, "point": [point_x, point_y, point_z]}
			result = send_to_rhino("add_text_dot", params)
			return f"Added text dot '{text}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def add_leader(points: str, text: str = "") -> str:
		"""
		Add a leader annotation (arrow with optional text)
		points: Semicolon-separated points, each as 'x,y,z' (min 2 points, e.g. '0,0,0;10,10,0')
		text: Optional text to display at the leader
		"""
		try:
			pts = [[float(c) for c in p.split(",")] for p in points.split(";")]
			params = {"points": pts}
			if text:
				params["text"] = text
			result = send_to_rhino("add_leader", params)
			return f"Added leader annotation"
		except Exception as e:
			return f"Error: {e}"
