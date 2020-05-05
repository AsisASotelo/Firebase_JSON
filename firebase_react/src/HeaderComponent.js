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
            <Jumbotron>
                <div className="container">
                    <div className="row row-header">
                        <div className="col-12 col-sm-6">
                            <h1>Sandy's Food Service</h1>
                            <p>We take inspiration from the World's best cuisines.</p>

                        </div>

                    </div>
                </div>

            </Jumbotron>
            </>


        )

    }
}

export default Header;