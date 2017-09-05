import React, { Component } from 'react';
import axios from 'axios';
import ReactDataGrid from 'react-data-grid';

class InventoryView extends Component {
  constructor(props){
    super(props)
    this.getCurrentProductInventoryId = this.getCurrentProductInventoryId.bind(this);
    this.createTableRows = this.createTableRows.bind(this);
    this.rowGetter = this.rowGetter.bind(this);
    this._columns = [
      { key: 'style', name: 'Style' },
      { key: 'waist', name: 'Waist' },
      { key: 'length', name: 'Length' },
      { key: 'count', name: 'Count' } ];
    this.state = {product_and_inventory: [], table_rows: []}
  }

  getCurrentProductInventoryId() {
    let splitUrl = this.props.location.pathname.split('/')
    return splitUrl[splitUrl.length - 1]
  }

  createTableRows(response_body) {
    return Object.values(response_body['inventory_list']).map(
        function(value) {
            return {
              style: value['style'],
              waist: value['waist'],
              length: value['length'],
              count: value['count'],
            }
        }, this)
  }

  rowGetter(i) {
    return this.state.table_rows[i]
  }
  
  componentWillMount(){
    var url = "http://localhost:5000/products/" + this.getCurrentProductInventoryId()
    axios.get(url).then((response) => {
        this.setState({
            product_and_inventory: response.data,
            table_rows: this.createTableRows(response.data)
        })
    });
  }

  render() {
    return (
        <div>
        <a href='/products'>Go Back Home</a>
        <h1>{this.state.product_and_inventory['product_name']}</h1>
        <h3>{this.state.product_and_inventory['product_description']}</h3>
        <div><img src={this.state.product_and_inventory['product_image']} alt={'Picture of Product ' + this.state.product_and_inventory['product_id']}/></div>
        <h1>Inventory</h1>
        <div>
          <ReactDataGrid
            columns = {this._columns}
            rowGetter = {this.rowGetter}
            rowsCount = {this.state.table_rows.length}
          />

        </div>
       </div>
    );
  }
}

export default InventoryView;
