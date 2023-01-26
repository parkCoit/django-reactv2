
import { useState } from "react"
import {userSignup} from 'uat/api'
import signUpService from 'uat/api'

const SignUp = () =>{

    const [inputs, setInputs] = useState({})
    const {email, password, nickname} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const request = {email, password, nickname}
        alert(`사용자 이름 : ${JSON.stringify(request)}`)
        userSignup(request)
        .then((res) => {
            console.log(`response is ${res.config.data}`)
            localStorage.setItem('token', JSON.stringify(res.config.data))
        })
        .catch((err)=>{
            console.log(err)
            alert('아이디와 비밀번호를 다시입력')
        })
    }

    const [signup, setSignup] = useState()

    const insertDummy = e => {
        e.preventDefault()
        signUpService.signUp2().then(res=>{
            alert(res)
        })
    }

    return(<>
        EMAIL : <input type="text" name="email" onChange={onChange} /><br/>
        PASSWORD : <input type="text" name="password" onChange={onChange} /><br/>
        NICKNAME : <input type="text" name="nickname" onChange={onChange} /><br/>
        <button onClick={onClick}> 회원가입 </button>
        <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>
        <button onClick={insertDummy}>더미 </button>
    </>)
}

export default SignUp







