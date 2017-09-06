import React, { Component } from 'react';
import axios from 'axios'
import ProductDetail from './components/ProductDetail.js'

class ProductsView extends Component {
  constructor(props){
    super(props)
    this.pantsDiv = this.pantsDiv.bind(this);
    this.goToInventory = this.goToInventory.bind(this);
    this.state = {products: []}
  }
  
  componentWillMount(){
    var url = "http://localhost:5000/products"
    axios.get(url).then((response) => {
        console.log(response)

        this.setState({
            products: response.data
        })
    });
  }

  goToInventory(id){
    this.props.history.replace('/inventory/' + id)
  }

  pantsDiv(key){
     return (
        <ProductDetail key={key} productId={key} product={this.state.products[key]} onClick={() => this.goToInventory(key)}></ProductDetail>
    )
  }

  render() {
    let content;
    content = Object.keys(this.state.products).map(
        function(key) {
            return this.pantsDiv(key)  
        }, this)

    return (
        <div>
            <h1>Welcome To Bonobos Pants Viewer</h1>
            <h2>Click on An Image to see its inventory</h2>
            {content}
        </div>
    );
  }
}

export default ProductsView;
