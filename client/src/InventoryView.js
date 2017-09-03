import React, { Component } from 'react';
import Request from 'superagent';
class InventoryView extends Component {
  constructor(props){
    super(props)
    this.state = {products: []}
  }
  
  componentWillMount(){
    var url = "http://localhost:5000/products"
    Request.get(url).then((response) => {
        this.setState({
            products: response.body
        })
    });
  }

  render() {
    return (
        <div>
        <h1>TODO</h1>
       </div>
    );
  }
}

export default InventoryView;
