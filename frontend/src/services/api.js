import axios from 'axios';

export const detectEmotion = async (frameBlob) => {
  const form = new FormData();
  form.append('file', frameBlob);
  const response = await axios.post('http://localhost:8000/detect', form, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data.detections;
};
