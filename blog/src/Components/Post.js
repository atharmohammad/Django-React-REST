import React,{useState,useEffect} from 'react';
import {useParams} from 'react-router-dom';
import axios from '../axios';
import Spinner from './Spinner/Spinner';

export default function Post(){
  const {id} = useParams();
  const [data,setData] = useState({post:[]});

  useEffect(()=>{
    axios.get('/'+id)
    .then(res=>{
      setData({post:res.data})
    })
    .catch(err=>console.log(err))
  },[setData])



  return(
    <div>
      <h1>{data.post.title}</h1>
      <p>{data.post.content}</p>
    </div>

  );
}
