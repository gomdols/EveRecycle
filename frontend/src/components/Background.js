import React, { Component } from 'react';
import { render } from 'react-dom';
import backgroundLogo from './img/recycling-logo.png';

class Background extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: 'Loading'
    };
  }

  componentDidMount() {
    fetch('api/users/')
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: 'Something went wrong!' };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <div>
        <a>
          <img
            src = {backgroundLogo}
            alt = {'Background-Logo'}
          />
        </a>
        
      </div>
    );
  }
}

export default Background;

const container = document.getElementById('background');
render(<Background />, container);