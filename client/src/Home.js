import React, { Component } from 'react';
import Request from 'superagent';
class Home extends Component {
  
  componentWillMount(){
    var url = "http://localhost:5000/products"
    Request.get(url).then((response) => console.log(response));
  }

  render() {
    return (
      <form>Hi</form>
    );
  }
}

export default Home;
