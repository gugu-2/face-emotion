import React from 'react';
import VideoFeed from './components/VideoFeed';
import EmotionOverlay from './components/EmotionOverlay';

function App() {
  const [detections, setDetections] = React.useState([]);

  return (
    <div>
      <VideoFeed setDetections={setDetections} />
      <EmotionOverlay detections={detections} />
    </div>
  );
}

export default App;
