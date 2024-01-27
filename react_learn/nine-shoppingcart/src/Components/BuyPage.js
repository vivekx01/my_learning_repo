import React, { useState, useEffect } from "react";
import axios  from "axios";
import { faker } from '@faker-js/faker';
import { Col, Container,  Row } from "reactstrap";
import CardItem from "./CardItem";
const apiKey = "wlTr6mxMHJ9SGQRuAvp5JDsquG9SK13dxs80depfF4AzWzW86AvWRt7J";

const url = "https://api.pexels.com/v1/search?query=laptop&per_page=6&page=1";

const localurl = "https://mocki.io/v1/599331b1-31fb-4fa6-b3fa-87cdc81b384e"

const BuyPage = ({ addInCart }) => {
    const [product, setProduct] = useState([])
    const fetchPhotos = async ()=>{
        const {data} = await axios.get(url,{
            headers:{
                Authorization: apiKey
            }
        }) 
        const {photos} = data;
        const allProduct = photos.map(photo=>({
            smallImage: photo.src.medium,
            tinyImage: photo.src.tiny,
            productName: faker.random.word(),
            productPrice: faker.commerce.price(),
            id: faker.datatype.uuid()
        }))
        setProduct(allProduct)
        console.log(allProduct);
    }

    // const fetchPhotos = async ()=>{
    //     const {data} = await axios.get(localurl,{})
    //     const {photos} = data;
    //     const allProduct = photos.map(photo=>({
    //         smallImage: photo.src.medium,
    //         tinyImage: photo.src.tiny,
    //         productName: faker.random.word(),
    //         productPrice: faker.commerce.price(),
    //         id: faker.datatype.uuid()
    //     }))
    //     setProduct(allProduct)
    // }

    useEffect(() => {
        fetchPhotos()
    }, [])

    return (
        <Container fluid>
            <h1 className="text-success text-center">
                Buy Page
            </h1>
            <Row>
                {product.map(product=>(
                    <Col md={4} key={product.id}>
                        <CardItem product={product} addInCart={addInCart}></CardItem>

                    </Col>
                ))}
            </Row>
        </Container>
    )

}

export default BuyPage