import React, { useRef, useEffect } from 'react';

const VideoFeed = () => {
  const videoRef = useRef();
  const canvasRef = useRef();
  const intervalRef = useRef();

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        videoRef.current.srcObject = stream;
      });
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
    };
  }, []);

  useEffect(() => {
    if (!videoRef.current) return;
    intervalRef.current = setInterval(async () => {
      if (videoRef.current.readyState === 4) {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
        canvas.toBlob(async (blob) => {
          if (blob) {
            try {
              const { detectEmotion } = await import('../services/api');
              const detections = await detectEmotion(blob);
              if (typeof window.setDetections === 'function') window.setDetections(detections);
            } catch (e) {}
          }
        }, 'image/jpeg');
      }
    }, 2000);
    return () => clearInterval(intervalRef.current);
  }, []);

  useEffect(() => {
    window.setDetections = (dets) => {
      if (typeof window._setDetections === 'function') window._setDetections(dets);
    };
  }, []);

  return (
    <div style={{ position: 'relative' }}>
      <video ref={videoRef} autoPlay width="600" height="400" />
      <canvas ref={canvasRef} width={600} height={400} style={{ display: 'none' }} />
    </div>
  );
};

export default VideoFeed;
