import React from 'react';
import Header from './components/HeaderComponent';
import Search from './components/SearchComponent';
import Footer from './components/FooterComponent';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
     
      <div className="m-1">
        <Search/>
      </div >
      <div style= {{margin:50}} className="m-3">
        <Footer/>
      </div>
      
      
    </div>
  );
}

export default App;
