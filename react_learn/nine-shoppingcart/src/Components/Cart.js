import React from "react"
import {Container,ListGroup,ListGroupItem,Button,CardHeader,CardBody,
Card,CardFooter,Col,Row} from "reactstrap"

const Cart = ({cartItem,removeItem,buyNow}) =>{
    let amount = 0;

    cartItem.forEach(item=>{
        amount = parseFloat(amount) + parseFloat(item.productPrice)
    })

    return (
        <Container>
            <h1 className="text-success">Your Cart</h1>
            <ListGroup>
                {cartItem.map(item=>(
                    <ListGroupItem>
                        <Row>
                            <Col>
                            <img height={80}
                             src={item.tinyImage} alt="item"
                             />
                            </Col>
                            <Col className="text-center">
                                <div className="text-primary">
                                    {item.productName}
                                </div>
                                <span>
                                    Price: {item.productPrice}  
                                </span>
                                <span><br /></span>
                                <Button color="danger"
                                onClick={()=>{removeItem(item)}}
                                >Remove</Button>
                            </Col>
                        </Row>
                    </ListGroupItem>
                ))}
            </ListGroup>
            {/* if everything is empty */}
            {
                cartItem.length >= 1 ? (
                    <Card className="text-center mt-3">
                        <CardHeader>
                            Grand Total 
                        </CardHeader>
                        <CardBody>
                            Your amount for {cartItem.length} products is $ {amount}
                        </CardBody>
                        <CardFooter>
                            <Button color="success" onClick={buyNow}>Checkout</Button>
                        </CardFooter>
                    </Card>
                ) : (
                    <h1 className="text-warning">Cart is empty</h1>
                )
            }
        </Container>
    )

}

export default Cart