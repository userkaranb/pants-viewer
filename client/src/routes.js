import React from 'react'
import { IndexRoute, Route, } from 'react-router'
import ProductsView from './ProductsView'
import InventoryView from './InventoryView'

const Routes = (
  <Route path="/" component={ProductsView}>
    <Route path="/inventory/:id" component={InventoryView}/>
  </Route>
)

export default Routes
