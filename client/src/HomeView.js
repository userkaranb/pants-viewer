import React, { Component } from 'react';
import axios from 'axios'
import ReactDataGrid from 'react-data-grid';

class HomeView extends Component {
  constructor(props){
    super(props)
    this.pantsDiv = this.pantsDiv.bind(this);
    this.createTableRows = this.createTableRows.bind(this);
    this.rowGetter = this.rowGetter.bind(this);
    this._columns = [
      { key: 'product_id', name: 'Product Id' },
      { key: 'style', name: 'Style' },
      { key: 'waist', name: 'Waist' },
      { key: 'length', name: 'Length' },
      { key: 'count', name: 'Count' } ];
    this.state = {product_and_inventory: [], table_rows: []}
  }
  
  componentWillMount(){
    var url = "http://localhost:5000/products_with_inventory"
    axios.get(url).then((response) => {
        this.setState({
            product_and_inventory: response.data,
            table_rows: this.createTableRows(response.data)
        })
    });
  }

  rowGetter(i) {
    return this.state.table_rows[i]
  }

  createTableRows(response_body) {
    var product_id_to_rows = Object.keys(response_body).map(function(k) {
          var values = response_body[k]['inventory_list']
          return Object.values(values).map(function(v){
            return {
              product_id: k,
              style: v['style'],
              waist: v['waist'],
              length: v['length'],
              count: v['count'],
            }
          })
        })
        var flattened = [].concat.apply([], product_id_to_rows)
        return flattened
  }

  pantsDiv(key){
     return (
        <div key={key} id={key}>
        <h1>{this.state.product_and_inventory[key]['product_name']}</h1>
        <h4>{this.state.product_and_inventory[key]['product_description']}</h4>
        <div><img src={this.state.product_and_inventory[key]['product_image']} alt={'Picture of Product ' + key}/></div>
        </div>
    )
  }

  render() {
    let content;
    content = Object.keys(this.state.product_and_inventory).map(
        function(key) {
            return this.pantsDiv(key)  
        }, this)
    return (
        <div>
          <div>
            {content}
          </div>
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

export default HomeView;
