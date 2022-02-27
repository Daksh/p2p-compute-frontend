import React, { useState, useEffect } from "react";
import {
  ChakraProvider,
  Table,
  Thead,
  Th,
  Tr,
  Td,
  Tbody,
} from "@chakra-ui/react";
import { useToast } from "@chakra-ui/react";
import io from "socket.io-client";
import { DownloadButton } from "./DownloadButton";
import "./job.scss";

let endPoint = "http://localhost:5001";
let socket = io.connect(`${endPoint}`);

export const Machines = ({ machines }) => {
  const toast = useToast();
  useEffect(() => {
    socket.on("connect", function () {
      socket.emit("connected");
    });
  });
  return (
    <ChakraProvider>
      <Table
        size="lg"
        colorScheme={"twitter"}
        variant="simple"
        style={{
          fontSize: "2rem",
          width: "40%",
          textAlign: "center",
          margin: "auto",
          marginTop: "3%",
        }}
      >
        <Thead style={{ fontSize: "2em" }}>
          <Tr>
            <Th>Id</Th>
            <Th>Status</Th>
          </Tr>
        </Thead>
        <Tbody>
          {machines.running.map((machine) => (
            <Tr key={machine}>
              <Td>{machine}</Td>
              <Td>running</Td>
            </Tr>
          ))}
          {machines.available.map((machine) => (
            <Tr key={machine}>
              <Td>{machine}</Td>
              <Td>available</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </ChakraProvider>
  );
};

