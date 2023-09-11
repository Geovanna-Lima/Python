Algoritmo "Divisão"

Var
   // Variavéis da
   num1, num2, result: real

Inicio
    // Inserir números da divisão
    escreva("Digite o primeiro número: ")
    leia(num1)
    escreva("Digite o segundo número: ")
    leia(num2)
    
    // Condição da divisão
    se(num2 <> 0) entao
        result <- num1/num2
        escreva("O valor da divisão é: ", result)
    senao
        escreva("Não é possível dividir por 0(zero)")
    fimse

Fimalgoritmo