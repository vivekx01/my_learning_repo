import React, { useState, useEffect } from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col } from "reactstrap";
import Axios from 'axios';
import './App.css';
import Cardp from "./Cardp"


function App() {
  const [details, setDetails] = useState({})
  const fetchDetails = async () => {
    const {data} = await Axios.get('https://randomuser.me/api') //directly extracting "data" from json object
    const details = data.results[0]
    console.log("Response: ", details.picture.large);
    setDetails(details)
  }
  useEffect(() => {
    fetchDetails()
  }, [])
  return (
    <Container fluid className='p-4 bg-primary App'>
      <Row>
        <Col md={4} className='offset-md-4 mt-4'>
        <Cardp details={details}></Cardp>
        </Col>
      </Row>

    </Container>

  );
}

export default App;
