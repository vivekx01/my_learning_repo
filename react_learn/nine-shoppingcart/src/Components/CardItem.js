import React from "react";
import {Card,CardImg,CardText,CardBody,CardTitle,Button,Container} from "reactstrap";

const CardItem = ({product, addInCart})=>{
     return (
        <Card className="mt-2 mb-1">
            <CardImg top height="250" width="100%" src={product.smallImage} />
            <CardBody className="text-center">
                <CardTitle>{product.productName}</CardTitle>
                <CardText className="secondary">Price: ${product.productPrice}</CardText>
            </CardBody>
            <Container className="mb-3 text-center">
            <Button
            color="success"
            onClick={()=>{
                addInCart(product)
            }}
            >Add to Cart</Button>

            </Container>
        </Card>
     ) 

}


export default CardItem