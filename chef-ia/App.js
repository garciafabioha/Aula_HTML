import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { TextInput } from 'react-native/types_generated/index';

export default function App() {
  return (
    <View>
      <StatusBar style="auto" />
      {/*Header*/}
      <View>
        <Text>🧑‍🍳</Text>
        <Text>Chef IA Garcia</Text>
        <Text>Digite os ingredientes que você tem</Text>
      </View>
    {/*Input*/}
      <TextInput>
        
      </TextInput>

    </View>
  );
}

const styles = StyleSheet.create({

});
