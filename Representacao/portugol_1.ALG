Algoritmo "Divis�o"

Var
   // Variav�is da
   num1, num2, result: real

Inicio
    // Inserir n�meros da divis�o
    escreva("Digite o primeiro n�mero: ")
    leia(num1)
    escreva("Digite o segundo n�mero: ")
    leia(num2)
    
    // Condi��o da divis�o
    se(num2 <> 0) entao
        result <- num1/num2
        escreva("O valor da divis�o �: ", result)
    senao
        escreva("N�o � poss�vel dividir por 0(zero)")
    fimse

Fimalgoritmo