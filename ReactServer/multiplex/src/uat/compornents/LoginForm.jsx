
import { useState } from "react"
import "uat/style/Login.css"
import {userLogin} from 'uat/api'
import {useNavigate} from "react-router-dom"

export default function LoginForm(){

    const [inputs, setInputs] = useState({})
    const {user_email, password} = inputs
    const navigate  = useNavigate()

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const request = {user_email, password}
        alert(`사용자 이름 : ${JSON.stringify(request)}`)
        userLogin(request)
        .then((res) => {
            alert(JSON.stringify(res.data))
            localStorage.setItem('loginUser', JSON.stringify(res.data))
            alert(`저장된 데이터 : ${localStorage.getItem('loginUser')}`)
            navigate('/home')  
        })
        .catch((err)=>{
            console.log(err)
            alert('아이디와 비밀번호를 다시입력')
        })
    }

    return(<>
        EMAIL : <input type="text" name="user_email" onChange={onChange} /><br/>
        PASSWORD : <input type="text" name="password" onChange={onChange} /><br/>
        <button onClick={onClick}> 로그인 </button>
    </>)
}





