import React, { Component } from 'react';
import {Card, CardImg, CardText, CardBody, CardLink,
  CardTitle, CardSubtitle
} from 'reactstrap';
import { Form, FormGroup, Label, Input, FormFeedback, FormText,Button,Table} from 'reactstrap';


const Search = (props) => {
    return (
      <div fullheight className="container">
          <div className="row justify-content-center ">

              <div className="col-sm-12 col-md-5">
                    <Card fullheight  body className = "text-center"inverse style={{ backgroundColor: '#333', borderColor: '#333' }}>
                        <CardBody>
                            <CardTitle >Welcome!</CardTitle>
                        </CardBody>
                        <CardText>This is the search application for the world database! This application is linked to Firebase! Entering a keyword and hit the search button.</CardText>

                        <Form>
                            <FormGroup>
                                <Label for="exampleEmail"></Label>
                                <Input placeholder="Keyword" id="keyword" bsSize="sm"/>
                                <FormFeedback>You will not be able to see this</FormFeedback>
                                
                            </FormGroup>

                        </Form>
                        <div className="container">
                            <div className="row justify-content-center">
                                <Button size="sm">Search</Button>
                            </div>
                        </div>
                        
                    </Card>
                </div>

                <div className="col-sm-12 col-md-7 ">
                    <Table responsive>
                    <thead>
                        <tr>
                        <th>#</th>
                        <th>Table Name</th>
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
                    




                </div>
        </div>
      </div>

     
    );
  };
  
  export default Search;