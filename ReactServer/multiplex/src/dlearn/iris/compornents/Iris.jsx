import { useState } from "react"
import "uat/style/Login.css"
import {getiris, postiris} from 'dlearn/iris/api'

const Stroke = () =>{

    const [inputs, setInputs] = useState({})
    const {SepalLengthCm, SepalWidthCm,
         PetalLengthCm, PetalWidthCm} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onGetClick = e => {
        e.preventDefault()
        const request = [SepalLengthCm, SepalWidthCm,
            PetalLengthCm, PetalWidthCm]
        
        alert(`정보 : ${JSON.stringify(request)}`)
        getiris(request)
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
        const request = {SepalLengthCm, SepalWidthCm,
            PetalLengthCm, PetalWidthCm}
        alert(`정보 : ${JSON.stringify(request)}`)
        postiris(request)
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
    <h1>Iris GET방식</h1>
        SepalLengthCm : <input type="text" name="SepalLengthCm" onChange={onChange} /><br/>
        SepalWidthCm : <input type="text" name="SepalWidthCm" onChange={onChange} /><br/>
        PetalLengthCm : <input type="text" name="PetalLengthCm" onChange={onChange} /><br/>
        PetalWidthCm : <input type="text" name="PetalWidthCm" onChange={onChange} /><br/>
        <button onClick={onGetClick}> Iris </button>
    </form>
    <form method="post">
    <h1>Iris POST방식</h1>
        SepalLengthCm : <input type="text" name="SepalLengthCm" onChange={onChange} /><br/>
        SepalWidthCm : <input type="text" name="SepalWidthCm" onChange={onChange} /><br/>
        PetalLengthCm : <input type="text" name="PetalLengthCm" onChange={onChange} /><br/>
        PetalWidthCm : <input type="text" name="PetalWidthCm" onChange={onChange} /><br/>
        <button onClick={onPostClick}> Iris </button>
    </form>
    </>)
}

export default Stroke