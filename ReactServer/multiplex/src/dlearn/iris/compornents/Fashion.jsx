import { useState } from "react"
import "uat/style/Login.css"
import {getFashion, postFashion} from 'dlearn/iris/api'

const Fashion = () =>{

    const [inputs, setInputs] = useState({})
    const {Num} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onGetClick = e => {
        e.preventDefault()
        alert(`정보 : ${JSON.stringify(Num)}`)
        getFashion(Num)
        .then((response) => {
            console.log(`response is ${response.data.result}`)
            localStorage.setItem('token', JSON.stringify(response.data.result))
            alert(`정보 : ${JSON.stringify(response.data.result)}`)
            
        })
        .catch((err)=>{
            console.log(err)
            alert('에러')
        })
    }

    const onPostClick = e => {
        e.preventDefault()
        const testNum = {Num}
        alert(`정보 : ${JSON.stringify(testNum)}`)
        postFashion(testNum)
        .then((response) => {
            console.log(`response is ${response.data.result}`)
            localStorage.setItem('token', JSON.stringify(response.data.result))
            alert(`정보 : ${JSON.stringify(response.data.result)}`)
            
        })
        .catch((err)=>{
            console.log(err)
            alert('에러')
        })
    }

    return(<>
    <form method="get">
    <h1>FASHION GET방식</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" placeholder="테스트할 옷 번호" name="Num" onChange={onChange}/>
    <button onClick={onGetClick}>옷의 카테고리 찾기</button>
    </form>
    <form method="post">
    <h1>FASHION POST방식</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" placeholder="테스트할 옷 번호" name="Num" onChange={onChange}/>
    <button onClick={onPostClick}>옷의 카테고리 찾기</button>
    </form>
    </>)
}

export default Fashion