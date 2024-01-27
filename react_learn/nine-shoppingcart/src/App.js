import React,{useState} from 'react';
import "bootstrap/dist/css/bootstrap.min.css"
import 'react-toastify/dist/ReactToastify.css';
import {ToastContainer, toast } from 'react-toastify';
import BuyPage from "./Components/BuyPage"
import { Container,Row,Col } from 'reactstrap';
import Cart from "./Components/Cart";
import './App.css';

function App() {
  const [cartItem,setCartItem] = useState([]);

  const addInCart = item =>{
    const isAlreadyAdded = cartItem.findIndex(function(array){
      return array.id === item.id
    })
    if (isAlreadyAdded!==-1) {
      return toast("already added in the cart",{
        type: "error"
      });
    }
    setCartItem([...cartItem,item]);
  }

  const buyNow=()=>{
    setCartItem([])
    toast("Purchase Complete",{
      type: "success"
    });
  }

  const removeItem= item =>{
    setCartItem(cartItem.filter(singleItem=> singleItem.id !== item.id))
  }

  return (
    <Container fluid>
      <ToastContainer></ToastContainer>
      <Row>
        <Col md="8">
          <BuyPage addInCart={addInCart}></BuyPage>
        </Col>
        <Col md="4">
          <Cart cartItem={cartItem} removeItem={removeItem} buyNow={buyNow}></Cart>
        </Col>
      </Row>
    
    </Container>
  );
}

export default App;
