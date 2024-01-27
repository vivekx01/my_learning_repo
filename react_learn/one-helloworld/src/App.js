import React from "react"
import "./style.css"
import Button from "./Button"
const App= ()=>{
    return(
        <div>
            <h1 style={{textAlign:"center"}}>Hello World</h1>
            <Button title="Heyy"></Button>
            <Button title="Hello"></Button>
            <Button></Button>

            {/* <button className="button ">Heyy</button>
            <button className="button ">Hello</button> */}
        </div>
        
    )
}

export default App