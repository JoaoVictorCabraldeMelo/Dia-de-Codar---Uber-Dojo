# Number In Words
  Em muito sistemas financeiros temos que escrever a quantia e sua forma por extenso
Dado este problema vamos tentar resolve-lo

  ## Como funciona:
    Recebe um número e retorna ele escrito de forma extensa 
  - Ex: 42 
        forty and two dollars
  - Ex: 742
        seven hundred and forty and two dollars
  - Ex: 4422
        four thousand and four hundred and twenty two dollars
  - Ex: 4242215
        four million and two hundred forty two thousands and two hundred fifteen
  
  ## Segunda Parte:
    Recebe uma string por extenso do número e transforma em numero
  - Ex: forty and two dollars
        42

  - Ex: seven hundred and forty and two dollars
        742

  - Ex: four thousand and four hundred and twenty two dollars
        4422

  - Ex: four million and two hundred forty two thousands and two hundred fifteen
        4242215
  ## TDD
    Seguir o Red, Green, Refactor que segue estas etapas:
      - Faz o teste para um determinada funcionalidade do programa
      - Falha no teste pois não está implementada
      - Faz o código pra passar no teste
      - Passa no teste
      - Refaz o código para uma forma mais elegante
