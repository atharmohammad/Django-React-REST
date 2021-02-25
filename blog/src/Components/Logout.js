import React,{useEffect} from 'react';
import {useHistory,Redirect} from 'react-router-dom';
import axios from '../axios'

export default function Logout (){

    const history = useHistory();
    useEffect(()=>{
      const response = axios.post('user/logout/blacklist/',{
          refresh_token : localStorage.getItem('refresh_token'),
        })
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        axios.defaults.headers['Authorization'] = null;
        console.log(response);
        history.push('/login');
    });

    return(
      <div></div>
    )
}
