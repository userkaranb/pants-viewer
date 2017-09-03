import React, { Component } from 'react';
import Request from 'superagent';
class InventoryView extends Component {
  constructor(props){
    super(props)
    this.state = {inventory: []}
  }
  
  componentWillMount(){
  }

  render() {
    console.log('inventory')
    return (
        <div>
        <h1>TODO</h1>
       </div>
    );
  }
}

export default InventoryView;
