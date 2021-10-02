import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity } from 'react-native';
import { Header, Icon, Airbnbrating } from 'react-native-elements';
import { RFValue } from 'react-native-responsive-fontsize';
import axios from 'axios';

export default class HomeScreen extends React.Component {
  constructor() {
    super();
    this.state = {
      movieDetails: {},
    };
  }
  convert(x) {
    h = Math.floor(x/60)
    m = x%60
    return `${h} hrs ${m} mins`
  }
  getMovies = () => {
    const url = "http://127.0.0.1:5000/get-movies"
    axios.get(url).then((response)=>{
      var details = response.data.data
      details["runtime"] = this.convert(details.runtime)
      this.setState({
        movieDetails: details
      })
    }).catch((error)=>{
      console.log(error.message)
    })
  }
  componentDidMount() {
    this.getMovies()
  }
  render() {
    const {movieDetails} = this.state
    return (
      <View>
        <Text>Home Screen</Text>
      </View>
    );
  }
}
