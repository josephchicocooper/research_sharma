import numpy as np
import matplotlib.pyplot as plt
import ezdxf


def generate_hollow_octogons(rows, cols, pattern_width, pattern_height, wall_thickness,convex):
    """Generates a grid of hollow rectangles with specified wall thickness."""
    fig, ax = plt.subplots()

    # Loop through the rows and columns to place hollow rectangles
    for i in range(rows):
        #odd even
        if( i%2 == 0) :
            for j in range(cols-1):
                x = j * pattern_width  # Horizontal position of the rectangle
                y = i * pattern_height  # Vertical position of the rectangle

                # Outer rectangle (the full-size rectangle)
                outer_rect = np.array(
                    [
                    (x + 0.5*pattern_width , y - i*pattern_height*(convex)),  # Bottom-left
                    (x+ pattern_width, y+ pattern_height* convex - i*pattern_height*(convex)),# bottom middle
                    (x + 1.5*pattern_width, y - i*pattern_height*(convex)),  # Bottom-right
                    (x + 1.5*pattern_width, y + pattern_height - i*pattern_height*(convex)),  # Top-right
                    (x + pattern_width, y + pattern_height - pattern_height*convex - i*pattern_height*(convex)),# top middle
                    (x+0.5*pattern_width, y + pattern_height - i*pattern_height*(convex))  # Top-left
                    ]              

                    )

                # Inner rectangle (smaller by the wall thickness on all sides)
                inner_rect = np.array(
                       [
                    (x + 0.5*pattern_width +wall_thickness , y+ 2* wall_thickness - i*pattern_height*(convex)),  # Bottom-left
                    (x+ pattern_width, y+ pattern_height* convex + wall_thickness - i*pattern_height*(convex)),# bottom middle
                    (x + 1.5*pattern_width - wall_thickness, y+2*wall_thickness - i*pattern_height*(convex)),  # Bottom-right
                    (x + 1.5*pattern_width-wall_thickness, y + pattern_height- 2*wall_thickness - i*pattern_height*(convex)),  # Top-right
                    (x + pattern_width, y + pattern_height - pattern_height*convex - wall_thickness - i*pattern_height*(convex)),# top middle
                    (x + 0.5*pattern_width+wall_thickness , y + pattern_height - 2*wall_thickness - i*pattern_height*(convex)),  # Top-left  
                ] 
                    )
                # Draw the outer rectangle
                ax.fill(*zip(*outer_rect), 'b', edgecolor='k')

            # Draw the inner rectangle as a hollow space by "cutting" it out (white fill)
                ax.fill(*zip(*inner_rect), 'w', edgecolor='k')
                
        if(i%2 != 0):
            
            for j in range(cols):
                x = j * pattern_width  # Horizontal position of the rectangle
                y = i * pattern_height  # Vertical position of the rectangle

                # Outer rectangle (the full-size rectangle)
                outer_rect = np.array(
                    [
                    (x , y - i*pattern_height*(convex)),  # Bottom-left
                    (x+ 0.5*pattern_width, y+ pattern_height* convex - i*pattern_height*(convex)),# bottom middle
                    (x + 1*pattern_width, y - i*pattern_height*(convex)),  # Bottom-right
                    (x + 1*pattern_width, y + pattern_height - i*pattern_height*(convex)),  # Top-right
                    (x + 0.5*pattern_width, y + pattern_height - i*pattern_height*convex- pattern_height*(convex)),# top middle
                    (x , y + pattern_height- i*pattern_height*(convex))  # Top-left
                    ]              

                    )

                # Inner rectangle (smaller by the wall thickness on all sides)
                inner_rect = np.array(
                       [
                    (x  +wall_thickness , y+ 2* wall_thickness - i*pattern_height*(convex)),  # Bottom-left
                    (x+ 0.5*pattern_width, y+ pattern_height* convex+wall_thickness- i*pattern_height*(convex)),# bottom middle
                    (x + pattern_width - wall_thickness, y+2* wall_thickness- i*pattern_height*(convex)),  # Bottom-right
                    (x + pattern_width-wall_thickness, y + pattern_height-2*wall_thickness - i*pattern_height*(convex)),  # Top-right
                    (x + 0.5*pattern_width, y + pattern_height - pattern_height*convex - 2*wall_thickness- i*pattern_height*(convex)),# top middle
                    (x +wall_thickness , y + pattern_height - 2*wall_thickness- i*pattern_height*(convex)),  # Top-left  
                ] 
                    )    

            

            # Draw the outer rectangle
                ax.fill(*zip(*outer_rect), 'b', edgecolor='k')

            # Draw the inner rectangle as a hollow space by "cutting" it out (white fill)
                ax.fill(*zip(*inner_rect), 'w', edgecolor='k')
        

    # Set equal scaling for both axes and display the plot
    ax.set_aspect('equal')
    plt.show()

