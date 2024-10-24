
import numpy as np
import matplotlib.pyplot as plt
import ezdxf

def generate_hollow_rectangles(rows, cols, pattern_width, pattern_height, wall_thickness):
    """Generates a grid of hollow rectangles with specified wall thickness."""
    fig, ax = plt.subplots()

    # Loop through the rows and columns to place hollow rectangles
    for i in range(rows):
        for j in range(cols):
            x = j * pattern_width  # Horizontal position of the rectangle
            y = i * pattern_height  # Vertical position of the rectangle

            # Outer rectangle (the full-size rectangle)
            outer_rect = np.array([
                [x, y],  # Bottom-left
                [x + pattern_width, y],  # Bottom-right
                [x + pattern_width, y + pattern_height],  # Top-right
                [x, y + pattern_height],  # Top-left
            ])

            # Inner rectangle (smaller by the wall thickness on all sides)
            inner_rect = np.array([
                [x + wall_thickness, y + wall_thickness],  # Bottom-left
                [x + pattern_width - wall_thickness, y + wall_thickness],  # Bottom-right
                [x + pattern_width - wall_thickness, y + pattern_height - wall_thickness],  # Top-right
                [x + wall_thickness, y + pattern_height - wall_thickness],  # Top-left
            ])

            # Draw the outer rectangle
            ax.fill(*zip(*outer_rect), 'b', edgecolor='k')

            # Draw the inner rectangle as a hollow space by "cutting" it out (white fill)
            ax.fill(*zip(*inner_rect), 'w', edgecolor='k')

    # Set equal scaling for both axes and display the plot
    ax.set_aspect('equal')
    plt.show()

def save_as_dxf(filename, rows, cols, pattern_width, pattern_height, wall_thickness):
    """Creates a DXF file with hollow rectangles and wall thickness."""
    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()

    for i in range(rows):
        for j in range(cols):
            x = j * pattern_width
            y = i * pattern_height

            # Outer rectangle
            outer_points = [
                (x, y),  # Bottom-left
                (x + pattern_width, y),  # Bottom-right
                (x + pattern_width, y + pattern_height),  # Top-right
                (x, y + pattern_height),  # Top-left
            ]

            # Inner rectangle (smaller by the wall thickness)
            inner_points = [
                (x + wall_thickness, y + wall_thickness),  # Bottom-left
                (x + pattern_width - wall_thickness, y + wall_thickness),  # Bottom-right
                (x + pattern_width - wall_thickness, y + pattern_height - wall_thickness),  # Top-right
                (x + wall_thickness, y + pattern_height - wall_thickness),  # Top-left
            ]

            # Draw the outer rectangle in the DXF
            for k in range(4):
                start_point = outer_points[k]
                end_point = outer_points[(k + 1) % 4]
                msp.add_line(start_point, end_point)

            # Draw the inner rectangle in the DXF
            for k in range(4):
                start_point = inner_points[k]
                end_point = inner_points[(k + 1) % 4]
                msp.add_line(start_point, end_point)

    # Save the DXF file
    doc.saveas(filename)

if __name__ == "__main__":
    # Parameters for the pattern
    rows = 10
    cols = 10
    pattern_width = 10
    pattern_height = 6
    wall_thickness = 1  # Thickness of the rectangle walls

    # Generate the pattern (visualization)
    generate_hollow_rectangles(rows, cols, pattern_width, pattern_height, wall_thickness)

    # Save as DXF file
    save_as_dxf("hollow_rectangle_pattern.dxf", rows, cols, pattern_width, pattern_height, wall_thickness)
    print("DXF file saved: hollow_rectangle_pattern.dxf")
