import React from "react";
import {Card,CardBody,CardTitle,CardText} from "reactstrap";
import {FaEnvelope,FaMapMarkedAlt,FaPhoneAlt} from "react-icons/fa"

const Cardp= ({details}) =>{
    return(
        <Card>
            <CardBody className="text-center">
                <img height="150" width="150" 
                className="rounded-circle img-thumbnail border-danger" 
                src={details.picture?.large} />
                <CardTitle className="text-primary">
                    <h1>
                        <span>{details.name?.title} </span>
                        <span>{details.name?.first} </span>
                        <span>{details.name?.last}</span>
                    </h1>
                </CardTitle>
                <CardText>
                    <FaMapMarkedAlt/>
                    { details.location?.city}
                    <p>
                    <FaPhoneAlt />
                    {details.phone}
                    </p>

                </CardText>
            </CardBody>
        </Card>
    )
}

export default Cardp