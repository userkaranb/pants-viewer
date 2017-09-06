import React, { Component } from 'react';

class ProductDetail extends Component {
  render() {
    return (
      <div key={this.props.productId} id={this.props.productId}>
        <h1>{this.props.product['product_name']}</h1>
        <h4>{this.props.product['product_description']}</h4>
        <div><img src={this.props.product['product_image']} onClick={this.props.onClick} alt={'Picture of Product ' + this.props.productId}/></div>
      </div>
    );
  }
}

export default ProductDetail;
