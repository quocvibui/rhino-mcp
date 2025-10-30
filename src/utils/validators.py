"""
Input validation utilities
"""


def validate_number(value, default=0):
	"""
	Validate and convert to number
	value: Input value to validate
	default: Default value if invalid
	return: Validated number
	"""
	try:
		return float(value) if value is not None else default
	except (TypeError, ValueError):
		return default


def validate_point(point, default=None):
	"""
	Validate point coordinates
	point: Point tuple or list (x, y, z)
	default: Default point if invalid
	return: Validated point tuple or default
	"""
	if default is None:
		default = (0, 0, 0)

	if not point or not isinstance(point, (list, tuple)):
		return default

	if len(point) < 3:
		return default

	try:
		return (float(point[0]), float(point[1]), float(point[2]))
	except (TypeError, ValueError):
		return default


def validate_points(points, min_count=2):
	"""
	Validate list of points
	points: List of point tuples
	min_count: Minimum required points
	return: Validated points list or None if invalid
	"""
	if not points or not isinstance(points, list):
		return None

	if len(points) < min_count:
		return None

	validated = []
	for pt in points:
		v_pt = validate_point(pt)
		if v_pt is None:
			return None
		validated.append(v_pt)

	return validated
