import React, { Component } from 'react';

class ProductDetail extends Component {
  render() {
    return (
      <div key={this.props.product_id} id={this.props.product_id}>
        <h1>{this.props.product['product_name']}</h1>
        <h4>{this.props.product['product_description']}</h4>
        <div><img src={this.props.product['product_image']} alt={'Picture of Product ' + this.props.product_id}/></div>
      </div>
    );
  }
}

export default ProductDetail;
