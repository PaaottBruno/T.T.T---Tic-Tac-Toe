import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  var x = 0
  var o = 1

  var xWon = false;
  var oWon = false;

  var area1;
  var area2;
  var area3;
  var area4;
  var area5;
  var area6;
  var area7;
  var area8;
  var area9;

  var array = [[area1],[area2],[area3],
              [area4],[area5],[area6],
              [area7],[area8],[area9]];

  // Mover
  function mover(){
      
      //     |    |
      // ---------------
      //     |    |   
      // ---------------
      //     |    |   
      // Quando clicar no quadrado/posição tem que adicionar o "x" ou "o" cada um tem seu valor
      // o "x" = 0 e "o" = 1, então quando colocado nos lugares o verificador ja esta agindo acada movimento
      // ou seja, sera verificado cada click na tela, ou atualização no proprio jogo.
  }

  // Fim da movimentação

  // Verificação se esta em linha reta o "x" ou "o"
  // Verificação do "x"
  array.forEach(function (row, row_index) {
      row.forEach(function (element, col_index) {

          // Horizontal x
          if (row_index == 0 && array[0][col_index] == 0 && array[1][col_index] == 0 && array[2][col_index] == 0) {
              xWon = true
          }
          else if (row_index == 1 && array[3][col_index] == 0 && array[4][col_index] == 0 && array[5][col_index] == 0) {
              xWon = true
          }
          else if (row_index == 2 && array[6][col_index] == 0 && array[7][col_index] == 0 && array[8][col_index] == 0) {
              xWon = true
          }
          
          //  Vertical x
          else if (row_index == 0 && array[0][col_index] == 0 && array[3][col_index] == 0 && array[6][col_index] == 0) {
              xWon = true
          }
          else if (row_index == 1 && array[1][col_index] == 0 && array[4][col_index] == 0 && array[7][col_index] == 0) {
              xWon = true
          }
          else if (row_index == 2 && array[2][col_index] == 0 && array[5][col_index] == 0 && array[8][col_index] == 0) {
              xWon = true
          }
          
          // Diagonal x
          else if (row_index == 0 && array[0][col_index] == 0 && array[4][col_index] == 0 && array[8][col_index] == 0) {
              xWon = true
          }
          else if (row_index == 1 && array[6][col_index] == 0 && array[4][col_index] == 0 && array[2][col_index] == 0) {
              xWon = true
          }

          if (!xWon) {
            // colocar aviso que deu velha
          }
      });
  }); 

  // Verificação do "o"
  array.forEach(function (row, row_index) {
      row.forEach(function (element, col_index) {
          
          // Horizontal o
          if (row_index == 0 && array[0][col_index] == 1 && array[1][col_index] == 1 && array[2][col_index] == 1) {
              oWon = true
          }
          else if (row_index == 1 && array[3][col_index] == 1 && array[4][col_index] == 1 && array[5][col_index] == 1) {
              oWon = true
          }
          else if (row_index == 2 && array[6][col_index] == 1 && array[7][col_index] == 1 && array[8][col_index] == 1) {
              oWon = true
          }
          
          //  Vertical o
          else if (row_index == 0 && array[0][col_index] == 1 && array[3][col_index] == 1 && array[6][col_index] == 1) {
              oWon = true
          }
          else if (row_index == 1 && array[1][col_index] == 1 && array[4][col_index] == 1 && array[7][col_index] == 1) {
              oWon = true
          }
          else if (row_index == 2 && array[2][col_index] == 1 && array[5][col_index] == 1 && array[8][col_index] == 1) {
              oWon = true
          }
          
          // Diagonal o
          else if (row_index == 0 && array[0][col_index] == 1 && array[4][col_index] == 1 && array[8][col_index] == 1) {
              oWon = true
          }
          else if (row_index == 1 && array[6][col_index] == 1 && array[4][col_index] == 1 && array[2][col_index] == 1) {
              oWon = true
          }
      
          if (!oWon) {
            // colocar aviso que deu velha
          }
      });
  });              
  return (
    <View style={styles.container}>
      <Text>Ola mundo</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'grey',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
