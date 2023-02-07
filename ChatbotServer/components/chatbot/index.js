import React from "react";
//import ChatBot from 'react-simple-chatbot';
import Wrapper from './styles';
//import steps from './steps';
//import { Socket } from "dgram";
import ChatbotSocket from './socket';


function ChatbotWrapper() {
  return (
    <Wrapper>
      {/* <ChatBot
        steps={steps}
        floating recognitionEnable
      /> */}
      <ChatbotSocket/>
    </Wrapper>
  );
}

export default ChatbotWrapper;