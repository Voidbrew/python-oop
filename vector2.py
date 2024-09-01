class Vector2:
    """
    Represents a 2D vector.
    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
    Methods:
        __add__(other): Adds two vectors element-wise.
        __sub__(other): Subtracts two vectors element-wise.
        __mul__(scalar): Multiplies the vector by a scalar.
        __truediv__(scalar): Divides the vector by a scalar.
        magnitude(): Calculates the magnitude of the vector.
        normalize(): Returns a normalized version of the vector.
        __str__(): Returns a string representation of the vector.
    Example:
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        v3 = v1 + v2
        print(v3)  # Output: Vector2(4, 6)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0, 0)
        return Vector2(self.x / mag, self.y / mag)

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"
