import React from 'react';
import Head from 'next/head'
import dynamic from 'next/dynamic';

import styles from '../styles/Home.module.css';
const ChatBot = dynamic(import('../components/chatbot'), { ssr: false });

class Home extends React.Component {
  state = {
    ip: {}
  }
  componentDidMount() {
    this.setState({
      iploading: true
    })
    fetch('https://ipapi.co/json/').then(res => res.json()).then(data => {
      this.setState({
        ip: data,
        iploading: false
      })
      console.log(data)
    }).catch(err => {
      console.err(err);
      this.setState({
        iploading: false
      })
    })
  }
  render() {
    const { ip, iploading } = this.state;
    return (
     
      <div className={styles.container}>
        <Head>
          <title>Chat bot sandbox with NextJS</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <div className={styles.main}>
          <ChatBot />
          
        </div>
      </div >
    )
  }
}

export default Home;