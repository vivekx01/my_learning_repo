import React from "react";
import { FaTimes, FaPen, FaRegCircle } from "react-icons/fa";
const Icon = ({ name }) => {
    switch (name) {
        case 'circle':
            return <FaRegCircle></FaRegCircle>
        case 'cross':
            return <FaTimes></FaTimes>
        default:
            return <FaPen></FaPen>
    }

}

export default Icon;