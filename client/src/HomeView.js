import React, { Component } from 'react';
import axios from 'axios'
import ProductDetail from './components/ProductDetail.js'
import InventoryTable from './components/InventoryTable.js'

class HomeView extends Component {
  constructor(props){
    super(props)
    this.productDetails = this.productDetails.bind(this);
    this.table = this.table.bind(this);
    this.state = {productAndInventory: []}
  }
  
  componentWillMount(){
    var url = "http://localhost:5000/products_with_inventory"
    axios.get(url).then((response) => {
        this.setState({
            productAndInventory: response.data
        })
    });
  }

  productDetails(){
    var products = this.state.productAndInventory
    return Object.keys(products).map(
       function(productId) {
         return <ProductDetail key={productId} productId={productId} product={products[productId]}></ProductDetail>
       }
    )
  }

  table() {
    if(this.state.productAndInventory.length !== 0) {
      return <InventoryTable responseBody={this.state.productAndInventory}></InventoryTable>
    }
  }

  render() {
    return (
        <div>
          {this.productDetails()}
          {this.table()}
        </div>
    );
  }
}

export default HomeView;
