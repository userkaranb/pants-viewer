import React, { Component } from 'react';
import ReactDataGrid from 'react-data-grid';

class InventoryTable extends Component {
  constructor(props){
    super(props)
    this.createTableRows = this.createTableRows.bind(this);
    this.rowGetter = this.rowGetter.bind(this);
    this._columns = [
      { key: 'product_id', name: 'Product Id' },
      { key: 'style', name: 'Style' },
      { key: 'waist', name: 'Waist' },
      { key: 'length', name: 'Length' },
      { key: 'count', name: 'Count' } ];
    this.tableRows = this.createTableRows(this.props.response_body)
  }

  rowGetter(i) {
    return this.tableRows[i]
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

  render() {
    return (
        <div>
            <ReactDataGrid
              columns = {this._columns}
              rowGetter = {this.rowGetter}
              rowsCount = {this.tableRows.length}
            />
        </div>
    );
  }
}

export default InventoryTable;
