import React from 'react';
import Login from './Login';


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {id: 0};

    this.setID = this.setID.bind(this);
  }

  setID(newID)
  {
    this.setState({id: newID});
    console.log("new ID: " + newID);
  }

  render() {
    return (
      <div className='App'>
        <Login setID={this.setID}/>
        <p>current ID: {this.state.id}</p>
      </div>
    );
  }
}

export default App;
