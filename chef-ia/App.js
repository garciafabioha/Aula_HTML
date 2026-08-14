import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Alert, ScrollView } from 'react-native';
import axios from 'axios';
import { EXPO_PUBLIC_GROQ_API_KEY } from '@env';

export default function App() {
  const [ingredientes, setIngredientes] = useState('');
  const [receita, setReceita] = useState('');
  const [modoPreparo, setModoPreparo] = useState('');


  const api = axios.create({
    baseURL: 'https://api.groq.com/openai/v1',
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${EXPO_PUBLIC_GROQ_API_KEY}`
    }
  });

  async function gerarReceita() {

    if (!ingredientes.trim()) {
      Alert.alert('Atenção', 'Digite alguns ingredientes antes 😉');
      return;
    }

    try {
      const resposta = await api.post('/chat/completions', {
        model: 'llama-3.1-8b-instant',
        temperature: 1,
        max_tokens: 1024,
        messages: [
          {
            role: 'system',
            content: 'Você é um chef criativo. Crie receitas simples e deliciosas com os ingredientes fornecidos. Responda em português do Brasil.'
          },
          {
            role: 'user',
            content: `Crie uma receita com esses ingredientes: ${ingredientes}.

                      Responda no formato abaixo:

                      Nome da receita:
                      Ingredientes:
                      - item 1
                      - item 2
                      - etc

                      Como preparar:
                      1. Passo 1
                      2. Passo 2
                      3. etc

                      Tempo de preparo:
                      Rendimento:
                      Dicas:`
          }
        ]
      });

      setReceita(resposta.data.choices[0].message.content);

    } catch (error) {
      const code = error?.response?.data?.error?.code;
      if (code === 'model_decommissioned' || code === 'model_not_found') {
        Alert.alert('Modelo indisponível', 'Atualizando modelo da IA. Tente novamente em instantes.');
      } else {
        Alert.alert('Erro', 'Falha ao gerar receita. Veja o console.');
      }
    }
  }

  async function gerarModoPreparo() {
    try {
      const resposta = await api.post('/chat/completions', {
        model: 'llama-3.1-8b-instant',
        temperature: 0.7,
        max_tokens: 512,
        messages: [
          {
            role: 'system',
            content: 'Você é um chef. Explique o modo de preparo passo a passo de forma simples.'
          },
          {
            role: 'user',
            content: `Explique como preparar a seguinte receita:\n\n${receita}`
          }
        ]
      });

      setModoPreparo(resposta.data.choices[0].message.content);
    } catch {
      Alert.alert('Erro', 'Falha ao gerar modo de preparo.');
    }
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
        value={ingredientes}
        onFocus={() => setReceita('')}
        onChangeText={(text) => {
          setIngredientes(text);
          if (!text.trim()) setReceita('');
        }}
      />
      {/*Botão*/}
      <TouchableOpacity style={styles.button} onPress={() => gerarReceita()}>
        <Text style={styles.buttonText}>Gerar Receita</Text>
      </TouchableOpacity>
      {/*Receita*/}
      {/*If se a receita chegar da IA, senão mostra o padrão*/}
      {receita ? (
        <View style={styles.receitaWrapper}>
          <View style={styles.receitaHeader}>
            <Text style={styles.receitaHeaderText}>Sua Receita</Text>
          </View>
          <ScrollView style={styles.receitaContainer}>
            <Text style={styles.receita}>{receita}</Text>
          </ScrollView>
        </View>
      ) : (
        <View style={styles.placeholderContainer}>
          <Text style={styles.placeholderEmoji}>🍳</Text>
          <Text style={styles.placeholderText}>Sua Receita aparecerá aqui !</Text>
        </View>
      )}
      {/*Modo de Preparo*/}
      {receita ? (
        <TouchableOpacity
          style={[styles.button, { backgroundColor: '#6c5ce7' }]}
          onPress={() => gerarModoPreparo()}
        >
          <Text style={styles.buttonText}>Como preparar</Text>
        </TouchableOpacity>
      ) : null}
      {/*Modo de Preparo*/}
      {modoPreparo ? (
        <View style={styles.receitaWrapper}>
          <View style={styles.receitaHeader}>
            <Text style={styles.receitaHeaderText}>Como Preparar</Text>
          </View>
          <ScrollView style={styles.receitaContainer}>
            <Text style={styles.receita}>{modoPreparo}</Text>
          </ScrollView>
        </View>
      ) : null}

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
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold'
  },
  receitaWrapper: {
    flex: 1,
    marginBottom: 30,
    borderRadius: 20,
    overflow: 'hidden',
    backgroundColor: '#2d2d44',
  },
  receitaHeader: {
    backgroundColor: '#e17055',
    paddingVertical: 12,
    paddingHorizontal: 15,
  },
  receitaHeaderText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  receitaContainer: {
    flex: 1,
    padding: 20,
  },
  receita: {
    color: '#fff',
    fontSize: 16,
    lineHeight: 26,
  },
  placeholderContainer: {
    flex: 1,
    alignContent: 'center',
  },
  placeholderEmoji: {
    fontSize: 32,
    marginBottom: 15,
  },
  placeholderText: {
    color: '#666',
    fontSize: 16,
  }

});
