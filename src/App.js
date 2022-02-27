import React, { useEffect, useState } from 'react';
import './App.css';
import {Route, Routes, BrowserRouter} from 'react-router-dom'
import {Home, Jobs, Network, Upload} from './pages'
import { ChakraProvider} from '@chakra-ui/react';
import io from "socket.io-client";

let endPoint = "http://localhost:5001";
let socket = io.connect(`${endPoint}`);
let machinesGlobal = {available: [], running: []};

function App() {

  const [machines, setMachines] = useState(machinesGlobal)
  const [connected, setConnected] = useState(false)
  useEffect(() => {
    socket.on('connect', function() {
      socket.emit('connected');
      socket.emit("fetch_m")
    });
    socket.on("updated_machines", (msg) => {
      setMachines(msg)
    })
  }, [])

  const onConnect = () => {
    setConnected(true)
  }

  return (
    <ChakraProvider>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/network" element={<Jobs machines={machines} connected={connected} onConnect={onConnect} />} />
        <Route path="/upload" element={<Network />}/>
        <Route path="/jobs" element={<Network/>}/>
      </Routes>
    </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;
