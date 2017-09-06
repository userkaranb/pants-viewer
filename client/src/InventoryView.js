import React, { Component } from 'react';
import axios from 'axios';
import InventoryTable from './components/InventoryTable.js'
import ProductDetail from './components/ProductDetail.js'

class InventoryView extends Component {
  constructor(props){
    super(props)
    this.table = this.table.bind(this);
    this.getCurrentProductInventoryId = this.getCurrentProductInventoryId.bind(this);
    this.state = {productAndInventory: [], table_rows: []}
  }

  getCurrentProductInventoryId() {
    let splitUrl = this.props.location.pathname.split('/')
    return splitUrl[splitUrl.length - 1]
  }

  componentWillMount(){
    var url = "http://localhost:5000/products/" + this.getCurrentProductInventoryId()
    axios.get(url).then((response) => {
        this.setState({
            productAndInventory: response.data
        })
    });
  }

  table() {
    if (this.state.productAndInventory.length !==0) {
      var body = {}
      body[this.getCurrentProductInventoryId()] = this.state.productAndInventory
      return <InventoryTable responseBody={body}></InventoryTable>
    }
  }

  render() {
    return (
        <div>
        <a href='/products'>Go Back Home</a>
        <ProductDetail productId={this.getCurrentProductInventoryId()} product={this.state.productAndInventory}></ProductDetail>
        <h1>Inventory</h1>
        {this.table()}
       </div>
    );
  }
}

export default InventoryView;
