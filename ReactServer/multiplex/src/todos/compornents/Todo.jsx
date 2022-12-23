import React from 'react';
import { useDispatch } from "react-redux";
import { deleteTodo } from "../reducers/todo.reducer";

const Todo = ({ id, text }) => {

	const dispatch = useDispatch();
	const onClick=e=>{
		e.preventDefault()
		dispatch(deleteTodo({id: id}))}

	return (
		<li className="task-item">
				{id} | {text}
				<button className="remove-task-button" onClick={onClick}>Delete</button>
		</li>
	);
};

export default Todo;