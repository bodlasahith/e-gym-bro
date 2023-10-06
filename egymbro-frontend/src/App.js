import React, { useState, useRef } from 'react';
import './App.css';
import {Upload, Camera} from 'react-bootstrap-icons';
import Education from './Education';
import Links from './Links';

function App() {
  const [uploadClicked, setUploadClicked] = useState(false);
  const [cameraActive, setCameraActive] = useState(false);
  const videoRef = useRef(null);

  const handleUploadClick = () => {
    setUploadClicked(true);
    setCameraActive(false);
  };

  const handleCameraClick = () => {
    setCameraActive(true);
    setUploadClicked(false);

    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      })
      .catch((error) => {
        console.error('Error accessing camera:', error);
        setCameraActive(false);
      });
  };

  return (
    <div className="App">
      <h1 className="title">E-GymBro</h1>
      <h2 className="title">A site to track your fitness gains quantitatively...</h2>
      <div className="button-container">
        <div className={`upload ${uploadClicked ? 'active' : ''}`} onClick={handleUploadClick}>
          <Upload className="icon"/>
        </div>
        <div className={`camera ${cameraActive ? 'active' : ''}`} onClick={handleCameraClick}>
          <Camera className="icon"/>{cameraActive && <video ref={videoRef} autoPlay />}
        </div>
      </div>
      <div className="buttons">
        <button className="go-button">Go!</button>
        <button className="education-button">Learn more about weightlifting here!</button>
      </div>
      <div className="education-page">
        <Education></Education>
        <Links></Links>
      </div>
    </div>
  );
}

export default App;
