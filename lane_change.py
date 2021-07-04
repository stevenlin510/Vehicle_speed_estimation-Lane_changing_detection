import statistics
def laneChange(track,bbox,lines_image):

	bottom_center = (int(((bbox[0])+(bbox[2]))/2),int(bbox[3])) 
	if bottom_center[0] >= 1920 or bottom_center[1] >= 1080:
		lane_area = 0
	else:
		lane_area = int(lines_image[bottom_center[1],bottom_center[0]])
	if track.lane_area != lane_area:
		track.lane_change+=1

	track.lane_area = lane_area

	# if bottom_center[0] - track.bc[0] != 0: 
	# 	slope = (bottom_center[1] - track.bc[1]) / (bottom_center[0] - track.bc[0]) 
	# else:
	# 	slope = 0

	# diff_slope = abs(slope - track.slope)
	# if diff_slope != 0:
	# 	if diff_slope > 2.5:
	# 		track.lane_change += 1

	# track.slope = slope
	# track.bc = bottom_center
	return track

