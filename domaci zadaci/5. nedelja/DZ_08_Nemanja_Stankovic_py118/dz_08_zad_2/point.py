class Point:
    """Model for point."""

    def __init__(self, coordinate_x: int,coordinate_y: int):
        """Initialize the point object."""
        self.coordinate_x=coordinate_x
        self.coordinate_y=coordinate_y

    def change_point_coordinates(self,new_coordinate_x: int, new_coordinate_y:int):
        """Change point coordinates."""
        self.coordinate_x=new_coordinate_x
        self.coordinate_y=new_coordinate_y

    def __str__(self):
        return f"({self.coordinate_x}, {self.coordinate_y})"

