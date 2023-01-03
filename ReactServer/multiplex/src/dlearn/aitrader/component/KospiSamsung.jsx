import {useState} from 'react'
import Services from "dlearn/aitrader/api"



const KoreanClassify = () => {
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
        alert(`보내는 값 : ${JSON.stringify(request)}`)
        Services.samsungKospi(request).then(res => {
            const json = JSON.parse(res)
            alert(`사용자 이름 : ${JSON.stringify(json)}`)
            setOutPuts(json['data'])
        })
    }
        
    

    return (<>
    <h2>언어 측정률</h2>
    DNN : <input type="text" name="string" onChange={onChange} /><br/>
    <button onClick={onClick}>DNN 주가 예측</button>
    DNN_Ensemble : <input type="text" name="string" onChange={onChange} /><br/>
    <button onClick={onClick}>주가 예측</button>
    LSTM : <input type="text" name="string" onChange={onChange} /><br/>
    <button onClick={onClick}>주가 예측</button>
    LSTM_Ensemble : <input type="text" name="string" onChange={onChange} /><br/>
    <button onClick={onClick}>주가 예측</button>
    <table>
        <thead>
            <tr>
                <th>주가 예측 </th>
            </tr>
        </thead>
        <tbody>
                <tr><td>{outputs}</td></tr>
        </tbody>
    </table>
    <p>버튼을 클릭하시면, 언어 측정률이 출력됩니다.</p>
    
    </>)
}
export default KoreanClassify