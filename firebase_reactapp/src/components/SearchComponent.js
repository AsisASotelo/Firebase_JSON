import React, { Component } from 'react';
import {Card, CardText, CardBody, CardTitle, } from 'reactstrap';
import { Form, FormGroup, Label, Input, FormFeedback, FormText,Button,Table} from 'reactstrap';
import * as firebase from 'firebase';



const firebaseConfig = {
    apiKey: "AIzaSyCtUWOkZTugbEAU1DlaGnb1-GuJhyh9LSQ",
    authDomain: "inf55-6540d.firebaseapp.com",
    databaseURL: "https://inf55-6540d.firebaseio.com",
    projectId: "inf55-6540d",
    storageBucket: "inf55-6540d.appspot.com",
    messagingSenderId: "594923972530",
    appId: "1:594923972530:web:3e44aeaa306104ac8466ab"
  };

  firebase.initializeApp(firebaseConfig);




class Search extends Component{

    constructor(props){
        super(props);
        this.state={
            data_tuples: null,
            searchKey: "",
            firebase_check: null,
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }
    
    handleSubmit = (event) => {

        alert("A name was enter " + this.state.searchKey)

        const userRef = firebase.database().ref().child(this.state.searchKey);
        
        userRef.on('value', snap =>{
            this.setState({
                data_tuples:snap.val()
                
            });
            console.log(snap.val())
        });
        event.preventDefault();
       
      

    }

    handleChange=(event) =>{
        this.setState({
            searchKey : event.target.value
        })
    }
    
    componentDidMount(){
        
        const rootRef = firebase.database().ref().child('test');
        rootRef.on('value', snap=> {

            this.setState({
                firebase_check:snap.val()    
            });
            console.log(snap.val())
        });
    }

    


        

  
        

        
    


    

   





    render(){
        const {searchKey}=this.state
    return (

        
      <div  className="container">
          <div className="row justify-content-center ">

              <div className="col-sm-12 col-md-5">
                    <Card body className = "text-center"inverse style={{ backgroundColor: '#333', borderColor: '#333' }}>
                        <CardBody>
                            <CardTitle >Welcome!</CardTitle>
                        </CardBody>
                        <CardText>This is the search application for the world database! This application is linked to Firebase! Entering a keyword and hit the search button.</CardText>
                            <CardText>{this.state.firebase_check}</CardText>
                            <CardText>SearchKey:{this.state.searchKey}</CardText>
                            <CardText>Test:{this.state.data_tuples}</CardText>

                        <Form className="form" onSubmit={this.handleSubmit }>
                            <FormGroup>
                                <Label for="exampleEmail"></Label>
                                <Input name = "searchKey" value = {this.state.value} type="text" placeholder="Keyword" id="keyword" onChange={this.handleChange} />
                                <FormFeedback>You will not be able to see this</FormFeedback>
                                
                            

                        
                            <div className="container">
                                <div className="row justify-content-center">
                                    <Button type="submit" className="btn" size="sm">Search</Button>
                                </div>
                            </div>
                            </FormGroup>

                        </Form>
                        
                    </Card>
                </div>

                <div className="col-sm-12 col-md-7 ">
                    <Card>
                    <Table responsive>
                    <thead>
                        <tr>
                        <th>#</th>
                        <th>{this.state.data_tuples}</th>
                        <th>Attribute</th>
                        <th>Rows</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <th scope="row">1</th>
                        <td>ASIS SOTELO SUCSK NUTS</td>
                        <td>Otto</td>
                        <td>@mdo</td>
                        </tr>
                        <tr>
                        <th scope="row">2</th>
                        <td>Jacob</td>
                        <td>Thornton</td>
                        <td>@fat</td>
                        </tr>
                        <tr>
                        <th scope="row">3</th>
                        <td>Larry</td>
                        <td>the Bird</td>
                        <td>@twitter</td>
                        </tr>
                    </tbody>

                    </Table>
                    </Card>
                    




                </div>
        </div>
      </div>

     
    );
  }
}


  export default Search;