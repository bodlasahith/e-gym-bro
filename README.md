# group-project-readme

Week 6 Goals: 
- Display output wireframe for the model 
- Create messages based off of the model output 

Bicep Comparison Example: https://github.com/sinahajizadeh/gym_computer_vision/blob/main/coach.py

Dataset: https://www.kaggle.com/datasets/hasyimabdillah/workoutfitness-video/data

Machine Learning Model: https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
 - Using MediaPipe to do keypoints 

Wireframes:
https://www.figma.com/file/z6DeskJib3B4WQOenzrFJZ/E-GymBro-Website-Wireframes?type=design&node-id=0%3A1&mode=design&t=UsDnv3MsdxTML8FT-1

Deploy on https://streamlit.io/:
Can do real-time processing with this extension: https://github.com/whitphx/streamlit-webrtc
Teachable Machine: No Code Solution: https://teachablemachine.withgoogle.com/train/pose

Preliminary Theory:
Get the angles of certain points 
Compare those angles to angles of professional weightlifters
Provide advice based on the range of those angles 


def compute_angle(A, B, C):
    # Vector BA
    BA = [A.x - B.x, A.y - B.y, A.z - B.z]
    # Vector BC
    BC = [C.x - B.x, C.y - B.y, C.z - B.z]

    # Dot product
    dot_product = sum(a*b for a, b in zip(BA, BC))

    # Magnitude of vectors
    mag_BA = math.sqrt(sum(a*a for a in BA))
    mag_BC = math.sqrt(sum(b*b for b in BC))

    # Cosine of the angle
    cos_theta = dot_product / (mag_BA * mag_BC)

    # Angle in radians
    theta = math.acos(cos_theta)

    # Convert to degrees
    theta_deg = math.degrees(theta)

    return theta_deg