def save_as_dxf(filename, rows, cols, pattern_width, pattern_height, wall_thickness ,convex):
    """Creates a DXF file with hollow rectangles and wall thickness."""
    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()

    # Set to store unique lines
    unique_lines = set()
    
    def add_unique_line(start_point, end_point):
        # Convert points to tuples to ensure they are hashable and can be added to a set
        line = (tuple(start_point), tuple(end_point))
        reverse_line = (tuple(end_point), tuple(start_point))
        
        # Add the line only if neither it nor its reverse exists
        if line not in unique_lines and reverse_line not in unique_lines:
            unique_lines.add(line)
            msp.add_line(start_point, end_point)
    
    for i in range(rows):
        #odd even
        if( i%2 == 0) :
            for j in range(cols-1):
                x = j * pattern_width  # Horizontal position of the rectangle
                y = i * pattern_height  # Vertical position of the rectangle

                # Outer rectangle (the full-size rectangle)
                outer_points = (
                    [
                    (x + 0.5*pattern_width , y - i*pattern_height*(convex)),  # Bottom-left
                    (x+ pattern_width, y+ pattern_height* convex - i*pattern_height*(convex)),# bottom middle
                    (x + 1.5*pattern_width, y - i*pattern_height*(convex)),  # Bottom-right
                    (x + 1.5*pattern_width, y + pattern_height - i*pattern_height*(convex)),  # Top-right
                    (x + pattern_width, y + pattern_height - pattern_height*convex - i*pattern_height*(convex)),# top middle
                    (x+0.5*pattern_width, y + pattern_height - i*pattern_height*(convex))  # Top-left
                    ]              

                    )

                # Inner rectangle (smaller by the wall thickness on all sides)
                inner_points = (
                       [
                    (x + 0.5*pattern_width +wall_thickness , y +2*wall_thickness - i*pattern_height*(convex)),  # Bottom-left
                    (x+ pattern_width, y+ pattern_height* convex+wall_thickness - i*pattern_height*(convex)),# bottom middle
                    (x + 1.5*pattern_width - wall_thickness, y+2*wall_thickness - i*pattern_height*(convex)),  # Bottom-right
                    (x + 1.5*pattern_width-wall_thickness, y + pattern_height-2*wall_thickness - i*pattern_height*(convex)),  # Top-right
                    (x + pattern_width, y + pattern_height - pattern_height*convex - wall_thickness - i*pattern_height*(convex)),# top middle
                    (x + 0.5*pattern_width+wall_thickness , y + pattern_height - 2*wall_thickness - i*pattern_height*(convex)),  # Top-left  
                ] 
                    )
                '''
                # Draw the outer rectangle
                for k in range(6):
                    start_point = outer_points[k]
                    end_point = outer_points[(k + 1) % 6]
                    msp.add_line(start_point, end_point)

            # Draw the inner rectangle in the DXF
                for k in range(6):
                    start_point = inner_points[k]
                    end_point = inner_points[(k + 1) % 6]
                    msp.add_line(start_point, end_point)
                '''
                for k in range(6):
                
                    add_unique_line(outer_points[k], outer_points[(k + 1) % 6])

                # Add unique lines for the inner rectangle
                for k in range(6):
                    add_unique_line(inner_points[k], inner_points[(k + 1) % 6])
                
        if(i%2 != 0):
            
            for j in range(cols):
                x = j * pattern_width  # Horizontal position of the rectangle
                y = i * pattern_height  # Vertical position of the rectangle

                # Outer rectangle (the full-size rectangle)
                outer_points = (
                    [
                    (x , y - i*pattern_height*(convex)),  # Bottom-left
                    (x+ 0.5*pattern_width, y+ pattern_height* convex - i*pattern_height*(convex)),# bottom middle
                    (x + 1*pattern_width, y - i*pattern_height*(convex)),  # Bottom-right
                    (x + 1*pattern_width, y + pattern_height - i*pattern_height*(convex)),  # Top-right
                    (x + 0.5*pattern_width, y + pattern_height - i*pattern_height*convex- pattern_height*(convex)),# top middle
                    (x , y + pattern_height- i*pattern_height*(convex))  # Top-left
                    ]              

                    )

                # Inner rectangle (smaller by the wall thickness on all sides)
                inner_points = (
                       [
                    (x  +wall_thickness , y+2*wall_thickness - i*pattern_height*(convex)),  # Bottom-left
                    (x+ 0.5*pattern_width, y+ pattern_height* convex+wall_thickness- i*pattern_height*(convex)),# bottom middle
                    (x + pattern_width - wall_thickness, y+2*wall_thickness- i*pattern_height*(convex)),  # Bottom-right
                    (x + pattern_width-wall_thickness, y + pattern_height-2*wall_thickness - i*pattern_height*(convex)),  # Top-right
                    (x + 0.5*pattern_width, y + pattern_height - pattern_height*convex - 2*wall_thickness- i*pattern_height*(convex)),# top middle
                    (x +wall_thickness , y + pattern_height - 2*wall_thickness- i*pattern_height*(convex)),  # Top-left  
                ] 
                    )    

            

                '''
                 # Draw the outer rectangle in the DXF
                for k in range(6):
                    start_point = outer_points[k]
                    end_point = outer_points[(k + 1) % 6]
                    msp.add_line(start_point, end_point)

            # Draw the inner rectangle in the DXF
                for k in range(6):
                    start_point = inner_points[k]
                    end_point = inner_points[(k + 1) % 6]
                    msp.add_line(start_point, end_point)
                '''
                for k in range(6):
                    add_unique_line(outer_points[k], outer_points[(k + 1) % 6])

                # Add unique lines for the inner rectangle
                for k in range(6):
                    add_unique_line(inner_points[k], inner_points[(k + 1) % 6])
           

    # Save the DXF file
    doc.saveas(filename)

if __name__ == "__main__":
    # Parameters for the pattern
    rows = 4
    cols = 4
    pattern_width = 10
    pattern_height = 15
    wall_thickness = 0.875  # Thickness of the rectangle walls
    convex = 0.3
    # Generate the pattern (visualization)
    generate_hollow_octogons(rows, cols, pattern_width, pattern_height, wall_thickness,convex)

    # Save as DXF file
    save_as_dxf("hollow_rectangle_pattern_two.dxf", rows, cols, pattern_width, pattern_height, wall_thickness,convex)
    print("DXF file saved: hollow_rectangle_pattern.dxf")

         
