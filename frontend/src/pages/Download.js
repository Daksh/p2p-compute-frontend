import { useEffect } from "react";
import React from "react";

export const Download = ({processOutput}) => {
  useEffect(() => {
      downloadTxtFile();
  }, [])
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
      <></>
  );
}