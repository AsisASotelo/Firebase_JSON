import React, {Component} from 'react';
import {Navbar, NavbarBrand,Jumbotron, Nav, NavbarToggler,Collapse, NavItem,NavLink} from 'reactstrap';



class Header extends Component{

    constructor(props){
        super(props);
            this.state={
                isNavOpen:false
            };
            this.toggleNav =this.toggleNav.bind(this);
        
    }

    toggleNav() {
        this.setState({isNavOpen: !this.state.isNavOpen});
    }


    render(){

        return(
            <>
                <Navbar className="navbar navbar-expand-lg navbar-dark bg-primary" expand="md">
                    <div className="container">
                        <NavbarBrand className="mr-auto" href="/">Project</NavbarBrand>
                        <NavbarToggler onClick={this.toggleNav} className="mr-2"/>
                        

                        <Collapse isOpen={this.state.isNavOpen} navbar>
                            <Nav className="ml-auto" navbar>
                                <NavItem>
                                    <NavLink href="#">Home</NavLink>
                                    
                                </NavItem>
                                <NavItem>
                                    <NavLink href="#">Search Database</NavLink>
                                    
                                </NavItem>
                                <NavItem>
                                    <NavLink href="#">About</NavLink>
                                    
                                </NavItem>



                            </Nav>

                        </Collapse>

                    </div>

                </Navbar>
                <Jumbotron>
                <div className="container">
                    <div className="row row-header">
                        <div className="col-12 mr-auto col-sm-6">
                            <h1>INF 551 Database Project</h1>
                            <p>Web Application/Firebase</p>

                        </div>

                    </div>
                </div>

            </Jumbotron>
            </>





            

        );

    }
}

export default Header;