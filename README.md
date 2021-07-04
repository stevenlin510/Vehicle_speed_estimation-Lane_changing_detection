# Vehicle Speed Estimation and Lane Changing Detection
This repository implements YOLOv3 and Deep SORT in order to perfrom real-time object tracking. Yolov3 is an algorithm that uses deep convolutional neural networks to perform object detection. I can feed these object detections into Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric) in order for a real-time object tracker to be created. For speed estimation I use vitual lanes post-processing to check the car speed between two lines. Also, I use background median filter technique to obtain background image and then detect the lane.  

### Reference code

For the baseline code of object detection and tracking, refer to this [GitHub][link]. Environment also set in the same way as this link.

[link]: https://github.com/yehengchen/Object-Detection-and-Tracking/tree/master/OneStage/yolo/deep_sort_yolov3

## Acknowledgments
* [Yolov3 TensorFlow Amazing Implementation](https://github.com/zzh8829/yolov3-tf2)
* [Deep SORT Repository](https://github.com/nwojke/deep_sort)
* [Yolo v3 official paper](https://arxiv.org/abs/1804.02767)
