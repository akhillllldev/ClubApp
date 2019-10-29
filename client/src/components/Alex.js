import React from 'react';
import { Message } from 'semantic-ui-react';

class Alex extends React.Component {
  componentDidMount() {
    console.log('Component mounted!!!');
  }

  render() {
    console.log('Render will be called later');
    return (
      <div
        style={{
          fontSize: '30px'
        }}>
        Hi, {this.props.baapKaData.name} is my dad
        <Message>
          <Message.Header>Changes in Service</Message.Header>
          <p>
            We updated our privacy policy here to better service our customers.
            We recommend reviewing the changes.
          </p>
        </Message>
      </div>
    );
  }
}

export default Alex;
