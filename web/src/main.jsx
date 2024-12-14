import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Math from './subj/Math.jsx';
import Eng from './subj/Eng.jsx';
import App from './App.jsx';
import Home from './Home.jsx'
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Router>
      <Routes>
        <Route path="/Math" element={<Math />} />
        <Route path="/Eng" element={<Eng />} />
        <Route path="/" element={<Home />} />
        <Route path="/push" element={<App />} />
      </Routes>
    </Router>
  </StrictMode>,
);
