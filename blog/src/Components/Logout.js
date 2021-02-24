import React,{useEffect} from 'react';
import {useHistory,Redirect} from 'react-router-dom';
import axios from '../axios'

export default function Logout (){

    const history = useHistory();
    useEffect(()=>{
      axios.post('user/logout/blacklist',{
          refresh_token : localStorage.getItem('refresh_token')
        }).then((response)=>{
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          axios.defaults.headers['Authorization'] = null;
            history.push('/login');
        })
        .catch(err=>console.log(err));

    });

    return(
      <div></div>
    )
}
