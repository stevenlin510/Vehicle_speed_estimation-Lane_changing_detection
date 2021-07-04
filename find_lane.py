import cv2
import numpy as np
import matplotlib.pyplot as plt 

def check_line(p1, p2, w):
    x = (p2[0]-p1[0])*(w[1]-p1[1])-(w[0]-p1[0])*(p2[1]-p1[1])
    
    return x
def remove_noise(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detect_edges(image, low_threshold, high_threshold):	
    return cv2.Canny(image, low_threshold, high_threshold)

def region_of_interest(canny):
    height = canny.shape[0]
    width = canny.shape[1]
    mask_l = np.zeros_like(canny)
    rectangle_l = np.array([[
    (10, 666),(741,281),
    (888, 274),
    (550, height),(0,height)]], np.int32)
    cv2.fillPoly(mask_l, rectangle_l, 255)
    mask_r = np.zeros_like(canny)
    rectangle_r = np.array([[
    (1255, 	1078),(981,302),
    (1125, 308),
    (1916, 799),(width,height)]], np.int32)
    cv2.fillPoly(mask_r, rectangle_r, 255)
    ml_image = cv2.bitwise_and(canny, mask_l)
    mr_image = cv2.bitwise_and(canny,mask_r)
    masked_image  = cv2.add(mr_image,ml_image)	
    return masked_image

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
   
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)

    li = []
    ri=[]
    for line in lines:
    	for x1,y1,x2,y2 in line:
    		fit = np.polyfit((x1,x2), (y1,y2), 1)
    		slope = fit[0]
    		intercept = fit[1]
    		if slope > 0.5 :
    			li.append([x1,y1,x2,y2])
    		if slope < -0.5 :
    			li.append([x1,y1,x2,y2])
    lines_image = np.zeros((*img.shape, 3), dtype=np.uint8)
    li = np.array(li)
    li = li.reshape(li.shape[0],1,-1)
    draw_lines(lines_image, li)
    return lines_image,li

def draw_lines(img, lines, color=[255, 0, 0], thickness=2):

    for line in lines:
        for x1,y1,x2,y2 in line:
        	cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def weighted_img(img, initial_img, α=0.7, β=1., γ=0.):

    return cv2.addWeighted(initial_img, α, img, β, γ)

def findLane(frame):
	img = frame.copy()
	output_image = grayscale(img)
	gaussian_img = remove_noise(output_image, 3)
	canny_img = detect_edges(gaussian_img, 50, 150)
	roi_img = region_of_interest(canny_img)
	kernel = np.ones((10,10),np.uint8)
	closing = cv2.morphologyEx(roi_img, cv2.MORPH_CLOSE, kernel)
	# cv2.imwrite('closing.jpg',closing)
	lines_image ,li= hough_lines(closing, 1, (np.pi/180), 100, 10, 100)
	cv2.imwrite('hough_lane.jpg',lines_image)
	gray_lines = grayscale(lines_image)
	return lines_image,li,gray_lines

if __name__ == '__main__':
	image = cv2.imread('bg.jpg')
	final_img,li,i = findLane(image)
	cv2.imwrite('lane.jpg',final_img)
