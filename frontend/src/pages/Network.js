import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import { UploadButton } from "./UploadButton";
import {Download} from "./Download";

let endPoint = "http://localhost:5001";
let socket = io.connect(`${endPoint}`);

const Network = () => {
  const [uploading, setUploading] = useState(false)
  const [processOutput, setProcessOutput] = useState()
  
  useEffect(() => {
    socket.on("processing_done", (msg) => {
      setProcessOutput(msg)
      setUploading(false)
    })
  }, []);

  const setContent = (content) => {
    setUploading(true)
    socket.emit("file_uploaded", content);
  };

  

  return (
    <div>
      <UploadButton uploading={uploading} setContent={setContent}/>
      {processOutput ? (<Download processOutput={processOutput}/>) : (<></>)}
    </div>
  );
}
export default Network;
