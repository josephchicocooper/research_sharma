import ezdxf
import numpy as np
import matplotlib.pyplot as plt
from feb_sine_portion import *

def create_custom_shape_dxf(width, height, concavity, ratio_height, filename="custom_shape_rowen.dxf"):
    #Creates a custom shape using given parameters, saves it as a DXF file, and visualizes it
    # Define points based on parameters
    points = np.array([
        [0, 0],
        [width, 0],
        [width - concavity * width, height * ratio_height],
        [width, height],
        [0, height],
        [0 + concavity * width, height * ratio_height],
        [0, 0]
    ])
    
    # create a new DXF document
    doc = ezdxf.new()
    msp = doc.modelspace()
    
    # add the shape as a polyline
    msp.add_lwpolyline(points, close=True)
    
    # Save DXF file
    doc.saveas(filename)
    
    # Plot using matplotlib
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.fill(points[:, 0], points[:, 1], alpha=0.3)
    plt.xlim(-10, width + 10)
    plt.ylim(-10, height + 10)
    plt.gca().set_aspect('equal')
    plt.title("Custom Shape Visualization")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.grid(True)
    plt.show()

def create_custom_shape_squiggle_dxf(width, height, concavity, ratio_height,horizontal_bb, diagonal_bb, mode , amplitude, filename="custom_shape1.dxf"):
    
    #Creates a custom shape using given parameters, saves it as a DXF file, and visualizes it
    # Define points based on parameters
    point1 = np.array([[0, 0]])
    
    point2 = find_point_on_line(0,0,width,0,horizontal_bb)
    point3 = find_point_on_line(width,0,0,0,horizontal_bb)
    distance = np.linalg.norm(point2 - point3)
    bottom_spring_pre_translate = generate_standing_wave_points(mode,amplitude,distance)
    bottom_spring =translate_points(bottom_spring_pre_translate,horizontal_bb,0)
    
    point4 = np.array([[width,0]])

    point5 = find_point_on_line(width,0,width - concavity * width, height * ratio_height,diagonal_bb)
    point6 = find_point_on_line(width - concavity * width, height * ratio_height,width,0,diagonal_bb)
    distance =np.linalg.norm(point5 - point6)
    theta  = calculate_angle_from_x_axis(point5,point6)
    lower_right_spring_prerotation_translate = generate_standing_wave_points(mode,amplitude,distance)
    lower_right_spring_pre_translate = rotate_points(lower_right_spring_prerotation_translate,theta)
    lower_right_spring=  translate_points(lower_right_spring_pre_translate,point5[0],point5[1])

    point7 = np.array([[ width - concavity * width, height * ratio_height]])
    
    point8 = find_point_on_line(width - concavity * width, height * ratio_height,width,height,diagonal_bb)
    point9 = find_point_on_line(width,height,width - concavity * width, height * ratio_height,diagonal_bb)
    distance =np.linalg.norm(point8 - point9)
    theta  = calculate_angle_from_x_axis(point8,point9)
    upper_right_spring_prerotation_translate = generate_standing_wave_points(mode,amplitude,distance)
    upper_right_spring_pre_translate = rotate_points(upper_right_spring_prerotation_translate,theta)
    upper_right_spring=  translate_points(upper_right_spring_pre_translate,point8[0],point8[1])

    point10 = np.array([[ width, height]])
    
    point11 = find_point_on_line(width,height,0,height,horizontal_bb)
    point12 = find_point_on_line(0,height,width,height,horizontal_bb)
    distance =np.linalg.norm(point11 - point12)
    theta  = calculate_angle_from_x_axis(point11,point12)
    upper_spring_prerotation_translate = generate_standing_wave_points(mode,amplitude,distance)
    upper_spring_pre_translate = rotate_points(upper_spring_prerotation_translate,theta)
    upper_spring=  translate_points(upper_spring_pre_translate,point11[0],point11[1])

    point13 = np.array([[ 0, height]])
    
    point14 = find_point_on_line( 0, height ,0 + concavity * width, height * ratio_height ,diagonal_bb)
    point15 = find_point_on_line(0 + concavity * width, height * ratio_height,0, height ,diagonal_bb)
    distance =np.linalg.norm(point14 - point15)
    theta  = calculate_angle_from_x_axis(point14,point15)
    upper_left_spring_prerotation_translate = generate_standing_wave_points(mode,amplitude,distance)
    upper_left_spring_pre_translate = rotate_points( upper_left_spring_prerotation_translate ,theta)
    upper_left_spring=  translate_points(upper_left_spring_pre_translate,point14[0],point14[1])

    point16 = np.array([[0 + concavity * width, height * ratio_height]])

    point17 = find_point_on_line(0 + concavity * width, height * ratio_height, 0,0 ,diagonal_bb)
    point18 = find_point_on_line(0,0, 0 + concavity * width, height * ratio_height,diagonal_bb)
    distance =np.linalg.norm(point17 - point18)
    theta  = calculate_angle_from_x_axis(point17,point18)
    bottom_left_spring_prerotation_translate = generate_standing_wave_points(mode,amplitude,distance)
    bottom_left_spring_pre_translate = rotate_points(  bottom_left_spring_prerotation_translate ,theta)
    bottom_left_spring=  translate_points(bottom_left_spring_pre_translate,point17[0],point17[1])

    
    points = np.vstack([point1,bottom_spring])
    points = np.vstack([points,point4])
    points = np.vstack([points,lower_right_spring])
    points = np.vstack([points,point7])
    points  = np.vstack([points,upper_right_spring])
    points = np.vstack([points,point10])
    points  = np.vstack([points,upper_spring])
    points = np.vstack([points,point13])
    points  = np.vstack([points,upper_left_spring])
    points = np.vstack([points,point16])
    points  = np.vstack([points,bottom_left_spring])
    


    

    
    
    
    # ceate a new DXF document
    doc = ezdxf.new()
    msp = doc.modelspace()
    
    # add the shape as a polyline
    msp.add_lwpolyline(points, close=True)
    
    # save DXF file
    doc.saveas(filename)
    
    # Plot using matplotlib
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.fill(points[:, 0], points[:, 1], alpha=0.3)
    plt.xlim(-10, width + 10)
    plt.ylim(-10, height + 10)
    plt.gca().set_aspect('equal')
    plt.title("Custom Shape Visualization")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.grid(True)
    plt.show()

    
    
# Example usage
#create_custom_shape_dxf(width=100, height=50, concavity=0.2, ratio_height=0.5)
#create_custom_shape_squiggle_dxf(width =10 , height= 10 , concavity= 0.3, ratio_height=0.5,horizontal_bb=1, diagonal_bb=1, mode =2 , amplitude =1, filename="custom_shape1.dxf")
#create_custom_shape_squiggle_dxf(width =6.6 , height= 10 , concavity= 0.43, ratio_height=0.5,horizontal_bb=2, diagonal_bb=2, mode =2 , amplitude =1.4, filename="custom_shape_6.dxf")
#create_custom_shape_dxf(width=10, height=10, concavity=0.45, ratio_height=0.3)
#create_custom_shape_squiggle_dxf(width =30, height= 30 , concavity= 0.45, ratio_height=0.5,horizontal_bb=0, diagonal_bb=0, mode =2 , amplitude =-5, filename="custom_shape_7.dxf")
create_custom_shape_dxf(width=6.6, height=10, concavity=0.45, ratio_height=0.5,filename="rowen_equi.dxf")
