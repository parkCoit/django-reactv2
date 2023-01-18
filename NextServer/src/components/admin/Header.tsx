import React, { useEffect, useState } from 'react';
import styled from 'styled-components'
import Navbar from './Navbar';
import NavbarAuth from './NavbarAuth';
export default function Header(){
  const [token, setToken] = useState("")
  useEffect(() => {
    alert(`토큰 유지 여부 ${localStorage.getItem('session')}`)
    setToken(localStorage.getItem('session')||"")
  }, [])
    return (
      <><header>
        {token === "" ?<Navbar/> : <NavbarAuth/>}
      </header>
      </>
    )
  }
const Span = styled.span`
    color: red;
    float: right;
    padding-right: 100px
`
const HR = styled.hr`
  border: 1px solid black;
  text-align: center;
`
