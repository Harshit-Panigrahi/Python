import * as React from "react";
import { Text, View } from "react-native";
import HomeScreen from "./screens/Home";
import RecommendationScreen from "./screens/recommendation";
import PopularScreen from "./screens/popular";
import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import { createMaterialTopTabNavigator } from "react-navigation-tabs";
import { RFValue } from "react-native-responsive-fontsize";

export default function App() {
	return <Appcontainer />;
}

const AppTopNavigation = createMaterialTopTabNavigator({
	RecommendedMovie: {
		screen: RecommendationScreen,
		navigationOptions: {
			tabBarLabel: "Recommended",
			tabBarOptions: {
				tabStyle: { backgroundColor: "#fff" },
				labelStyle: { color: "#000" },
				indicatorStyle: { backgroundColor: "#000" },
			},
		},
	},
	PopularMovies: {
		screen: PopularScreen,
		navigationOptions: {
			tabBarLabel: "Popular",
			tabBarOptions: {
				tabStyle: { backgroundColor: "#fff" },
				labelStyle: { color: "#000" },
				indicatorStyle: { backgroundColor: "#000" },
			},
		},
	},
});

const AppStackNavigator = createStackNavigator({
  Home: {
    screen: HomeScreen,
    navigationOptions: {
      header: false
    }
  },
  AppTopNav : {
    screen: AppTabNavigation,
    navigationOptions: {
      headerBackTitle: null,
      headerTintColor: '#fff',
      headerTitle: "Recommended Movies",
      headerStyle: {
        backgroundColor: "#df6789"
      },
      headerTitleStyle: {
        color: "#000",
        fontSize: RFValue(18),
        fontWeight: "bold"
      }
    }
  }
},
{
  initialRouteName: "Home"
}
);

const Appcontainer = createAppContainer(AppStackNavigator)
