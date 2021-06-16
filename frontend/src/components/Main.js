import React, { Component } from 'react';
import { render } from 'react-dom';
import Background from './Background.js'
import './css/background.css';

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      
    };
  }

  render() {
    return (
      <div>
        <Background></Background>
      </div>
    );
  }
}



export default Main;

const container = document.getElementById('main');
render(<Main />, container);