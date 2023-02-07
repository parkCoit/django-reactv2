import {useState} from 'react'
import Services from "dlearn/aitrader/api"



const KoreanClassify = () => {
    const [inputs, setInputs] = useState({})
    const [outputs, setOutPuts] = useState()
    const {num} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const request = {num}
        alert(`보내는 값 : ${JSON.stringify(request)}`)
        Services.samsungKospi(request).then(res => {
            const json = JSON.parse(res)
            alert(`사용자 이름 : ${JSON.stringify(json)}`)
            setOutPuts(json['data'])
        })
    }
        
    

    return (<>
    <h2>주가 예측</h2>
    날짜 입력 : <input type="text" name="num" onChange={onChange} /><br/>
    <button onClick={onClick}>주가 예측</button>
    <table>
        <thead>
            <tr>
                <th>DNN 결과 </th><th>DNN 양상블 결과 </th><th>LSTM 결과 </th><th>LSTM 양상블 결과 </th>
            </tr>
        </thead>
        <tbody>
            {outputs && outputs.map(({dnn, dnnensemble, lstm, lstmensemble})=> (
                <tr key={dnn}>
                    <td>{dnn}</td>
                    <td>{dnnensemble}</td>
                    <td>{lstm}</td>
                    <td>{lstmensemble}</td>      
                </tr>
                
                ))}
        </tbody>
    </table>
    <p>버튼을 클릭하시면, 언어 측정률이 출력됩니다.</p>
    
    </>)
}
export default KoreanClassify