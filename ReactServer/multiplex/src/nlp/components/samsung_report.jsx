import {useState} from 'react'
import samsungService from "nlp/api"


const SamsungReport = () => {
    const [movie, setMovie] = useState()

    const onClick = e => {
        e.preventDefault()
        samsungService.samsung().then(res => {
            const json = JSON.parse(res)
            setMovie(json['data'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i = 0; i< arr.length; i++) arr[i].value = ""
    }
        
    

    return (<>
    <h2>삼성 리포트</h2>
    <button onClick={onClick}>삼성 리포트</button>
    <p>버튼을 클릭하시면, 삼성 리포트 목록이 출력됩니다.</p>
    <table>
        <teahd>
            <tr>
                <th>단어 </th><th >개수</th>
            </tr>
        </teahd>
        <tbody>
            {movie && movie.map(({word,num})=> (
                <tr key={word}><td>{word}</td><td>{num}</td></tr>
                ))}
        </tbody>
    </table>
    </>)
}
export default SamsungReport