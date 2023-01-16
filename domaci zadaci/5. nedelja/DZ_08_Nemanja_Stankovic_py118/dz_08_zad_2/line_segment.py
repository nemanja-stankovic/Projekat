from point import Point


class LineSegment:
    """Model for line segment."""

    def __init__(self, first_point: Point, second_point: Point, length: float):
        """Initialize the line segment object."""
        self.first_point = first_point
        self.second_point = second_point
        self.length = length

    def change_points_or_length(self, new_first_point: Point, new_second_point: Point, new_length: float):
        """Change point points or length."""
        self.first_point = new_first_point
        self.second_point = new_second_point
        self.length = new_length

    def __str__(self):
        return f"duz od tacke {self.first_point}, do tacke {self.second_point}, duzine {self.length}"