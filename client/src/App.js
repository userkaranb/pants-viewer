import React, { Component } from 'react';
import { Router, Route, } from 'react-router';
import { BrowserRouter, } from 'react-router-dom';
import { createHashHistory } from 'history';
import ProductsView from './ProductsView.js';
import InventoryView from './InventoryView'
import './App.css';

const history = createHashHistory()

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <Route exact path="/" exact component={ProductsView}/>
          <Route exact path="/inventory/:id" exact component={InventoryView}/>
        </div>  
      </BrowserRouter>
    );
  }
}

export default App;
