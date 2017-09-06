import React, { Component } from 'react';
import axios from 'axios';
import InventoryTable from './components/InventoryTable.js'
import ProductDetail from './components/ProductDetail.js'

class InventoryView extends Component {
  constructor(props){
    super(props)
    this.table = this.table.bind(this);
    this.getCurrentProductInventoryId = this.getCurrentProductInventoryId.bind(this);
    this.state = {product_and_inventory: [], table_rows: []}
  }

  getCurrentProductInventoryId() {
    let splitUrl = this.props.location.pathname.split('/')
    return splitUrl[splitUrl.length - 1]
  }

  componentWillMount(){
    var url = "http://localhost:5000/products/" + this.getCurrentProductInventoryId()
    axios.get(url).then((response) => {
        this.setState({
            product_and_inventory: response.data
        })
    });
  }

  table() {
    if (this.state.product_and_inventory.length !==0) {
      var body = {}
      body[this.getCurrentProductInventoryId()] = this.state.product_and_inventory
      return <InventoryTable response_body={body}></InventoryTable>
    }
  }

  render() {
    return (
        <div>
        <a href='/products'>Go Back Home</a>
        <ProductDetail product_id={this.getCurrentProductInventoryId()} product={this.state.product_and_inventory}></ProductDetail>
        <h1>Inventory</h1>
        {this.table()}
       </div>
    );
  }
}

export default InventoryView;
