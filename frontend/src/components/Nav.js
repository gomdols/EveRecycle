import React, { Component } from 'react';
import './css/background.css';

class Nav extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isToggleOn: false,
    };
    this.navClick = this.navClick.bind(this);
  }

  navClick(){
    this.setState(state => ({
      isToggleOn: !state.isToggleOn,
    }));
  }

  render() {
    let navClass = this.state.isToggleOn ? 'toggleOn' : 'toggleOff';
    let navStripText = this.state.isToggleOn ? '눌러서 메뉴 닫기' : '눌러서 메뉴 열기'
    return (  
      <nav id='nav' className={navClass}>
        <div className='nav-strip' onClick={this.navClick}>
          <span>
            {navStripText}
          </span>
        </div>

      </nav>
    );
  }
}

export default Nav;