
import React from 'react';

class Login extends React.Component
{
    constructor(props) {
        super(props);
        this.state = {stringID: ''};
    
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.continueAsGuest = this.continueAsGuest.bind(this);
      }
    
      handleChange(event)
      {
        this.setState({stringID: event.target.value});
      }
    
      handleSubmit(event) {
        event.preventDefault();

        let intID = parseInt(this.state.stringID);
        //TODO: once we connect database, add clause checking if the ID is in the database
        if(isNaN(intID) || intID <= 0)
        {
            alert("not a valid CID! it must be a positive number")
            return;
        }
        else
            this.props.setID(intID);

        //TODO: redirect to home page for registered users!
    
      }
    
      continueAsGuest(event) {
        this.props.setID(-1);
        //TODO: redirect to registration page for guest users!
      }
    
      render() {
    
        return (
          <div onSubmit={this.handleSubmit}>
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

export default Login;