from point import Point
from line_segment import LineSegment
from quadrilateral import Quadrilateral

def main():
    A = Point(4, 6)
    B = Point(4, 8)
    C = Point(2, 6)
    D = Point(2, 8)
    AB = LineSegment(A, B, 2)
    CD = LineSegment(C, D, 2)
    ABCD = Quadrilateral(AB, CD)
    print(A)
    print(AB)
    print(ABCD)
if __name__ == '__main__':
    main()
