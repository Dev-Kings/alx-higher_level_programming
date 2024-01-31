#!/usr/bin/python3
"""
A module containing class Rectangle.
"""


class Rectangle:
    """Class with area and perimeter calculation methods.
    Attributes:
        number_of_instances(int): Number of objects created.
        print_symbol: Symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init method initializing private width and height.
        Args:
            width (int, optional): Width of rectangle.
            height (int, optional): Height of rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
            type(self).number_of_instances += 1

    @property
    def width(self):
        """int: width of rectangle.
        Raises:
            TypeError: if not an integer.
            ValueError: if less than 0.
        Returns:
            Width of rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """int: height of rectangle.
        Raises:
            TypeError: if not an integer.
            ValueError: if less than 0.
        Returns:
            Height of rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of rectangle.
        Returns:
            Area of rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of rectangle.
        Returns:
            Perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """String representation of rectangle class.
        Returns:
            Character '#' representing the area.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = [str(self.print_symbol) * self.__width for i in
                         range(self.__height)]
        return ("\n".join(rectangle_str))

    def __repr__(self):
        """String repr of rectangle class.
        Returns:
            Formatted string representation.
        """
        return ("{}({}, {})".format(self.__class__.__name__, self.__width,
                self.__height))

    def __del__(self):
        """Deletes a class instance and prints a message.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
