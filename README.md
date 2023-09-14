# Read-time Ball Motion Detection

This project detects and tracks the motion of a ball in a video and calculates how many times the ball hits the ground.

## How to Run

1. Ensure you have all the required libraries installed:

``` sh
pip install opencv-python numpy scikit-learn
```


2. Run the script:

``` sh
python main.py
```

**_NOTE:_**  you must specify the video path in the main file.

The algorithm:

* Employs Gaussian blur and motion detection methodologies to extract moving parts from each frame.
* Utilizes contour-based techniques to identify the ball, thereby eliminating noise and irrelevant objects.
* Keeps a persistent track of the ball's motion, thus enabling the prediction of its future movement.
* Efficiently calculates the number of times the ball hits the ground, providing insights into its motion dynamic

