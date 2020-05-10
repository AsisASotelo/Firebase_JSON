import React, { Component } from 'react';
import {Card, CardText, CardBody, CardTitle, } from 'reactstrap';
import { Form,CardHeader, FormGroup, Label, Input, FormFeedback, FormText,Button,Table,} from 'reactstrap';
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



function RenderTable(object) {

    
    if(object!= null){
        
        
        console.log(Object.keys(object.object))
        return(
            <Table striped bordered hover responsive>
                <thead class="table-dark">
                    <tr>
                    <th>Document</th>
                    <th>Rows</th>
                    </tr>
                </thead>

                <tbody>
                    {Object.keys(object.object).map((key,i) => (
                        
                            <tr class="table-active" key = {i}>
                                <th scope="row">{key}</th>
                                <td class="user">{object.object[key].toString()}</td>
                            </tr>
                        )
                    )}

                </tbody>

                

            </Table>
            
        )
           


       

    }


    else{
        return(
            <Table>
                <thead>
                    <tr>
                    <th>#</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Username</th>
                    </tr>
                </thead>

            </Table>
        );
    }

    return(<div></div>);


}


class Search extends Component{

    constructor(props){
        super(props);
        this.state={
            data_tuple:[],
            searchKey: "",
            firebase_check: null,
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }
    
    handleSubmit = (event) => {

        alert("A name was enter " + this.state.searchKey)

        const userRef = firebase.database().ref("index/" + this.state.searchKey);
        
        userRef.on('value', snap =>{
            
            this.setState({
                data_tuple:snap.val()

            })

            
            


            // console.log(snap.val())
            // console.log("value of data tuple is " + this.state.data_tuple)
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
                        <CardHeader>WELCOME</CardHeader>
                        <CardBody>
                            
                            
                            
                        </CardBody>
                        <CardText>This is the search application for the world database! This application is linked to Firebase! Entering a keyword and hit the search button.</CardText>
                            <CardText>{this.state.firebase_check}</CardText>
                            <CardText>SearchKey:{this.state.searchKey}</CardText>
                            

                        <Form className="form" onSubmit={this.handleSubmit }>
                            <FormGroup>
                                <Label for="exampleEmail"></Label>
                                <Input name = "searchKey" value = {this.state.value} type="text" placeholder="Keyword" id="keyword" onChange={this.handleChange} />
                                <FormFeedback>You will not be able to see this</FormFeedback>
                                
                            

                        
                            <div className="container">
                                <div className="row justify-content-center">
                                    <Button type="submit" className="btn m-2" size="sm">Search</Button>
                                </div>
                            </div>
                            </FormGroup>

                        </Form>
                        
                    </Card>
                </div>

                <div className="col-sm-12 col-md-7 ">
                    <Card>
                        <RenderTable object= {this.state.data_tuple} /> 
                    </Card>
                    
    
                    

                    
                    
                    




                </div>
        </div>
      </div>

     
    );
  }
}


  export default Search;