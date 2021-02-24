import React,{useState,useEffect} from 'react';
import {useParams,useHistory} from 'react-router-dom';
import axios from '../axios';
import Spinner from './Spinner/Spinner';

export default function Post(){
  const {id} = useParams();
  const history = useHistory();
  const [data,setData] = useState({post:[]});

  useEffect(()=>{
    axios.get('/'+id)
    .then(res=>{
      setData({post:res.data})
    })
    .catch(err=>console.log(err))
  },[setData])

  const deleteHandler = ()=>{
    axios.delete('/'+id)
        .then(res=>{
            console.log(res);
        })
        .catch(err=>console.log(err));

        history.push('/')
  }

  return(
    <div>
      <h1>{data.post.title}</h1>
      <p>{data.post.content}</p>
      <button onClick={deleteHandler}>Delete</button>
    </div>

  );
}
