# parameters for calculating vehicle speed
ms2kmh = 3.6
vdlDistance = 18 # distance between VDLs
fps = 25 # input video's fps

def check_line(p1, p2, w):

    x = (p2[0]-p1[0])*(w[1]-p1[1])-(w[0]-p1[0])*(p2[1]-p1[1])
    
    return x

def calcSpeed(track,luLine,ldLine,ruLine,rdLine,bbox,frame_idx):

    bottom_center = (int(((bbox[0])+(bbox[2]))/2),int(bbox[3])) 

    if int(bottom_center[0]) <= 960:

        if track.speed_update and check_line(luLine[0], luLine[1], bottom_center) < 0:
            track.time_passing_vline_start = frame_idx

        if track.speed_update and check_line(ldLine[0], ldLine[1], bottom_center) > 0:
            track.time_passing_vline_end = frame_idx

    elif int(bottom_center[0]) >= 960:
        if track.speed_update and check_line(rdLine[0], rdLine[1], bottom_center) > 0:
            track.time_passing_vline_start = frame_idx
        if track.speed_update and check_line(ruLine[0], ruLine[1], bottom_center) < 0:
            track.time_passing_vline_end = frame_idx 

    if track.time_passing_vline_end > 0 and track.time_passing_vline_start > 0:
        track.speed_time = (track.time_passing_vline_end-track.time_passing_vline_start) * 1/fps
        if track.speed_update and track.speed_time > 0:
            track.speed_update = False

        if int(bottom_center[0]) <= 960: 
            if check_line(ldLine[1], ldLine[0], bottom_center) < 0:
                
                track.speed = vdlDistance/(track.speed_time)*ms2kmh
        else: 
            if check_line(ruLine[1], ruLine[0], bottom_center) > 0:
                track.speed = vdlDistance/(track.speed_time)*ms2kmh
    
    return track