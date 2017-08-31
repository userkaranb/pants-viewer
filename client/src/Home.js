import React, { Component } from 'react';
import Request from 'superagent';
class Home extends Component {
  constructor(){
    super()
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
    let content;
    content = Object.keys(this.state.products).map(
        function(key) {
            return (<div key={key} id={key}/>)
        })

    return (
        <div>
        {content}
       </div>
    );
  }
}

export default Home;
