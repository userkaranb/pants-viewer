import React, { Component } from 'react';
import { Route, } from 'react-router';
import { BrowserRouter, } from 'react-router-dom';
import ProductsView from './ProductsView.js';
import InventoryView from './InventoryView'
import './App.css';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <switch>
          <Route path="/" exact component={ProductsView}/>
          <Route path="/products" exact component={ProductsView}/>
          <Route path="/inventory/:id" exact component={InventoryView}/>
        </switch>
      </BrowserRouter>
    );
  }
}

export default App;
