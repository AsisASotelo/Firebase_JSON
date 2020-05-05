import React, {Component} from "react";

class Search extends Component {
    state={};

    render(){
        return (

            <div className="container">
                    <div className="row">

                        <h1>Welcome to INF_551 Database Search</h1>
                        <input className="col-12 col-md-7" name="text" type="text" placeholder="Enter Keyword" />
                        <button className="col-md-12">Search</button>

                    </div>  
            </div>

        );
    }
}

export default Search;

