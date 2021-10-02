import * as React from 'react';
import { View, Text } from 'react-native';

export default class PopularScreen extends React.component {
  constructor(){
    super();
    this.state = {
      data: []
    }
  }
  getdata() {
    const url = "http://127.0.0.1:5000/"

  }
  componentDidMount(){
    this.getdata();
  }
  render(){
    return(
      <View>
        <Text>Popular Screen</Text>
      </View>
    )
  }
}