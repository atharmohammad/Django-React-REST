import React,{useState,useEffect} from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import {Grid , Paper }from '@material-ui/core';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import {useHistory,NavLink} from 'react-router-dom';
import axios from '../Axios/Login'
import FbLogin from 'react-facebook-login'
import axiosInst from 'axios'

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" to='/'>
        Blog
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function Login() {
  const classes = useStyles();
  const history = useHistory();

  const initialFormData = Object.freeze({
    email:'',
    password:''
  });

  const [formData,updateFormData] = useState(initialFormData);
  const handlechange = (event)=>{
    updateFormData({
      ...formData,
      [event.target.name]:event.target.value,
    })
  };

    // useEffect(()=>{
    // })

  const loginHandler = (event)=>{
    event.preventDefault();

    axiosInst
  			.post(`auth/token/`, {
  				grant_type: 'password',
  				username: formData.email,
  				password: formData.password,
  				client_id: '3l3VNwmdec1Ld18PpH2EM6cIQDaE0z2h7xyv7i8G',
  				client_secret:
  					'HO8R13EnEGyA3zg4CCNKrrGahAPMBOSiPwS4A0zvOA8mMrBzpcyyJbz2h9eX2K2ocW1BZGluDSdYrP1sYwEYsr7jUxHjLSUALj4j0t6zO4jmgGmldHaKJrVMyGKK5Pac',
  			})
  			.then((res) => {
  				localStorage.setItem('access_token', res.data.access_token);
  				localStorage.setItem('refresh_token', res.data.refresh_token);
  				history.push('/');
  				window.location.reload();
  			});


  }

    const responseFacebook = async (response) => {
      // console.log(response)
      axios
    		.post('http://127.0.0.1:8000/auth/convert-token', {
    			token: response.accessToken,
    			backend: 'facebook',
    			grant_type: 'convert_token',
    			client_id: '3l3VNwmdec1Ld18PpH2EM6cIQDaE0z2h7xyv7i8G',
    			client_secret:
    				'HO8R13EnEGyA3zg4CCNKrrGahAPMBOSiPwS4A0zvOA8mMrBzpcyyJbz2h9eX2K2ocW1BZGluDSdYrP1sYwEYsr7jUxHjLSUALj4j0t6zO4jmgGmldHaKJrVMyGKK5Pac',
    		})
    		.then((res) => {
    			localStorage.setItem('access_token', res.data.access_token);
    			localStorage.setItem('refresh_token', res.data.refresh_token);
          history.push('/');
          window.location.reload();
    		});

    };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
        </Avatar>
        <Typography component="h1" variant="h5">
          Login
        </Typography>
        <form className={classes.form} noValidate>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                onChange={handlechange}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                onChange={handlechange}
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick={loginHandler}
          >
            Login
          </Button>
          <FbLogin
						appId="262218718682544"
						fields="name,email,picture"
						callback={responseFacebook}
					/>
          <Grid container justify="flex-end">
            <Grid item>
              <NavLink to='/register' variant="body2">
                Don't Have account ? Sign up
              </NavLink>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
        <Copyright />
      </Box>
    </Container>
  );
}
