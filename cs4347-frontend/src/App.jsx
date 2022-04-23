import React from 'react';
import Login from './Login';
import Test from './test';


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {id: null};

    this.setID = this.setID.bind(this);
  }

  setID(newID)
  {
    this.setState({id: newID});
    console.log("new ID: " + newID);
  }

  render() {

    let login = (<Login setID={this.setID}/>);
    let test = (<Test />);

    return (
      <div className='App'>
        {this.state.id == null && login }
        {this.state.id != null && test}
        <p>current ID: {this.state.id}</p>
      </div>
    );
  }
}

export default App;
