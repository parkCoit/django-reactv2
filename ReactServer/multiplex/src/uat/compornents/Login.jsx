
import { useState } from "react"
import "uat/style/Login.css"
import {userLogin} from 'uat/api'

const Login = () =>{

    const [inputs, setInputs] = useState({})
    const {email, password} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const request = {email, password}
        alert(`사용자 이름 : ${JSON.stringify(request)}`)
        userLogin(request)
        .then((res) => {
            console.log(`response is ${res.config.data}`)
            localStorage.setItem('token', JSON.stringify(res.config.data))
        })
        .catch((err)=>{
            console.log(err)
            alert('아이디와 비밀번호를 다시입력')
        })
    }

    return(<>
        EMAIL : <input type="text" name="email" onChange={onChange} /><br/>
        PASSWORD : <input type="text" name="password" onChange={onChange} /><br/>
        <button onClick={onClick}> 로그인 </button>
    </>)
}

export default Login



