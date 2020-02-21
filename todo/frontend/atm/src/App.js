import React, { Component } from 'react';

class App extends Component {
  state = {
    accounts: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/users/');
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
      <table border='1'>
      <tr><th>User</th><th>Card number</th><th>Pin</th><th>Amount</th></tr>
        {this.state.accounts.map(item => (
          <tr key={item.id}>
            <td>{item.username}</td>
            <td>{item.card_number}</td>
            <td>{item.pin}</td>
            <td>{item.amount}</td>
          </tr>
        ))}
      </table>
      </div>
    );
  }
}

export default App;