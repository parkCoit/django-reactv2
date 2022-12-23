
import { combineReducers} from "@reduxjs/toolkit"
import todoReducer from "todos/reducers/todo.reducer"

export default combineReducers({
    todos: todoReducer
})



