
import { useState } from "react"
import { useDispatch } from 'react-redux'
import { addTodo } from '../reducers/todo.reducer'

const AddTodo = () => {

    const [value, setValue] = useState('')
    const dispatch = useDispatch()
    const onChange = e => setValue(e.target.value)
    const onSubmit = e => {
        e.preventDefault()
        dispatch(addTodo({text: value}))
        setValue('')
    }

    return (<>
    <h2>스케줄러</h2>
    <form onSubmit={onSubmit} method='POST'>
        <label htmlFor="todo">할 일 :</label><br/>
        <input 
            type="text" 
            id="todo" 
            name="todo"
            placeholder="할일 입력"
            value={value} 
            onChange={onChange} /><br/><br/>
        
    </form> 
    <p>할 일을 등록하시면, 스케줄 목록에 출력됩니다.</p>
    </>)
}
export default AddTodo