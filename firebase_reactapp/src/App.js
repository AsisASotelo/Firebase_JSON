import React from 'react';
import Header from './components/HeaderComponent';
import Search from './components/SearchComponent';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
      <Search/>
      <h2>Thanks For Visiting!</h2>
    </div>
  );
}

export default App;
