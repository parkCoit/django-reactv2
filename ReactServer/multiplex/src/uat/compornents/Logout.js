import React from 'react';
import { useHistory } from 'react-router-dom';
export default function Logout(){
    const history = useHistory()
    return <button
        onClick = { e => {
            e.preventDefault()
            e.stopPropagation()
            localStorage.clear(e)
            history.push('/')
        }}> 로그아웃
    </button>}