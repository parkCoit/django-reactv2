import { useState } from "react"

const Counter = () => {
    const [count,setCount] = useState(10)
    return (<>
        <div>카운트 수 : {count}
            <h3>카운트 플러스</h3>
            <button onClick={()=>{setCount(count + 1)}}>더하기</button>
            <button onClick={()=>{setCount(count - 1)}}>빼기</button>
            
        </div>
        </>)
}
export default Counter 