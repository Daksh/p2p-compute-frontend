import React from 'react'
import {Button} from '@chakra-ui/react'

export const DownloadButton = ({processOutput}) => {
    const downloadTxtFile = () => {
        const element = document.createElement("a");
        const file = new Blob([processOutput], {
          type: "text/plain"
        });
        element.href = URL.createObjectURL(file);
        element.download = `${Date.now()}-processed.txt`;
        document.body.appendChild(element);
        element.click();
      };

      return (
          <Button onClick={downloadTxtFile}>Download</Button>
      )

}