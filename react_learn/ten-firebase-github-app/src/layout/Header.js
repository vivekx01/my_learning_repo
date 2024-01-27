import React,{useState,useContext} from "react";
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,NavItem,NavLink,NavbarText
} from "reactstrap"

import {Link} from "react-router-dom"
import {UserContext} from "../context/UserContext"

const Header = () =>{
    const context = useContext(UserContext)
    const [isOpen,setIsOpen] = useState(false)
    const toggle = () => setIsOpen(!isOpen)
    return (
        <Navbar color="dark" dark expand="md">
            <NavbarBrand>
                <Link to="/" className="text-white" style={{textDecoration: 'none'}}>
                    Github-Fire App
                </Link>
            </NavbarBrand>
            <NavbarText className="text-white">
                {context?.user?.email ? context.user.email : ""}
            </NavbarText>
            <NavbarToggler onClick={toggle} />
            <Collapse isOpen={isOpen} navbar>
            <Nav className="ms-auto" navbar>
                {
                    context?.user ? (
                        <NavItem>
                            <NavLink onClick={()=>{context.setUser(null)}} className="text-white" style={{cursor:'pointer'}}>
                                Logout
                            </NavLink>
                        </NavItem>
                    ) : (
                        <>
                        <NavItem>
                            <NavLink tag={Link} to='/signup' className="text-white" style={{ cursor: 'pointer' }}>
                                Signup
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink tag={Link} to='/signin' className="text-white" style={{ cursor: 'pointer' }}>
                                    Signin
                            </NavLink>
                        </NavItem>
                        </>
                    )
                }
                {/* <NavItem>
                        <NavLink>
                            Hello Vivek!
                        </NavLink>
                </NavItem> */}
                
                
            </Nav>
            </Collapse>
        </Navbar>
    )
}

export default Header