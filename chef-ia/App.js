import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';

export default function App() {

  function gerarReceita() {
    const [ingredientes, setIngredientes] = useState('') 
  } 

  return (
    <View style={styles.container}>
      <StatusBar style="light" />
      {/*Header*/}
      <View style={styles.header}>
        <Text style={styles.emoji}>🧑‍🍳</Text>
        <Text style={styles.title}>Chef IA Garcia</Text>
        <Text style={styles.subTitle}>Digite os ingredientes que você tem</Text>
      </View>
      {/*Input*/}
      <TextInput 
        style={styles.input}
        placeholder='Ex: frango, arroz, tomate, cebola...'
        multiline
        placeholderTextColor="#888"
        value={}
        onChangeText={}
      />
      {/*Botão*/}
      <TouchableOpacity 
        style={styles.button}
        onPress={gerarReceita}
      >
        <Text style={styles.buttonText}>Gerar Receita</Text>
      </TouchableOpacity>
      {/*Receita*/}
      <View>
        <Text>🥘</Text>
        <Text>Sua Receita aparecerá aqui !</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a1a2e',
    paddingHorizontal: 20,
  },
  header: {
    alignItems: 'center',
    paddingTop: 60,
    paddingBottom: 20
  },
  emoji: {
    fontSize: 50,
    marginBottom: 10
  },
  title: {
    fontSize: 32,
    marginBottom: 10,
    color: '#fff',
    fontWeight: 'bold'
  },
  subTitle: {
    fontSize: 14,  
    color: '#888',
    marginTop: 5
  },
  input: {
    backgroundColor: '#2d2d44',
    borderRadius: 15,
    padding: 15,
    fontSize: 16,
    color: '#fff',
    minHeight: 80,
    textAlignVertical: 'top',
    marginBottom: 15
  },
  button: {
    backgroundColor: '#e17055', 
    paddingVertical: 16,
    borderRadius: 15,
    alignItems: 'center', 
    marginBottom: 15,
    textAlign: 'center',
  },
  buttonText: {
    color: '#fff', 
    fontSize: 16,   
    fontWeight: 'bold'
  }
});
