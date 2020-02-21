import React, { Component } from 'react';

class App extends Component {
  state = {
    accounts: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const accounts = await res.json();
      this.setState({
        accounts
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.accounts.map(item => (
          <div key={item.id}>
            <h1>{item.username}</h1>
            <h1>{item.card_number}</h1>
            <h5>{item.pin}</h5>
            <h5>{item.amount}</h5>
          </div>
        ))}
      </div>
    );
  }
}

export default App;