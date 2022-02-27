import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import { UploadButton } from "./UploadButton";
import {Download} from "./Download";
import { Processes } from "./Processes";
import {Breadcrumb, BreadcrumbItem, BreadcrumbLink, Button} from "@chakra-ui/react"

let endPoint = "http://localhost:5001";
let socket = io.connect(`${endPoint}`);

const Network = () => {
  const [uploading, setUploading] = useState(false)
  const [processOutput, setProcessOutput] = useState()
  
  useEffect(() => {
    socket.on('connect', function() {
      socket.emit('connected');
    });

    socket.on("processing_done", (msg) => {
      setProcessOutput(msg)
    })

    socket.on("updated_machines", (msg) => {
      console.log("updated machines")
      console.log(msg)
    })
  }, []);

  const setContent = (content) => {
    setUploading(true)
    socket.emit("file_uploaded", content);
    setTimeout(() => setUploading(false), 3000)
  };

  const onRegister = () => {
    console.log('onRegister called');
    socket.emit('register_this_machine');
  };

  return (
    <div>
      <Breadcrumb separator='>' fontSize='lg' style={{fontSize: "1.5em", padding: "20px"}} >
        <BreadcrumbItem>
          <BreadcrumbLink href='/'>Home</BreadcrumbLink>
        </BreadcrumbItem>

        <BreadcrumbItem>
          <BreadcrumbLink href='/network'>Network</BreadcrumbLink>
        </BreadcrumbItem>

        {/* <BreadcrumbItem isCurrentPage>
          <BreadcrumbLink href='/network'>Process</BreadcrumbLink>
        </BreadcrumbItem> */}
      </Breadcrumb>
      <Processes></Processes>
      <UploadButton uploading={uploading} setContent={setContent}/>
      {processOutput ? (<Download processOutput={processOutput}/>) : (<></>)}
    </div>
  );
}
export default Network;
