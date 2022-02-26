import React from 'react';
import './App.css';
import {Route, Routes, BrowserRouter} from 'react-router-dom'
import {Home, Jobs, Network, Upload} from './pages'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/network" element={<Network />} />
        <Route path="/upload" element={<Upload />}/>
        <Route path="/jobs" element={<Jobs />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
