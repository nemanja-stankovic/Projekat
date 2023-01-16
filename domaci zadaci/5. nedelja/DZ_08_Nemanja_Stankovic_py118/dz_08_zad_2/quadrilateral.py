from line_segment import LineSegment


class Quadrilateral:
    """Model for quadrilateral."""

    def __init__(self,first_line_segment: LineSegment, second_line_segment: LineSegment):
        """Initialize the line quadrilateral object."""
        self.first_line_segment=first_line_segment
        self.second_line_segment=second_line_segment

    def area(self):
        """Area calculation"""
        return self.first_line_segment.length*self.second_line_segment.length

    def perimeter(self):
        """Perimetar calculation"""
        return 2*(self.first_line_segment.length+self.second_line_segment.length)

    def __str__(self):
        return f"Cetvorougao sa prvom stranicom duzine {self.first_line_segment.length},drugom stranicom duzine {self.second_line_segment.length} i tackama: {self.first_line_segment.first_point},{self.first_line_segment.second_point},{self.second_line_segment.first_point},{self.second_line_segment.second_point}"