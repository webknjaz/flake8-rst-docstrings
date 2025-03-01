"""Example of a malformed definition list.

This is expected to fail validation:

    $ flake8 --select RST RST203/def_list.py
    RST203/def_list.py:18:1: RST203 Definition list ends without a blank line; unexpected unindent.

In this case, the four parameters should all have their own ``:parameter``
opening.
"""

def box(x1, y1, width=500, hieght=100):
    """Draw a box.

    :parameter
        x1: - required left coordinate, float
        y1: - required bottom coordinate, float
        width: - optional width, float
        height: - optional height, float
    :return: Graphics object
    """
    pass

