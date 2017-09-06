import React, { Component } from 'react';
import ReactDataGrid from 'react-data-grid';

class InventoryTable extends Component {
  constructor(props){
    super(props)
    this.createTableRows = this.createTableRows.bind(this);
    this.rowGetter = this.rowGetter.bind(this);
    this._columns = [
      { key: 'productId', name: 'Product Id' },
      { key: 'style', name: 'Style' },
      { key: 'waist', name: 'Waist' },
      { key: 'length', name: 'Length' },
      { key: 'count', name: 'Count' } ];
    this.tableRows = this.createTableRows(this.props.responseBody)
  }

  rowGetter(i) {
    return this.tableRows[i]
  }

  createTableRows(responseBody) {
    var productIdToRows = Object.keys(responseBody).map(function(k) {
          var values = responseBody[k]['inventory_list']
          return Object.values(values).map(function(v){
            return {
              productId: k,
              style: v['style'],
              waist: v['waist'],
              length: v['length'],
              count: v['count'],
            }
          })
        })
        var flattened = [].concat.apply([], productIdToRows)
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
