import React from 'react';
import {Navbar, NavbarBrand,Jumbotron, Nav, NavbarToggler,Collapse, NavItem} from 'reactstrap';
import { NavLink } from 'react-router-dom';


class Header extends React.Component {

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
            <Navbar dark >
                <div className = "container">
                <NavbarToggler onClick={this.toggleNav}/>
                    <NavbarBrand className="mr-auto" href="/">
                        <img src="assets/images/asis_logo.png" height="200" width="200"
                            alt="logo"/>
                    </NavbarBrand>

                    <Nav navbar>
                        <NavItem className="nav-link" to='/home'>
                            Home
                        </NavItem>
                    </Nav>
                </div>

            </Navbar>



            <Jumbotron fluid>
                <div className="container">
                    <div className="row row-header">
                        <div className="col-12 col-sm-6">
                            <h1>Firebase DB Search</h1>
                            <p>Search Project built with React</p>

                        </div>

                    </div>
                </div>

            </Jumbotron>
            </>


        )

    }
}

export default Header;