import React, { Component } from 'react';
import axios from 'axios'
import ProductDetail from './components/ProductDetail.js'
import InventoryTable from './components/InventoryTable.js'

class HomeView extends Component {
  constructor(props){
    super(props)
    this.productDetails = this.productDetails.bind(this);
    this.table = this.table.bind(this);
    this.state = {product_and_inventory: [], table_rows: []}
  }
  
  componentWillMount(){
    var url = "http://localhost:5000/products_with_inventory"
    axios.get(url).then((response) => {
        this.setState({
            product_and_inventory: response.data
        })
    });
  }

  productDetails(){
    var products = this.state.product_and_inventory
    return Object.keys(products).map(
       function(product_id) {
         return <ProductDetail key={product_id} product_id={product_id} product={products[product_id]}></ProductDetail>
       }
    )
  }

  table() {
    if(this.state.product_and_inventory.length !== 0) {
      return <InventoryTable response_body={this.state.product_and_inventory}></InventoryTable>
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
