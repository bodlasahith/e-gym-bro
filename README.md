# group-project-team88
group-project-team88 created by GitHub Classroom

Our project was building a trained ML model that detects an incorrect form when doing a workout or exercise.

We used many modules & stacks including:
- MediaPipe
- StreamLit
- Tensorflow

This demonstrates the architecture of our project & how all component interoperate w/ each other
![image](https://github.com/CS222-UIUC-FA23/group-project-team88/assets/112727686/8b6630d5-fd58-481a-a440-d74f96155e38)

In summary, 

1. We first trained a predetermined template that serves as a base to compare exercises to.

2. Input a video into the model 
  -> MediaPipe will return a matrix of angle calculations (basically a numeric representation of your body form and placement)
  -> Our KNN model will compare to the trained template
  -> You will recieve an output of suggestions determining on how close your workout compared to the "good template"


**Setup & Instructions**
To set this project up on your end:
1. Clone this repo to your github
2. Have docker installed in your local machine
3. Build container using the dockerfile in the repo
4. Launch the container
6. In your terminal, run: streamlit run frontend.py

USE THIS FILE TO YOUR REFERENCE ON SETTING UP A DOCKER CONTAINER: https://courses.engr.illinois.edu/cs225/fa2022/resources/own-machine/


Roles & Responsibilities:
Akhil & Ayush: Backend/ML + Data Collection + Integrating mediapipe & streamlit (model w/ frontend)
Sahith & Jacob: Frontend development + data collection + docker setup
