
import "uat/style/Login.css"
import {stroke} from 'stroke/api'

const Stroke = () =>{

    const onClick = e => {
        e.preventDefault()
        stroke()
        .then((res) => {
            console.log(`response is ${res.config.data}`)
            localStorage.setItem('token', JSON.stringify(res.config.data))
        })
        .catch((err)=>{
            console.log(err)
            alert('에러')
        })
    }

    return(<>
        <button onClick={onClick}> Stroke </button>
    </>)
}

export default Stroke