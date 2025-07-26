import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

window._setDetections = null;
ReactDOM.render(<App />,
  document.getElementById('root'),
  () => {
    window._setDetections = (dets) => {
      const rootInstance = document.getElementById('root')._reactRootContainer._internalRoot.current.child.stateNode;
      if (rootInstance && typeof rootInstance.setDetections === 'function') {
        rootInstance.setDetections(dets);
      }
    };
  }
);
