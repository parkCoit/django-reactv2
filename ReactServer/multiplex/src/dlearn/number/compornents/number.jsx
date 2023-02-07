import { useState } from "react"
import {getnumber, postnumber} from 'dlearn/number/api'

const Number = () =>{

    const [inputs, setInputs] = useState({})
    const {Num} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onGetClick = e => {
        e.preventDefault()
        alert(`인식 한 숫자 : ${JSON.stringify(Num)}`)
        getnumber(Num)
        .then((response) => {
            console.log(`response is ${response.data.result}`)
            localStorage.setItem('token', JSON.stringify(response.data.result))
            alert(`인식 한 숫자 : ${JSON.stringify(response.data.result)}`)
            
        })
        .catch((err)=>{
            console.log(err)
            alert('에러')
        })
    }

    const onPostClick = e => {
        e.preventDefault()
        const testNum = {Num}
        alert(`인식 한 숫자 : ${JSON.stringify(testNum)}`)
        postnumber(testNum)
        .then((response) => {
            console.log(`response is ${response.data.result}`)
            localStorage.setItem('token', JSON.stringify(response.data.result))
            alert(`인식 한 숫자 : ${JSON.stringify(response.data.result)}`)
            
        })
        .catch((err)=>{
            console.log(err)
            alert('에러')
        })
    }

    return(<>
    <form method="get">
    <h1>Number GET방식</h1>
    <p>사진 번호를 입력해주세요.(9999번까지)</p>
    <input type="text" placeholder="테스트할 옷 번호" name="Num" onChange={onChange}/>
    <button onClick={onGetClick}>손글씨 찾기</button>
    </form>
    <form method="post">
    <h1>Number POST방식</h1>
    <p>사진 번호를 입력해주세요.(9999번까지)</p>
    <input type="text" placeholder="테스트할 옷 번호" name="Num" onChange={onChange}/>
    <button onClick={onPostClick}>손글씨 찾기</button>
    </form>
    </>)
}

export default Number