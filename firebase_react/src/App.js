import React,{Component} from 'react';
import Header from './HeaderComponent';
import './App.css';
import * as firebase from 'firebase';
import "firebase/auth"
import "firebase/firestore";

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

class App extends Component {

  constructor(){
    super();
    this.state={
      speed:10

    };
  }

  componentDidMount(){

    const rootRef=firebase.database().ref().child('react');
    const speedRef=rootRef.child('speed');
    speedRef.on('value',snap=>{
      this.setState({
        speed:snap.val()

      });


    });
    
  }

  render(){
    return (
      <div className="App">
        <Header></Header>
        <h1>{this.state.speed}</h1>
        <input type="Search" placeholder="Search Database "></input>
      </div>
    );
  }
}

export default App;
