import ezdxf
import numpy as np
import matplotlib.pyplot as plt

def generate_standing_wave_points(mode, amplitude, distance, num_points=100):
    #Generates points for a standing wave with given mode, amplitude, and distance
    x_values = np.linspace(0, distance, num_points)
    y_values = amplitude * np.sin(mode * np.pi * x_values / distance)
    return np.column_stack((x_values, y_values))

def visualize_standing_wave(mode, amplitude, distance, num_points=100):
    #Visualizes the standing wave points using matplotlib
    points = generate_standing_wave_points(mode, amplitude, distance, num_points)
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.title(f"Standing Wave Visualization (Mode {mode})")
    plt.xlabel("Distance")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

def visualizepPoints(points):
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.title(f"Standing Wave Visualization (Mode {mode})")
    plt.xlabel("Distance")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

def rotate_points(points, theta):
    #Rotates a set of points by an angle theta (in radians) around the origin
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    return np.dot(points, rotation_matrix.T)

def calculate_angle_from_x_axis(start, end):
    #Calculates the angle theta from the x axis to the line connecting two points
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return np.arctan2(dy, dx)

def translate_points(points, x_disp, y_disp):
    #Translates a set of points by given x and y displacements.
    translation_matrix = np.array([x_disp, y_disp])
    return points + translation_matrix

#visualize_standing_wave(5,1,4)
'''
mode = 3
amplitude  =2
distance =  10
num_points =  50
points = generate_standing_wave_points(mode, amplitude, distance, num_points)
points = rotate_points(points,1.5)
visualizepPoints(points)
'''


def find_point_on_line(x1, y1, x2, y2, d):
    # Define the points as numpy arrays
    point1 = np.array([x1, y1])
    point2 = np.array([x2, y2])
    
    # calculate the direction vector
    direction = point2 - point1
    
    # normalize the direction vector
    magnitude = np.linalg.norm(direction)
    unit_direction = direction / magnitude
    
    # clculate the new point at distance d from point1
    new_point = point1 + d * unit_direction
    
    return new_point
'''
# Example 
x1, y1 = 0, 0
x2, y2 = 4, 4
d = 5.65

new_point = find_point_on_line(x1, y1, x2, y2, d)
print(f"The point {d} units from ({x1}, {y1}) along the line to ({x2}, {y2}) is {new_point}")

'''
