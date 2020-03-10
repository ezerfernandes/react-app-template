import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.scss';
import MouseIcon from '@material-ui/icons/Mouse';
import MyPayPalButton from "./components/MyPalPalButton";
import LoginBoxWithVerticalDivider from './components/LoginBoxWithVerticalDivider';
import { Button, Icon, Label } from 'semantic-ui-react';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <MouseIcon /><a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      <p>The current time is {currentTime}.</p>
      <p><MyPayPalButton /></p>
      <div>
        <Button primary>Primary</Button>
        <Button secondary>Secondary</Button>
      </div>
      <div>
        <Button as='div' labelPosition='left'>
          <Label as='a' basic>
            2,048
          </Label>
          <Button icon>
            <Icon name='fork' />
          </Button>
        </Button>
        
      </div>
      <LoginBoxWithVerticalDivider />
      </header>
    </div>
  );
}

export default App;
