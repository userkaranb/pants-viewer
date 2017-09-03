import React, { Component } from 'react';
import Request from 'superagent';
class Home extends Component {
  constructor(){
    super()
    this.pantsDiv = this.pantsDiv.bind(this);
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

  pantsDiv(key){
    console.log(this.state.products[key])
     return (
        <div key={key} id={key}>
        <div>{this.state.products[key]['product_name']}</div>
        <div><img src={this.state.products[key]['product_image']}/></div>
        </div>
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

export default Home;
