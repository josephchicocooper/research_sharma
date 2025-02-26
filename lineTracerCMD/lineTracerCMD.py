import sys
import cv2
import ezdxf

def process_image(image_path, save_name):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    binary_image = cv2.adaptiveThreshold(
        blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(closed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()
    
    for contour in contours:
        points = contour.squeeze(axis=1)
        if len(points) < 2:
            continue
        for i in range(len(points) - 1):
            msp.add_line(points[i].tolist(), points[i + 1].tolist())
        msp.add_line(points[-1].tolist(), points[0].tolist())
    
    doc.saveas(save_name)
    print(f"DXF saved as {save_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lineTracerCMD.py <image_file> <output_dxf>")
        sys.exit(1)
    
    image_file = sys.argv[1]
    output_dxf = sys.argv[2]
    if not output_dxf.endswith(".dxf"):
        output_dxf += ".dxf"
    
    process_image(image_file, output_dxf)
