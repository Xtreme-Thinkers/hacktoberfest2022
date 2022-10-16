import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {App,view} from './App';


const Index = () => {
  console.log(view);
  return (
    <>
      {view? <p>hello</p> : <App/> }
    </>
    
  )
}




const root = ReactDOM.render(<Index/>,document.getElementById('root'));
