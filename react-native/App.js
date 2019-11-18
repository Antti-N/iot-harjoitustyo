/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  Button,
  Component,
  StatusBar,
} from 'react-native';

import {
  Header,
  LearnMoreLinks,
  Colors,
  DebugInstructions,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state={
      vihrea : 'white',
      keltainen: 'white',
      punainen: 'white',
      response : null,
    }
  }

  componentDidMount() {
    //var kierros= 0; 
    this._interval = setInterval(() => {
      this.setState({
        response: getData()
      }, () => 
        //Callback
        {
          // kierros++;
          // console.log("Ollaan kierroksella: "+kierros)
          // console.log("Response: ",this.state.response)
          
          if(this.state.response[0].punainen==1){
            this.state.punainen="red";
          }
          else{
            this.state.punainen="white"
          }
          if (this.state.response[0].keltainen==1){
            this.state.keltainen="yellow"
          }
          else{
            this.state.keltainen="white";
          }
          if(this.state.response[0].vihrea==1){
            this.state.vihrea="green";
          }
          else{
            this.state.vihrea="white";
          }
        }
      );

    }, 1000);
  }


  componentWillUnmount() {
    clearInterval(this._interval);
  }


  render(){
    return (
      <View style={{justifyContent: 'center', alignItems: 'center'}}>
        <Text style={{fontSize:32}}>Nyt on hieno kilke</Text  >
        <Text></Text>
        <View id = 'punainen' style={[styles.circle, {backgroundColor:this.state.punainen}]} /> 
        <View id = 'keltainen' style={[styles.circle, {backgroundColor:this.state.keltainen}]} />
        <View id = 'vihrea' style={[styles.circle, {backgroundColor:this.state.vihrea}]} />
      </View>
    );
  }
};

 
function getData() {
  //console.log("getData")
  var data = [{"id":1,"punainen":0,"vihrea":0,"keltainen":1}];
  // return fetch('http://127.0.0.1:3002/valot')
  //   .then((response) => response.json())
  //   .then((responseJson) => {
  //     console.log(response)
  //     return responseJson;
  //console.log(data)
  return data;
    // })
    // .catch((error) => {
    //   console.error(error);
    // });
}



const styles = StyleSheet.create({
  scrollView: {
    backgroundColor: Colors.lighter,
  },
  engine: {
    position: 'absolute',
    right: 0,
  },
  body: {
    backgroundColor: Colors.white,
  },
  circle: {
    width: 200,
    height: 200,
    borderRadius: 200/2,
    backgroundColor: 'white',
    borderColor: 'black',
    borderWidth: 2
},
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
});

export default App;
