import React, { useState } from "react";
import {
    FormGroup,
    Input,
    InputGroup,
    Button,
    Form,
    Container
} from "reactstrap";
import { v4 } from "uuid";

const TodoForm = ({addTodos}) =>{
    const [todoString,setTodoString] = useState("");
    const handleSubmit = e => {
        e.preventDefault()
        if (todoString==="") {
            return alert("Please fill some value")
        }
        const todo = {
            todoString,
            id: v4(),
        }
        addTodos(todo) //this method is passsed as a prop
        setTodoString("")
    }
    return(
        <Form onSubmit={handleSubmit}>
            <FormGroup>
                <InputGroup>
                <Input 
                type="text"
                name="todo"
                id="todo"
                placeholder="Enter a Todo"
                value={todoString}
                onChange={e=> setTodoString(e.target.value)}
                />
                <Button
                color="success"
                >Add Todo</Button>
                </InputGroup>
            </FormGroup>
        </Form>
    )

}

export default TodoForm;