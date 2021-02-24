import React,{Component} from 'react';
import axios from '../axios';
import Spinner from './Spinner/Spinner';
import {withRouter} from 'react-router'
class Page extends Component{

  state = {
    loading:true,
    post:[]
  }

  componentDidMount(){
    axios.get('post').then(response=>{
      this.setState({
        loading:false,
        post:response.data
      });
      // console.log(response.data)
    })
  }

  PostShowHandler(id){
    this.props.history.push('/' + id);
  }


  render(){
    let post;
    if(this.state.loading){
      post = <Spinner/>
    }
    else{
      post = this.state.post.map(data=>{
        return(
          <button onClick={() => this.PostShowHandler(data.id)}>
              <a>{data.title}</a>
          </button>
        );
      })
    }
    return (
      <div>
        <div>
            {post}
        </div>
      </div>
    );
  }
}

export default withRouter(Page);
