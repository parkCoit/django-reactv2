import 'uat/style/UserList.css'
import {useEffect, useState} from 'react'
import axios from 'axios'
import {ListForm} from 'uat'

export default function UserList(){
    const [list, setList] = useState([])
    useEffect(()=>{
        axios
        .get('http://localhost:8000/blog/auth/user-list')
        .then(res => {setList(res.data)})
        .catch(err => {console.log(err)})
    }, [])
   
    return <>
        <ListForm list={list}/>
    </>
}

