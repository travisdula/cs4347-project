import React from 'react';
import logo from './logo.svg';
import './App.css';
import { IncrementalProgramOptions } from 'typescript';


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {stringID: '', intID: 0};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.continueAsGuest = this.continueAsGuest.bind(this);
  }

  handleChange(event)
  {
    this.setState({stringID: event.target.value});
  }

  handleSubmit(event) {
    let testIntID = parseInt(this.state.stringID);
    console.log("int ID: " + testIntID);
    if(testIntID = NaN)
      return;

    this.setState({intID: testIntID});
    //TODO: redirect to home page for registered users!

    event.preventDefault();
  }

  continueAsGuest(event) {
    this.setState({intID: -1});
    console.log("continuing as guest!");
    //TODO: redirect to home page for guest users!
  }

  render() {

    return (
      <div className="App" onSubmit={this.handleSubmit}>
          <p>Welcome to the airport database! Please log in to perform actions, or continuie as guest. You might be required to register to pursue some actions.</p>
          <form>
            <label>CID: </label>
            <input value={this.state.stringID} onChange={this.handleChange} type={"text"}></input>
            <input type={"submit"}></input>
          </form>
          <p><span onClick={this.continueAsGuest}>Continue as guest</span></p>
      </div>
    );
  }
}

export default App;
