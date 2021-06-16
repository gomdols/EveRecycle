import React, { Component } from 'react';
import backgroundLogo from './img/recycling-logo.png';
import Nav from './Nav.js';

class Background extends Component {
  constructor(props) {
    super(props);
    this.state = {

    };
  }

  render() {
    return (
      <div className='wrapper'>
        <a className='logo' href='/' target='_self'>
          <img
            src = {backgroundLogo}
            alt = 'Background-Logo'
          />
        </a>
        <Nav></Nav>
        <Index></Index>
      </div>
    );
  }
}

class Index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      
    };
  }

  render() {
    return (
      <div className='contents'>
        <h1>에브리사이클</h1>
        <p className='subtitle'>
          모든 생각의 재활용
        </p>
        <IndexInfo></IndexInfo>
      </div>
    );
  }
}

class IndexInfo extends Component{
  constructor(props) {
    super(props);
    this.state = {
      
    };
  }

  render() {
    return(
      <div>
        <p className='content1'>
          평소 쓸일 없는, 쓸모 없는, 쓸 수 없는 아이디어를<br/>
          쓰레기통에 구겨 버리지 마세요. 
        </p>
        <p className='content2'>
          충분히 놀라운 아이디어가 될 수 있습니다.<br/>
          에브리사이클에서 사람들과 당신의 아이디어를 세상에 구현하세요.
        </p>
      </div>
    );
  }
}

export default Background;
