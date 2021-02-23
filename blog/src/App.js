import React,{Component} from 'react';
import axios from './axios';
import Spinner from './Components/Spinner/Spinner';
import Layout from './Components/Layout'
import Page from './Components/Page'
import Login from './Components/Login'
import Logout from './Components/Logout'
import Register from './Components/Register'
import {BrowserRouter,Route,Switch} from 'react-router-dom'
import Post from './Components/Post'

function App (props){

    let routes = (
      <Switch>
        <Route exact path='/logout' component={Logout}/>
        <Route exact path='/login' component={Login}/>
        <Route exact path='/register' component={Register}/>
        <Route exact path='/:id' component={Post}/>
        <Route exact path='/' component={Page}/>
      </Switch>
    );

    return (

        <BrowserRouter>
            <div>
              <Layout>
              {routes}
              </Layout>
            </div>
        </BrowserRouter>

    );

}

export default App;
