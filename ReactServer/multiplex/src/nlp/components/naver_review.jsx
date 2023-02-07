import {useState} from 'react'
import Services from "nlp/api"



const NaverReview = () => {
    const [inputs, setInputs] = useState({})
    const [outputs, setOutPuts] = useState()
    const {string} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const request = {string}
        Services.naverReview(request).then(res => {
            const json = JSON.parse(res)
            alert(`사용자 이름 : ${JSON.stringify(json)}`)
            setOutPuts(json['data'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i = 0; i< arr.length; i++) arr[i].value = ""
    }
        
    

    return (<>
    <h2>긍정 측정률</h2>
    문장 : <input type="text" name="string" onChange={onChange} /><br/>
    <button onClick={onClick}>긍정 측정률</button>
    <table>
        <thead>
            <tr>
                <th>긍정 측정률 </th>
            </tr>
        </thead>
        <tbody>
                <tr><td>{outputs}</td></tr>
        </tbody>
    </table>
    <p>버튼을 클릭하시면, 긍정 측정률이 출력됩니다.</p>
    
    </>)
}
export default NaverReview