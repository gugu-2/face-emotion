import React from 'react';

const EmotionOverlay = ({ detections }) => (
  <div className="overlay">
    {detections.map((det, idx) => (
      <div key={idx} style={{
        position: 'absolute',
        top: det.box[1],
        left: det.box[0],
        width: det.box[2],
        height: det.box[3],
        border: '2px solid red',
        color: 'white'
      }}>
        {det.emotion} ({det.confidence.toFixed(2)})
      </div>
    ))}
  </div>
);

export default EmotionOverlay;
