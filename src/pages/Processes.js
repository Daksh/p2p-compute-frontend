import React, {useState, useEffect} from 'react'
import { ChakraProvider, Table, Thead, Th, Tr, Td, Tbody} from '@chakra-ui/react'
import { useToast } from '@chakra-ui/react'
import io from "socket.io-client";
import {DownloadButton} from "./DownloadButton"

let endPoint = "http://localhost:5001";
let socket = io.connect(`${endPoint}`);

export const Processes = () => {

    const [processed, setProcessed] = useState([{id: '1', data:'aa'}])
    const toast = useToast()
    useEffect(() => {
        socket.on('connect', function() {
          socket.emit('connected');
        });
    
        socket.on("processing_done", (output) => {
            toast({
                title: 'Processed successfully',
                description: "",
                status: 'success',
                duration: 5000,
                isClosable: true,
              })
          setProcessed([...processed, {id: `process-${processed.length}`, data: output}])
        })
        socket.on("processing_failed", () => {
            toast({
                title: 'Processing failed',
                description: "",
                status: 'error',
                duration: 5000,
                isClosable: true,
              })
        })
      }, []);

      return (
          <ChakraProvider>
          <Table size='lg' colorScheme={"twitter"} variant="simple" style={{fontSize:"1.em", width: "40%", textAlign: "center", margin: "auto", marginTop: "10%"}}>
            <Thead  style={{fontSize:"2em"}}>
                <Tr>
                <Th>Id</Th>
                <Th>Data</Th>
                <Th>Status</Th>
                </Tr>
            </Thead>
            <Tbody>
            {processed.map(process => (<Tr key={process.id}>
                <Td>{process.id}</Td>
                <Td><DownloadButton processOutput={process.data}></DownloadButton></Td>
                <Td>ok</Td>
            </Tr>))}
            </Tbody>
            </Table>
          </ChakraProvider>
      )

}