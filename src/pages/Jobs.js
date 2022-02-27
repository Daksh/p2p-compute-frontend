import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import { Machines } from "./Machines";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  Button,
} from "@chakra-ui/react";

let endPoint = "http://localhost:5001";
let socket = io.connect(`${endPoint}`);

const Jobs = ({ machines, connected, onConnect }) => {
  const [uploading, setUploading] = useState(false);
  const [processOutput, setProcessOutput] = useState();

  useEffect(() => {
    socket.on("connect", function () {
      socket.emit("connected");
    });

    socket.on("processing_done", (msg) => {
      setProcessOutput(msg);
    });

    socket.on("updated_machines", (msg) => {
      console.log("updated machines");
      console.log(msg);
    });
  }, []);

  const setContent = (content) => {
    setUploading(true);
    socket.emit("file_uploaded", content);
    setTimeout(() => setUploading(false), 3000);
  };

  const onRegister = () => {
    console.log("onRegister called");
    socket.emit("register_this_machine");
    onConnect();
  };

  return (
    <div style={{ minHeight: "100vh" }}>
      <Breadcrumb
        separator=">"
        fontSize="lg"
        style={{ fontSize: "1.5em", padding: "20px" }}
      >
        <BreadcrumbItem>
          <BreadcrumbLink href="/">Home</BreadcrumbLink>
        </BreadcrumbItem>

        <BreadcrumbItem>
          <BreadcrumbLink href="/jobs">Process</BreadcrumbLink>
        </BreadcrumbItem>

        {/* <BreadcrumbItem isCurrentPage>
          <BreadcrumbLink href='/network'>Process</BreadcrumbLink>
        </BreadcrumbItem> */}
      </Breadcrumb>
      <Machines machines={machines}></Machines>
      <div style={{ marginTop: "5%" }}>
        <Button
          onClick={onRegister}
          size="lg"
          isDisabled={connected}
          colorScheme={connected ? "green" : "blue"}
          style={{
            marginTop: "10%",
            margin: "auto",
            display: "block",
            fontSize: "2rem",
          }}
        >
          {connected ? "Connected" : "Connect"}
        </Button>
      </div>
    </div>
  );
};
export default Jobs;

