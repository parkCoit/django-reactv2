
import { createSlice } from "@reduxjs/toolkit"
import { v4 as uuidv4 } from 'uuid'


const todoSlice = createSlice({
  name: 'todos',
  initialState: [],
  reducers : {
    addTodo: (state, action) => {
      const newTodo = {
        id: uuidv4(),
        text: action.payload.text
      }
      state.push(newTodo)
    }, 
    deleteTodo: (state, action) => {
      return state.filter((todo) => todo.id !== action.payload.id)
    }
  }
})

export const { addTodo, deleteTodo } = todoSlice.actions

export default todoSlice.reducer