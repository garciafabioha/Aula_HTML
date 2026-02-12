import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Alert } from 'react-native';
import axios from 'axios';

const groq_api_key = process.env.EXPO_PUBLIC_GROQ_API_KEY;

export default function App() {
  const [ingredientes, setIngredientes] = useState('');
  const [receita, setReceita] = useState('');

  const api = axios.create({
    baseURL: 'https://api.groq.com/openai/v1',
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${groq_api_key}`
    }
  });

  async function gerarReceita() {

    if (!ingredientes.trim()) {
      Alert.alert('Atenção', 'Digite alguns ingredientes antes 😉');
      return;
    }

    try {
      const resposta = await api.post('/chat/completions', {
        model: 'llama-3.2-8b-instant',
        temperature: 1,
        max_tokens: 1024,
        message: [
          {
            role: 'system',
            content: `Você é um chef criativo. Crie receitas simples e deliciosas com os
          ingredientes fornecidos. Responda em português do Brasil.`
          },
          {
            role: 'user',
            content: `Crie uma receita com esses ingredientes: ${ingredientes}`
          }
        ]
      });

      Alert.alert(resposta);

      setReceita(resposta.data.choices[0].message.content);
      console.log('✅ Resposta completa:', resposta.data);
      console.log('📝 Texto da receita:', resposta.data.choices?.[0]?.message?.content);

    } catch (error) {
      console.error('❌ Erro ao chamar a API:', error?.response?.data || error.message);
    }
  }

  return (
    <View style={styles.container}>
      <StatusBar style="light" />

      <View style={styles.header}>
        <Text style={styles.emoji}>🧑‍🍳</Text>
        <Text style={styles.title}>Chef IA Garcia</Text>
        <Text style={styles.subTitle}>Digite os ingredientes que você tem</Text>
      </View>

      <TextInput
        style={styles.input}
        placeholder='Ex: frango, arroz, tomate, cebola...'
        multiline
        placeholderTextColor="#888"
        value={ingredientes}
        onChangeText={setIngredientes}
      />

      <TouchableOpacity style={styles.button} onPress={() => gerarReceita()}>
        <Text style={styles.buttonText}>Gerar Receita</Text>
      </TouchableOpacity>

      <View>
        <Text style={{ color: '#fff', marginTop: 10 }}>
          {receita || 'Sua Receita aparecerá aqui!'}
        </Text>
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
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold'
  }
});
